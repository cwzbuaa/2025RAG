import json
import os
from datetime import datetime
from collections import defaultdict

# ========== 1. 加载 JSONL 文件 ==========
def load_jsonl(jsonl_path):
    """加载一个JSONL文件"""
    corpus = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            corpus.append(json.loads(line))
    print(f"✅ 加载 {os.path.basename(jsonl_path)}：{len(corpus)} 条记录")
    return corpus


# ========== 2. 分块统计类 ==========
class ChunkStatistics:
    def __init__(self):
        self.reset()

    def reset(self):
        self.total_chunks = 0
        self.chunk_lengths = []
        self.semantic_breaks = 0
        self.doc_chunk_counts = defaultdict(int)

    def add_chunk(self, doc_id, text):
        self.total_chunks += 1
        self.chunk_lengths.append(len(text))
        self.doc_chunk_counts[doc_id] += 1

        # 简易语义断裂检测（句末非标点）
        if text.strip() and text.strip()[-1] not in ['。', '！', '？', '.', '!', '?', '\n', '"']:
            self.semantic_breaks += 1

    def get_report(self, name):
        if not self.chunk_lengths:
            return f"⚠️ {name}: 无数据"

        avg_len = sum(self.chunk_lengths) / len(self.chunk_lengths)
        report = f"""
{'='*60}
📘 分块策略: {name}
{'='*60}
📊 基本统计:
  - 总分块数: {self.total_chunks}
  - 平均块长度: {avg_len:.1f} 字符
  - 最短块: {min(self.chunk_lengths)} 字符
  - 最长块: {max(self.chunk_lengths)} 字符
  - 原始文档数: {len(self.doc_chunk_counts)}
  - 平均每文档块数: {self.total_chunks / len(self.doc_chunk_counts):.2f}

⚠️ 语义完整性:
  - 疑似语义断裂: {self.semantic_breaks} 个 ({self.semantic_breaks/self.total_chunks*100:.1f}%)

📈 长度分布:
  - 0-256字符: {sum(1 for l in self.chunk_lengths if l <= 256)}
  - 257-512字符: {sum(1 for l in self.chunk_lengths if 256 < l <= 512)}
  - 513-768字符: {sum(1 for l in self.chunk_lengths if 512 < l <= 768)}
  - 769+字符: {sum(1 for l in self.chunk_lengths if l > 768)}
{'='*60}
"""
        return report


# ========== 3. 生成对比报告 ==========
def compare_chunking(length_file, parent_child_file, output_path):
    # 读取数据
    length_corpus = load_jsonl(length_file)
    parent_child_corpus = load_jsonl(parent_child_file)

    # 统计长度分块
    length_stats = ChunkStatistics()
    for doc in length_corpus:
        doc_id = doc.get("doc_id", "unknown")
        text = doc.get("content", "")
        length_stats.add_chunk(doc_id, text)

    # 统计父子分块
    parent_child_stats = ChunkStatistics()
    for doc in parent_child_corpus:
        doc_id = doc.get("doc_id", "unknown")
        text = doc.get("child_content", "")
        parent_child_stats.add_chunk(doc_id, text)

    # 汇总报告
    report_lines = [
        "=" * 80,
        "分块策略对比报告",
        f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 80,
        ""
    ]
    report_lines.append(length_stats.get_report("长度分块 (Length-based)"))
    report_lines.append(parent_child_stats.get_report("父子分块 (Parent-Child)"))

    # 汇总表格对比
    report_lines.append("\n" + "=" * 80)
    report_lines.append("📋 策略对比汇总")
    report_lines.append("=" * 80)
    report_lines.append("{:<20} {:<12} {:<15} {:<15}".format("策略", "总分块数", "平均块长度", "语义断裂率"))
    report_lines.append("-" * 80)
    for name, stats in [("长度分块", length_stats), ("父子分块", parent_child_stats)]:
        if stats.total_chunks > 0:
            avg_len = sum(stats.chunk_lengths) / len(stats.chunk_lengths)
            break_rate = stats.semantic_breaks / stats.total_chunks * 100
            report_lines.append("{:<20} {:<12} {:<15.1f} {:<15.1f}%".format(
                name, stats.total_chunks, avg_len, break_rate
            ))

    # 建议部分
    report_lines.append("\n\n💡 策略选择建议:")
    report_lines.append("-" * 80)
    report_lines.append("• 长度分块: 简单快速，适合结构均匀的技术文档。")
    report_lines.append("• 父子分块: 保留上下文层级，适合多层标题或复杂报告类文档。")
    report_lines.append("=" * 80)

    # 输出
    report_text = "\n".join(report_lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(f"\n📄 分块对比报告已生成: {output_path}\n")
    print(report_text)


# ========== 4. 主函数入口 ==========
if __name__ == "__main__":
    # 配置输入输出路径
    length_file = "chunked_corpus/howtocook/chunked_corpus_length.jsonl"        # 替换为长度分块结果路径
    parent_child_file = "chunked_corpus/howtocook/chunked_corpus.jsonl"  # 替换为父子分块结果路径
    output_report = "chunking_comparison_report.txt"

    compare_chunking(length_file, parent_child_file, output_report)
