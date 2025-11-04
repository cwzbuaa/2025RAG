import json
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import time
from langchain_community.vectorstores import FAISS
import numpy as np
from pathlib import Path
import re
import os
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import DashScopeEmbeddings

# ----------------------------
# 1. 配置 DashScope 嵌入模型（使用 1024 维度模型）
# ----------------------------
embedding_model = DashScopeEmbeddings(
    model="text-embedding-v4",  # 使用 1024 维度的模型
    dashscope_api_key="sk-"
)

# ----------------------------
# 2. 测试嵌入模型维度
# ----------------------------
test_embedding = embedding_model.embed_query("测试文本")

# ----------------------------
# 3. 加载 FAISS 向量库（使用相同的嵌入模型）
# ----------------------------
vectorstore = FAISS.load_local("../faiss_index", embedding_model, allow_dangerous_deserialization=True)

# ----------------------------
# 4. 配置 LLM（Qwen 模型）
# ----------------------------
llm = ChatOpenAI(
    api_key="sk-",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-flash",
    temperature=0.1
)
print("✅ LLM 配置成功")

# ----------------------------
# 5. 构建 RAG 链
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
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    chain_type_kwargs={"prompt": PROMPT},
    return_source_documents=True
)

# ----------------------------
# 6. 测试问答
# ----------------------------
if __name__ == "__main__":
    query = "番茄炒蛋怎么做"
    print(f"问题：{query}\n")
    

    result = qa_chain.invoke({"query": query})
    
    # 打印召回的 top-3 文档
    print("\n=== Retrieved Documents (Top-3) ===")
    for i, doc in enumerate(result["source_documents"]):
        print(f"\n--- Source {i+1} ---")
        print("Content:", doc.page_content[:300] + "..." if len(doc.page_content) > 300 else doc.page_content)
        print("Metadata:", doc.metadata)

    print("✅ 回答：")
    print(result["result"].strip())
    
        