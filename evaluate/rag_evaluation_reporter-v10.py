import os
import sys
import json
import time
from pathlib import Path
import pandas as pd
import traceback  # 用于详细错误跟踪
import nest_asyncio
nest_asyncio.apply()

# --- RAGAS评估相关组件 ---
from ragas import evaluate
from ragas.metrics import (  # pyright: ignore[reportMissingImports]
    context_recall,
    context_precision,
    faithfulness,
    answer_relevancy
)
from datasets import Dataset  # 用于解决 DataFrame 转换问题

# --- RAGAS LLM配置 ---
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import DashScopeEmbeddings

# --- 直接导入预构建的RAG系统 ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RETRIEVER_DIR = PROJECT_ROOT / "retriever-generator"
if str(RETRIEVER_DIR) not in sys.path:
    sys.path.append(str(RETRIEVER_DIR))
# 1. 获取当前文件的绝对路径 (A/a.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# 2. 获取上一级目录的绝对路径 (ProjectRoot)
project_root = os.path.abspath(os.path.join(current_dir, ".."))
# 3. 将 ProjectRoot 添加到 Python 的搜索路径
if project_root not in sys.path:
    sys.path.append(project_root)
# ===========================================
from agent_backend import load_agent_executor

# =============== 配置部分 ===============
# 统一API_KEY（与agent_backend.py保持一致）
API_KEY = "sk-20f1731cef9343c0978ad7774724d00f"  # 必须与agent_backend.py中的API_KEY一致
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 评估配置
TEST_DATA_PATH = "Evaluation Results Analysis/ragas_evaluation_questions_end_10.jsonl"
REPORT_DIR = "evaluation_results"
os.makedirs(REPORT_DIR, exist_ok=True)  

# 通用AI配置（与RAG系统使用相同的模型以保证公平比较）
GENERAL_MODEL = "qwen-flash"
GENERAL_TEMPERATURE = 0.1

# RAGAS评估专用配置
RAGAS_EVALUATION_MODEL = "qwen-turbo"  # 使用更强大的模型进行评估
RAGAS_TEMPERATURE = 0.1


# =============== 配置RAGAS使用的LLM ===============
def create_ragas_llm():

    # 创建LangChain兼容的LLM实例（通义千问）
    llm = ChatOpenAI(
        model_name=RAGAS_EVALUATION_MODEL,
        temperature=RAGAS_TEMPERATURE,
        api_key=API_KEY,
        base_url=BASE_URL
    )

    # 包装为RAGAS兼容的LLM
    return LangchainLLMWrapper(llm)


# =============== 数据加载函数 ===============

def load_test_questions(file_path: str) -> list:
    """加载测试问题集JSONL文件（每行一个JSON对象）"""
    questions = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():  # 跳过空行
                    data = json.loads(line.strip())
                    questions.append(data)
        print(f"✅ 成功加载 {len(questions)} 个测试问题")
        return questions
    except Exception as e:
        print(f"❌ 加载测试问题失败: {str(e)}")
        traceback.print_exc()
        raise


# =============== RAG系统评估函数 ===============

