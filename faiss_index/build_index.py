import json
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
import time
from openai import OpenAI
from langchain_community.vectorstores import FAISS
import numpy as np
from pathlib import Path
import re
# ----------------------------
# 1. 加载你的 JSONL 文件（适配你的字段）
# ----------------------------
file_path = "data/chunked_corpus_fuzi/chunked_corpus.jsonl"

def clean_text_for_embedding(text: str) -> str:
    # 移除所有控制字符（除了 \n \r \t）
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
    # 确保反斜杠被正确处理（可选）
    text = text.replace("\\\\", "\\").replace("\\", "＼")  # 把 \ 转为全角，避免转义
    return text.strip()


def load_chunks_from_jsonl(file_path):
    documents = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            data = json.loads(line.strip())
            page_content = clean_text_for_embedding(data["child_content"])
            metadata = data.get("metadata", {})
            metadata["chunk_id"] = data.get("chunk_id", "")
            doc = Document(page_content=page_content, metadata=metadata)
            documents.append(doc)
    return documents

# 加载文档
chunks = load_chunks_from_jsonl(file_path)  # 替换为你的文件路径

# ----------------------------
# 2. 配置 text-embedding-v4（阿里云百炼）
# ----------------------------

embedding_client = OpenAI(
    api_key="",  # 替换为你的实际 Key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)



def safe_embed_text(text: str, client: OpenAI, model="text-embedding-v4", max_retries=3):
    """安全地 embedding 单条文本，自动重试"""
    for attempt in range(max_retries):
        try:
            # 清理文本
            clean_text = text.replace("\x00", "").replace("\ufffd", "").strip()
            if not clean_text:
                clean_text = " "

            
            response = client.embeddings.create(
                model=model,
                input=[clean_text]
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"  ⚠️ 尝试 {attempt+1} 失败: {str(e)[:100]}")
            if attempt < max_retries - 1:
                time.sleep(1)  # 稍等再试
            else:
                raise e

embeddings = []
failed_indices = []



for i, doc in enumerate(chunks):
    print(f"处理 chunk {i+1}/{len(chunks)}")
    try:
        emb = safe_embed_text(doc.page_content, embedding_client)
        embeddings.append(emb)
    except Exception as e:
        print(f"❌ chunk {i} 失败: {e}")
        failed_indices.append(i)
        # 可选：用零向量代替（不推荐），或跳过
        # embeddings.append([0.0] * 1536)

if failed_indices:
    print(f"\n⚠️ 共 {len(failed_indices)} 个 chunk 失败，索引: {failed_indices}")
    # 打印失败的文本内容（用于调试）
    for idx in failed_indices[:3]:  # 只打印前3个
        print(f"\n--- 失败 chunk {idx} 内容 ---")
        print(repr(chunks[idx].page_content[:200]))
else:
    print("✅ 所有 chunks embedding 成功！")

# 如果全部成功，手动构建 FAISS
if not failed_indices:
    from langchain_community.vectorstores.utils import DistanceStrategy
    vectorstore = FAISS.from_embeddings(
        text_embeddings=list(zip([doc.page_content for doc in chunks], embeddings)),
        embedding=embedding_client,  # 你的 OpenAIEmbeddings 实例
        metadatas=[doc.metadata for doc in chunks]
    )
    print("✅ FAISS 向量库构建完成！")


# ----------------------------
# 3. 构建 FAISS 向量库
# ----------------------------
# print("正在生成嵌入并构建 FAISS 向量库...")
# vectorstore = FAISS.from_documents(chunks, embedding_client)
# print("FAISS 向量库构建完成！")

# 可选：保存到本地，下次直接加载（避免重复嵌入）
vectorstore.save_local("faiss_index4")