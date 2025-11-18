import json
import pandas as pd
from langchain.llms import OpenAI  # 也可用开源模型如Qwen-7B
from dotenv import load_dotenv
import os

# 加载环境变量（用OpenAI需填APIKey，开源模型可跳过）
load_dotenv()
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-instruct")

def generate_qa_from_chunk(chunked_jsonl_path, save_qa_excel):
    """
    从分块语料生成QA对（先批量生成，再人工筛选）
    :param chunked_jsonl_path: 分块后的语料路径
    :param save_qa_excel: QA对输出Excel路径
    """
    qa_list = []
    with open(chunked_jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            chunk = json.loads(line)
            content = chunk["content"]
            doc_title = chunk["metadata"]["title"]
            
            # 用LLM生成QA对（提示词可根据领域调整）
            prompt = f"""
            基于以下关于「{doc_title}」的内容，生成1个问题和对应的标准答案：
            内容：{content}
            要求：1. 问题要覆盖内容的核心知识点；2. 答案要准确、简洁，不超过300字；3. 用中文生成。
            输出格式：问题：xxx\n答案：xxx
            """
            try:
                response = llm(prompt, max_tokens=500)
                # 解析LLM输出（提取问题和答案）
                if "问题：" in response and "答案：" in response:
                    q = response.split("问题：")[1].split("答案：")[0].strip()
                    a = response.split("答案：")[1].strip()
                    qa_list.append({
                        "doc_id": chunk["doc_id"],
                        "chunk_id": chunk.get("chunk_id", chunk.get("child_chunk_id")),
                        "问题": q,
                        "标准答案": a,
                        "答案来源": doc_title
                    })
            except Exception as e:
                print(f"生成QA失败（chunk_id: {chunk.get('chunk_id')}）：{e}")
    
    # 保存为Excel（方便人工筛选和修改）
    df = pd.DataFrame(qa_list)
    df.to_excel(save_qa_excel, index=False, engine="openpyxl")
    print(f"QA对生成完成，共{len(qa_list)}条，保存路径：{save_qa_excel}")
    print("提示：请打开Excel人工筛选无效QA（如问题重复、答案错误），最终保留100-200条用于测评。")

# 生成测评数据集（用语义分块的语料，语义完整度高）
generate_qa_from_chunk("chunked_corpus_semantic.jsonl", "rag_test_qa.xlsx")