def run_rag_system(test_questions: list):

    print("\n🔄 正在加载预构建的RAG系统（来自agent_backend.py）...")

    try:
        # 直接调用agent_backend.py中的函数，创建完整的RAG系统
        # 这确保了评估使用的是与实际部署完全相同的系统
        # ====== 修复关键点：设置DashScope API Key环境变量 ======
        os.environ["DASHSCOPE_API_KEY"] = API_KEY  # 使用相同的API_KEY
        print(f"✅ 已设置DASHSCOPE_API_KEY环境变量 (前10位: {API_KEY[:10]}...)")  # 避免打印完整密钥
        # ====================================================

        from agent_backend import load_agent_executor  # 现在环境变量已设置
        print("✅ 正在加载RAG系统...")
        agent_executor, retriever, memory = load_agent_executor(
            enable_rerank=True,  # 启用重排功能
            rerank_model="qwen3-rerank",
            top_k=5,  # 先召回5个文档
            rerank_top_n=3  # 重排后返回3个最相关文档
        )
        print("✅ RAG系统加载成功！")
    except Exception as e:
        print(f"❌ 加载RAG系统失败: {str(e)}")
        traceback.print_exc()
        raise

    results = []
    total_time = 0
    failed_questions = 0

    print(f"\n🔍 开始RAG系统测试（共 {len(test_questions)} 个问题）...")

    for i, q in enumerate(test_questions, 1):
        question_text = q["Question_Text"]
        print(f"  [问题 {i}/{len(test_questions)}] {question_text[:50]}{'...' if len(question_text) > 50 else ''}")

        try:
            start_time = time.time()

            # 使用预构建的Agent执行器处理问题
            # 注意：AgentExecutor的输入是{"input": "问题文本"}
            result = agent_executor.invoke({"input": question_text})

            # 从Agent结果中提取最终答案
            answer = result.get("output", "")

            # 从 intermediate_steps 提取检索到的上下文（参考 app.py 的处理方式）
            context_list = []
            if "intermediate_steps" in result and result["intermediate_steps"]:
                for step in result["intermediate_steps"]:
                    if isinstance(step, tuple) and len(step) == 2:
                        action, observation = step
                        # LangChain AgentAction 常用属性为 .tool，而非 .name
                        if hasattr(action, "tool") and action.tool == "search_recipe_database":
                            if isinstance(observation, list):
                                for doc in observation:
                                    if hasattr(doc, "page_content"):
                                        context_list.append(doc.page_content)
                            elif hasattr(observation, "page_content"):
                                context_list.append(observation.page_content)
                            elif isinstance(observation, str):
                                context_list.append(observation)

            # 将上下文列表合并为字符串
            # 若未捕获到上下文，回退直接调用 retriever
            if not context_list:
                try:
                    fallback_docs = retriever.invoke(question_text)
                    if isinstance(fallback_docs, list):
                        context_list = [
                            getattr(d, "page_content", str(d)) for d in fallback_docs
                        ]
                    elif hasattr(fallback_docs, "page_content"):
                        context_list = [fallback_docs.page_content]
                    elif isinstance(fallback_docs, str):
                        context_list = [fallback_docs]
                except Exception:
                    pass
            context_str = "\n".join(context_list) if context_list else ""

            # 计算处理时间
            elapsed = time.time() - start_time
            total_time += elapsed

            # 保存结果
            results.append({
                "question": question_text,
                "answer": answer,
                "context_list": context_list,
                "context_str": context_str,
                "standard_answer": q["Ground_Truth"],
                "time": elapsed,
                "success": True
            })

        except Exception as e:
            print(f"    ❌ 处理问题失败: {str(e)}")
            traceback.print_exc()
            failed_questions += 1

            # 保存失败结果
            results.append({
                "question": question_text,
                "answer": f"处理失败: {str(e)}",
                "context_list": [],
                "context_str": "",
                "standard_answer": q["Ground_Truth"],
                "time": 0,
                "success": False
            })

    if failed_questions > 0:
        print(f"\n⚠️  警告: {failed_questions} 个问题处理失败，已记录错误信息")

    avg_time = total_time / (len(test_questions) - failed_questions) if (
                                                                                    len(test_questions) - failed_questions) > 0 else 0
    print(f"✅ RAG系统测试完成! 平均响应时间: {avg_time:.2f}秒")

    return results, total_time


# =============== 通用AI评估函数 ===============

def create_general_llm():
    """创建通用AI模型（与RAG系统使用相同的模型配置，确保公平比较）"""
    # 从langchain_openai导入ChatOpenAI
    from langchain_openai import ChatOpenAI

    # 使用与RAG系统相同的模型和参数
    return ChatOpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=GENERAL_MODEL,  # 与RAG系统相同的模型
        temperature=GENERAL_TEMPERATURE
    )


