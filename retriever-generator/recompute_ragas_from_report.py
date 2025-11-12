import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Tuple

import nest_asyncio
nest_asyncio.apply()

import pandas as pd
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    context_precision,
    context_recall,
    faithfulness,
    answer_relevancy,
)
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import DashScopeEmbeddings


DEFAULT_API_KEY = os.getenv("DASHSCOPE_API_KEY") or ""
DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
DEFAULT_LLM_MODEL = "qwen-turbo"
DEFAULT_TEMPERATURE = 0.1
DEFAULT_EMBEDDING_MODEL = "text-embedding-v4"


def create_llm(api_key: str, base_url: str, model: str, temperature: float):
    return ChatOpenAI(
        api_key=api_key,
        base_url=base_url,
        model_name=model,
        temperature=temperature,
    )


def create_embeddings(api_key: str, model: str):
    return DashScopeEmbeddings(
        model=model,
        dashscope_api_key=api_key,
    )


def prepare_dataset(results: List[Dict[str, Any]], is_rag: bool) -> Tuple[Dataset, List[Dict[str, Any]]]:
    rows: List[Dict[str, Any]] = []
    valid_entries: List[Dict[str, Any]] = []

    for entry in results:
        if not entry.get("success", True):
            continue

        question = str(entry.get("question", ""))
        answer = str(entry.get("answer", ""))
        ground_truth = str(entry.get("standard_answer") or entry.get("ground_truth") or "无标准答案")

        contexts = entry.get("context_list") if is_rag else []
        if not isinstance(contexts, list):
            contexts = [str(contexts)] if contexts else []
        # 确保 contexts 是字符串列表
        contexts = [str(c) for c in contexts] if contexts else []
        if not contexts:
            contexts = ["无上下文"]

        rows.append(
            {
                "question": question,      # 字符串
                "answer": answer,          # 字符串
                "contexts": contexts,      # 字符串列表
                "ground_truth": ground_truth,  # 字符串
            }
        )
        valid_entries.append(entry)

    if not rows:
        return Dataset.from_list([]), []

    dataset = Dataset.from_list(rows)
    return dataset, valid_entries


def run_ragas_evaluation(
    dataset: Dataset,
    metrics_to_compute: List[Any],
    llm,
    embeddings,
) -> Tuple[Dict[str, float], List[Dict[str, float]]]:
    if len(dataset) == 0:
        return {}, []

    result = evaluate(
        dataset,
        metrics=metrics_to_compute,
        llm=llm,
        embeddings=embeddings,
        raise_exceptions=False,
    )

    summary_metrics: Dict[str, float] = {}
    per_sample_metrics: List[Dict[str, float]] = [{} for _ in range(len(dataset))]

    try:
        if hasattr(result, "to_pandas"):
            df = result.to_pandas()
            excluded_cols = {"question", "answer", "ground_truth", "contexts"}
            for col in df.columns:
                if col in excluded_cols:
                    continue
                numeric_series = pd.to_numeric(df[col], errors="coerce")
                if numeric_series.notna().any():
                    summary_metrics[col] = float(numeric_series.mean())
                    for idx, value in enumerate(numeric_series.tolist()):
                        per_sample_metrics[idx][col] = float(value) if pd.notna(value) else None

        if not summary_metrics and hasattr(result, "overall") and isinstance(result.overall, dict):
            for name, value in result.overall.items():
                try:
                    summary_metrics[name] = float(value)
                except Exception:
                    summary_metrics[name] = None
            # 当 overall 构建时，也同步到 per-sample（全部相同数值）
            for metrics_dict in per_sample_metrics:
                metrics_dict.update(summary_metrics)

    except Exception as exc:  # noqa: BLE001
        print(f"⚠️ 处理 RAGAS 结果时出现异常: {exc}")
        summary_metrics = {}

    return summary_metrics, per_sample_metrics


