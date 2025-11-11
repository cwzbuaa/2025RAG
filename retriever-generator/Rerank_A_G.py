import json
import requests
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from pydantic.v1 import BaseModel, Field
from typing import List, Optional
from langchain.schema import Document
import time
from langchain_core.retrievers import BaseRetriever
from langchain_core.callbacks import CallbackManagerForRetrieverRun
# 导入 ConfigDict 用于 Pydantic v2 配置
from pydantic import ConfigDict


class RerankChain:
    def __init__(self, api_key: str, model: str = "qwen3-rerank"):
        self.api_key = api_key
        self.model = model
        self.url = "https://dashscope.aliyuncs.com/api/v1/services/rerank/text-rerank/text-rerank"
    
    def rerank(self, query: str, documents: List[str], top_n: int = 3, return_documents: bool = True):
        """
        使用千问重排模型对文档进行重排
        """
        payload = {
            "model": self.model,
            "input": {
                "query": query,
                "documents": documents
            },
            "parameters": {
                "return_documents": return_documents,
                "top_n": top_n
            }
        }
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(self.url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise Exception(f"重排 API 请求失败: {response.status_code}, {response.text}")
        
        result = response.json()
        
        # 解析重排结果
        reranked_docs = []
        if 'output' in result and 'results' in result['output']:
            for item in result['output']['results']:
                if 'document' in item:
                    doc_data = item['document']
                    # 创建 LangChain Document 对象
                    doc = Document(
                        page_content=doc_data.get('text', ''),
                        metadata={
                            'score': item.get('relevance_score', 0),
                            'index': doc_data.get('index', -1)
                        }
                    )
                    reranked_docs.append(doc)
        
        return reranked_docs

class RerankRetriever(BaseRetriever): # 继承 BaseRetriever
    # 定义字段
    vectorstore: object = Field(default=None, description="向量存储")
    rerank_chain: object = Field(default=None, description="重排链")
    top_k: int = Field(default=5, description="先召回的文档数量")
    rerank_top_n: int = Field(default=3, description="重排后返回的文档数量")
    
    # 使用 Pydantic v2 推荐的 model_config
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        # 1. 先从向量库召回 top_k 个文档
        initial_docs = self.vectorstore.similarity_search(query, k=self.top_k)
        
        # 2. 提取文档内容用于重排
        doc_texts = [doc.page_content for doc in initial_docs]
        
        # 3. 使用重排模型对召回的文档进行重排
        reranked_docs = self.rerank_chain.rerank(
            query=query,
            documents=doc_texts,
            top_n=self.rerank_top_n
        )
        
        # 4. 将重排后的文档按分数排序（降序）
        reranked_docs.sort(key=lambda x: x.metadata.get('score', 0), reverse=True)
        
        return reranked_docs

# ----------------------------
# 1. 配置 DashScope 嵌入模型（使用 1024 维度模型）
# ----------------------------
from langchain_community.embeddings import DashScopeEmbeddings

embedding_model = DashScopeEmbeddings(
    model="text-embedding-v4",  # 使用 1024 维度的模型
    dashscope_api_key="sk-f1d25d991a2f4b1699daf8bc3c8d880b"
)
print("✅ 嵌入模型初始化成功")

# ----------------------------
# 2. 测试嵌入模型维度
# ----------------------------
test_embedding = embedding_model.embed_query("测试文本")
print(f"✅ 嵌入维度：{len(test_embedding)}")

# ----------------------------
# 3. 加载 FAISS 向量库
# ----------------------------
vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
print("✅ 向量库加载成功")

# ----------------------------
# 4. 配置千问重排链
# ----------------------------
rerank_chain = RerankChain(
    api_key="sk-f1d25d991a2f4b1699daf8bc3c8d880b",
    model="qwen3-rerank"
)
print("✅ 重排链配置成功")

# ----------------------------
# 5. 创建带重排功能的检索器
# ----------------------------
rerank_retriever = RerankRetriever(
    vectorstore=vectorstore,
    rerank_chain=rerank_chain,
    top_k=7,        # 先召回 5 个文档
    rerank_top_n=3  # 重排后返回 3 个最相关文档
)
print("✅ 重排检索器创建成功")

# ----------------------------
# 6. 配置 LLM（Qwen 模型）
# ----------------------------
llm = ChatOpenAI(
    api_key="sk-f1d25d991a2f4b1699daf8bc3c8d880b",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-flash",
    temperature=0.1,
)
print("✅ LLM 配置成功")

# ----------------------------
# 7. 构建 RAG 链（带重排功能）
# ----------------------------
prompt_template = """你是一个专业的烹饪助手。请仅根据以下上下文信息回答问题，不要编造内容。

上下文：
{context}

问题：{question}

回答："""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=rerank_retriever,  # 使用带重排功能的检索器
    chain_type_kwargs={"prompt": PROMPT},
    return_source_documents=True
)

# ----------------------------
# 8. 测试问答
# ----------------------------
if __name__ == "__main__":
    query = "适合健身的低脂餐"
    print(f"问题：{query}\n")
    

    start_time = time.time()
    result = qa_chain.invoke({"query": query})
    end_time = time.time()
    
    print(f"=== 检索和生成耗时: {end_time - start_time:.2f} 秒 ===\n")
    
    # 打印重排后的文档（按相关性分数排序）
    print("\n=== 重排后的文档 (Top-3) ===")
    for i, doc in enumerate(result["source_documents"]):
        score = doc.metadata.get('score', 0)
        print(f"\n--- 文档 {i+1} (相关性分数: {score:.4f}) ---")
        print("Content:", doc.page_content[:300] + "..." if len(doc.page_content) > 300 else doc.page_content)
        print("Meta", doc.metadata)

    print("\n✅ 最终回答：")
    print(result["result"].strip())