def run_general_ai(test_questions: list):
    """运行通用AI测试（无检索功能）"""
    print("\n🔄 初始化通用AI模型...")
    try:
        general_llm = create_general_llm()
        print("✅ 通用AI模型加载成功！")
    except Exception as e:
        print(f"❌ 加载通用AI模型失败: {str(e)}")
        traceback.print_exc()
        raise

    results = []
    total_time = 0
    failed_questions = 0
    print(f"\n🔍 开始通用AI测试（共 {len(test_questions)} 个问题）...")

    for i, q in enumerate(test_questions, 1):
        question_text = q["Question_Text"]
        print(f" [问题 {i}/{len(test_questions)}] {question_text[:50]}{'...' if len(question_text) > 50 else ''}")

        try:
            start_time = time.time()
            # ✅ 修改提示词，明确指令
            prompt = (
                "你是一个AI烹饪助手，名叫“航小厨”。你的任务是回答关于菜谱、食材和烹饪技巧的问题。\n"
                "重要规则：\n"
                "1. 如果问题是关于烹饪的，请基于你的专业知识回答。\n"
                "2. 如果问题与烹饪无关（如文学、历史、科技等），你必须回答："
                "\"我是一个AI烹饪助手航小厨，我的任务是帮您处理关于菜谱的问题。很抱歉，我无法回答烹饪之外的问题。\"\n\n"
                f"问题：{question_text}\n\n"
                "回答："
            )

            response = general_llm.invoke(prompt)
            answer = response.content if hasattr(response, 'content') else str(response)

            elapsed = time.time() - start_time
            total_time += elapsed

            results.append({
                "question": question_text,
                "answer": answer,
                "context_list": [],
                "context_str": "",
                "standard_answer": q["Ground_Truth"],
                "time": elapsed,
                "success": True
            })

        except Exception as e:
            print(f" ❌ 处理问题失败: {str(e)}")
            traceback.print_exc()
            failed_questions += 1
            results.append({
                "question": question_text,
                "answer": f"处理失败: {str(e)}",
                "context_list": [],
                "context_str": "",
                "standard_answer": q["Ground_Truth"],
                "time": 0,
                "success": False
            })

    if failed_questions > 0:
        print(f"\n⚠️ 警告: {failed_questions} 个问题处理失败，已记录错误信息")
    avg_time = total_time / (len(test_questions) - failed_questions) if (len(test_questions) - failed_questions) > 0 else 0
    print(f"✅ 通用AI测试完成! 平均响应时间: {avg_time:.2f}秒")
    return results, total_time


# =============== RAGAS指标计算函数 ===============
def calculate_ragas_metrics(results: list, is_rag: bool = True):
    """
    计算RAGAS评估指标
    参数:
        results: 评估结果列表
        is_rag: 是否为RAG系统（影响计算哪些指标）
    """
    print(f"\n📊 计算{'RAG' if is_rag else '通用AI'}系统RAGAS指标...")

    # 1. 创建RAGAS专用的LLM（关键修复：避免使用OpenAI）
    try:
        ragas_llm = create_ragas_llm()
        print(f"✅ RAGAS评估LLM配置成功! 模型: {RAGAS_EVALUATION_MODEL}")
    except Exception as e:
        print(f"❌ 创建RAGAS评估LLM失败: {str(e)}")
        traceback.print_exc()
        # 返回空指标
        empty_metrics = {
            "context_recall": None,
            "context_precision": None,
            "faithfulness": None,
            "answer_relevancy": None
        }
        return results, empty_metrics

        # 2. 准备数据（过滤掉失败的问题）
    valid_results = [r for r in results if r.get("success", True)]
    if len(valid_results) == 0:
        print("⚠️ 警告: 没有有效的结果可用于计算指标")
        empty_metrics = {
            "context_recall": None,
            "context_precision": None,
            "faithfulness": None,
            "answer_relevancy": None
        }
        return results, empty_metrics

    data = []
    for r in valid_results:
        # 准备上下文：RAGAS 要求为字符串列表，优先使用 context_list
        contexts = r.get("context_list") if is_rag else []
        if not isinstance(contexts, list):
            contexts = [str(contexts)] if contexts else []
        # 如果为空，用占位
        contexts = contexts if contexts else ["无上下文"]

        # 准备标准答案：优先使用 standard_answer
        ground_truth = r.get("standard_answer") or ""


        # 构建数据点
        data_point = {
            "question": r["question"],
            "answer": r["answer"],
            # RAGAS要求contexts是字符串列表
            "contexts": contexts,
            "ground_truth": ground_truth if ground_truth else "无标准答案"
        }
        data.append(data_point)

    try:
        # 3/4. 直接用 from_list 构建 Dataset，避免 DataFrame 破坏列表类型
        dataset = Dataset.from_list(data)

        # 5. 选择要计算的指标
        metrics_to_compute = []
        if is_rag:
            # RAG系统计算所有指标
            metrics_to_compute = [
                context_recall,
                context_precision,
                faithfulness,
                answer_relevancy
            ]
        else:
            # 通用AI只计算无上下文依赖的指标
            metrics_to_compute = [
                # faithfulness,
                answer_relevancy
            ]


        print(" 🔄 正在计算指标，请耐心等待...")
        #print(metrics_to_compute)

        # 7. 在调用 evaluate 之前，设置 RAGAS 所需的 OpenAI 兼容环境变量（用于其内部 OpenAIEmbeddings）
        #    RAGAS 会从环境变量读取密钥与 base_url
        os.environ.setdefault("OPENAI_API_KEY", API_KEY)
        os.environ.setdefault("OPENAI_BASE_URL", BASE_URL)
        # 兼容部分库读取 OPENAI_API_BASE
        os.environ.setdefault("OPENAI_API_BASE", BASE_URL)
        # 将默认嵌入模型切换为 DashScope 的 embeddings 模型，避免使用 text-embedding-ada-002
        os.environ.setdefault("OPENAI_EMBEDDING_MODEL", "text-embedding-v4")

        # 8. 显式使用 DashScope 的 embedding，避免 RAGAS 默认的 OpenAI ada-002
        dashscope_embeddings = DashScopeEmbeddings(
            model="text-embedding-v4",
            dashscope_api_key=API_KEY,
        )

        # 9. 调用 evaluate
        metrics = evaluate(
                dataset,
                metrics=metrics_to_compute,
                llm=ragas_llm,  # 注入自定义LLM
                embeddings=dashscope_embeddings,
                raise_exceptions=False  # 防止单个问题失败导致整个评估崩溃
            )

        summary_metrics = {}
        metrics_df = None
        metrics_series_map = {}

        try:
            if hasattr(metrics, "to_pandas"):
                metrics_df = metrics.to_pandas()
                excluded_cols = {"question", "answer", "ground_truth", "contexts"}
                for col in metrics_df.columns:
                    if col in excluded_cols:
                        continue
                    numeric_series = pd.to_numeric(metrics_df[col], errors="coerce")
                    if numeric_series.notna().any():
                        metrics_series_map[col] = numeric_series
                        summary_metrics[col] = float(numeric_series.mean())

            if not summary_metrics and hasattr(metrics, "overall") and isinstance(metrics.overall, dict):
                for name, val in metrics.overall.items():
                    try:
                        summary_metrics[name] = float(val)
                    except Exception:
                        summary_metrics[name] = None
        except Exception:
            summary_metrics = {}

        # 将每条样本的指标写入结果；若缺失则使用汇总
        for idx, r in enumerate(valid_results):
            sample_metrics = {}
            for name, series in metrics_series_map.items():
                value = series.iloc[idx] if idx < len(series) else None
                sample_metrics[name] = float(value) if pd.notna(value) else None
            if not sample_metrics:
                sample_metrics = dict(summary_metrics)
            r["metrics"] = sample_metrics

        print(f"✅ 指标计算成功! 样本数: {len(valid_results)}")
        return results, summary_metrics

    except Exception as e:
        print(f"❌ 计算RAGAS指标失败: {str(e)}")
        traceback.print_exc()
        # 返回失败的指标
        empty_metrics = {
            "context_recall": None,
            "context_precision": None,
            "faithfulness": None,
            "answer_relevancy": None
        }
        return results, empty_metrics