def update_report(
    report: Dict[str, Any],
    system_key: str,
    summary_metrics: Dict[str, float],
    per_sample_metrics: List[Dict[str, float]],
    valid_entries: List[Dict[str, Any]],
):
    if system_key not in report:
        return

    system_block = report[system_key]
    detailed = system_block.get("detailed_results", [])

    # 写入 summary 指标
    existing_summary = system_block.get("summary_metrics", {})
    existing_summary.update(summary_metrics)
    system_block["summary_metrics"] = existing_summary

    # 写入每条样本的指标
    for entry in detailed:
        entry["metrics"] = entry.get("metrics") or {}

    for metrics_dict, entry in zip(per_sample_metrics, valid_entries):
        entry["metrics"] = metrics_dict


def main():
    parser = argparse.ArgumentParser(description="重新计算 evaluation_report.json 中的 RAGAS 指标")
    parser.add_argument(
        "--report",
        type=str,
        default=None,
        help="evaluation_report JSON 文件路径；若不提供，将自动选择 evaluation_results 目录下最新的 evaluation_report_*.json",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="可选，输出覆盖路径；未提供则就地覆盖原文件",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=DEFAULT_API_KEY,
        help="DashScope API Key",
    )
    parser.add_argument(
        "--base-url",
        type=str,
        default=DEFAULT_BASE_URL,
        help="DashScope 基础 URL",
    )
    parser.add_argument(
        "--llm-model",
        type=str,
        default=DEFAULT_LLM_MODEL,
        help="RAGAS 评估使用的 LLM 模型",
    )
    parser.add_argument(
        "--embedding-model",
        type=str,
        default=DEFAULT_EMBEDDING_MODEL,
        help="RAGAS 评估使用的嵌入模型",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=DEFAULT_TEMPERATURE,
        help="LLM 温度",
    )
    args = parser.parse_args()

    if args.report is None:
        default_dir = Path("evaluation_results")
        candidates = sorted(
            default_dir.glob("evaluation_report_*.json"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        if not candidates:
            raise FileNotFoundError(
                "未指定 --report，且在 evaluation_results/ 目录中找不到 evaluation_report_*.json"
            )
        report_path = candidates[0]
        print(f"🔍 未指定 --report，自动选择最新报告: {report_path}")
    else:
        report_path = Path(args.report)
        if not report_path.exists():
            raise FileNotFoundError(f"找不到报告文件: {report_path}")

    with open(report_path, "r", encoding="utf-8") as f:
        report = json.load(f)

    llm = create_llm(args.api_key, args.base_url, args.llm_model, args.temperature)
    embeddings = create_embeddings(args.api_key, args.embedding_model)

    # RAG 系统
    rag_results = report.get("rag_system", {}).get("detailed_results", [])
    rag_dataset, rag_valid_entries = prepare_dataset(rag_results, is_rag=True)
    rag_metrics_to_compute = [context_recall, context_precision, faithfulness, answer_relevancy]

    rag_summary, rag_sample_metrics = run_ragas_evaluation(
        rag_dataset,
        rag_metrics_to_compute,
        llm,
        embeddings,
    )
    update_report(report, "rag_system", rag_summary, rag_sample_metrics, rag_valid_entries)

    # 通用 AI 系统
    general_results = report.get("general_ai", {}).get("detailed_results", [])
    general_dataset, general_valid_entries = prepare_dataset(general_results, is_rag=False)
    # 注意：faithfulness 需要 contexts，没有 RAG 时无法计算
    general_metrics_to_compute = [answer_relevancy]

    general_summary, general_sample_metrics = run_ragas_evaluation(
        general_dataset,
        general_metrics_to_compute,
        llm,
        embeddings,
    )
    update_report(report, "general_ai", general_summary, general_sample_metrics, general_valid_entries)

    output_path = Path(args.output) if args.output else report_path
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"✅ RAGAS 指标已重新计算并保存至: {output_path}")
    if rag_summary:
        print("📊 RAG 系统摘要指标:")
        for k, v in rag_summary.items():
            print(f"  - {k}: {v}")
    if general_summary:
        print("📊 通用 AI 摘要指标:")
        for k, v in general_summary.items():
            print(f"  - {k}: {v}")


if __name__ == "__main__":
    main()