# =============== 报告生成函数 ===============

def generate_raw_report(rag_results, rag_summary, rag_total_time,
                        general_results, general_summary, general_total_time):
    """生成原始测试结果报告"""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(REPORT_DIR, f"evaluation_report_{timestamp}.json")

    # 计算性能指标
    rag_success_count = sum(1 for r in rag_results if r.get("success", True))
    rag_avg_time = rag_total_time / rag_success_count if rag_success_count > 0 else 0
    rag_throughput = rag_success_count / rag_total_time if rag_total_time > 0 else 0

    general_success_count = sum(1 for r in general_results if r.get("success", True))
    general_avg_time = general_total_time / general_success_count if general_success_count > 0 else 0
    general_throughput = general_success_count / general_total_time if general_total_time > 0 else 0

    # 构建报告结构
    report = {
        "metadata": {
            "timestamp": timestamp,
            "total_questions": len(rag_results),
            "successful_rag_questions": rag_success_count,
            "successful_general_questions": general_success_count,
            "evaluation_config": {
                "rag_system": "agent_backend.py (with reranking)",
                "general_ai_model": GENERAL_MODEL,
                "ragas_evaluation_model": RAGAS_EVALUATION_MODEL,
                "temperature": GENERAL_TEMPERATURE
            }
        },
        "rag_system": {
            "summary_metrics": {
                **rag_summary,
                "avg_response_time_seconds": rag_avg_time,
                "throughput_requests_per_second": rag_throughput,
                "success_rate": rag_success_count / len(rag_results) if len(rag_results) > 0 else 0
            },
            "detailed_results": rag_results
        },
        "general_ai": {
            "summary_metrics": {
                **general_summary,
                "avg_response_time_seconds": general_avg_time,
                "throughput_requests_per_second": general_throughput,
                "success_rate": general_success_count / len(general_results) if len(general_results) > 0 else 0
            },
            "detailed_results": general_results
        },
        "comparison": {
            "faithfulness_delta": (rag_summary.get("faithfulness", 0) or 0) - (
                        general_summary.get("faithfulness", 0) or 0),
            "answer_relevancy_delta": (rag_summary.get("answer_relevancy", 0) or 0) - (
                        general_summary.get("answer_relevancy", 0) or 0),
            "avg_time_delta": rag_avg_time - general_avg_time
        }
    }

    # 保存报告
    try:
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 评估报告已保存至: {report_file}")
        print(f"   - 文件大小: {os.path.getsize(report_file) / 1024:.2f} KB")
        return report_file
    except Exception as e:
        print(f"❌ 保存报告失败: {str(e)}")
        traceback.print_exc()
        return None


# =============== 主函数 ===============

def main():
    """主评估流程"""
    print("=" * 60)
    print("🍽️  RAG烹饪助手系统评估")
    print("=" * 60)

    # 1. 加载测试问题
    print("\n📥 步骤1: 加载测试问题集...")
    try:
        test_questions = load_test_questions(TEST_DATA_PATH)
    except Exception as e:
        print(f"致命错误: 无法加载测试数据 - {str(e)}")
        return

    # 2. 运行RAG系统测试
    print("\n" + "=" * 60)
    print("🔍 步骤2: 评估RAG系统 (带检索增强)")
    print("=" * 60)
    rag_results, rag_total_time = run_rag_system(test_questions)

    # 3. 运行通用AI测试
    print("\n" + "=" * 60)
    print("🔍 步骤3: 评估通用AI (无检索)")
    print("=" * 60)
    general_results, general_total_time = run_general_ai(test_questions)

    # 4. 计算评估指标
    print("\n" + "=" * 60)
    print("📊 步骤4: 计算评估指标")
    print("=" * 60)
    rag_results, rag_summary = calculate_ragas_metrics(rag_results, is_rag=True)
    general_results, general_summary = calculate_ragas_metrics(general_results, is_rag=False)

    # 5. 生成报告
    print("\n" + "=" * 60)
    print("💾 步骤5: 生成评估报告")
    print("=" * 60)
    report_path = generate_raw_report(
        rag_results, rag_summary, rag_total_time,
        general_results, general_summary, general_total_time
    )

    # 6. 打印摘要
    print("\n" + "=" * 60)
    print("🎯 评估摘要")
    print("=" * 60)

    if report_path:
        print(f"✅ 评估完成! 报告已保存至: {report_path}")

        # 打印关键指标
        print("\n📈 RAG系统关键指标:")
        print(f"   - 答案相关性: {rag_summary.get('answer_relevancy', 'N/A'):.4f}" if rag_summary.get(
            'answer_relevancy') is not None else "   - 答案相关性: N/A")
        print(f"   - 事实准确性: {rag_summary.get('faithfulness', 'N/A'):.4f}" if rag_summary.get(
            'faithfulness') is not None else "   - 事实准确性: N/A")
        print(f"   - 上下文召回率: {rag_summary.get('context_recall', 'N/A'):.4f}" if rag_summary.get(
            'context_recall') is not None else "   - 上下文召回率: N/A")
        print(f"   - 上下文精确率: {rag_summary.get('context_precision', 'N/A'):.4f}" if rag_summary.get(
            'context_precision') is not None else "   - 上下文精确率: N/A")
        print(
            f"   - 平均响应时间: {rag_total_time / len([r for r in rag_results if r.get('success', True)] or [1]):.2f}秒")

        print("\n📈 通用AI关键指标:")
        print(f"   - 答案相关性: {general_summary.get('answer_relevancy', 'N/A'):.4f}" if general_summary.get(
            'answer_relevancy') is not None else "   - 答案相关性: N/A")
        print(f"   - 事实准确性: {general_summary.get('faithfulness', 'N/A'):.4f}" if general_summary.get(
            'faithfulness') is not None else "   - 事实准确性: N/A")
        print(
            f"   - 平均响应时间: {general_total_time / len([r for r in general_results if r.get('success', True)] or [1]):.2f}秒")
    else:
        print("❌ 评估未完成，报告生成失败")

    print("\n" + "=" * 60)
    print("🎉 评估流程结束")
    print("=" * 60)


# =============== 程序入口 ===============

if __name__ == "__main__":
    main()

