from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,  # 长度分块
    SentenceTransformersTokenTextSplitter  # 语义分块
)
import json
import os
from datetime import datetime
from collections import defaultdict

# 1. 加载原始JSONL语料
def load_corpus(jsonl_path):
    """加载单个JSONL文件"""
    corpus = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            corpus.append(json.loads(line))
    return corpus

# 2. 批量加载文件夹下所有JSONL文件
def load_all_corpus(corpus_dir):
    """
    批量加载文件夹下的所有JSONL文件
    :param corpus_dir: JSONL文件所在目录
    :return: 所有文档的列表
    """
    all_corpus = []
    jsonl_files = [f for f in os.listdir(corpus_dir) if f.endswith('.jsonl')]
    
    print(f"📂 发现 {len(jsonl_files)} 个JSONL文件:")
    for jsonl_file in jsonl_files:
        file_path = os.path.join(corpus_dir, jsonl_file)
        corpus = load_corpus(file_path)
        all_corpus.extend(corpus)
        print(f"  ✓ {jsonl_file}: {len(corpus)} 个文档")
    
    print(f"\n📊 总计加载: {len(all_corpus)} 个文档\n")
    return all_corpus

# 3. 分块统计类
class ChunkStatistics:
    """分块统计分析器"""
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.total_chunks = 0
        self.chunk_lengths = []
        self.doc_chunk_counts = defaultdict(int)
        self.semantic_breaks = 0  # 语义断裂次数（简单检测：块结尾不是句号/问号/感叹号）
    
    def add_chunk(self, doc_id, chunk_content):
        """添加一个分块的统计信息"""
        self.total_chunks += 1
        self.chunk_lengths.append(len(chunk_content))
        self.doc_chunk_counts[doc_id] += 1
        
        # 检测语义断裂（简单规则：块结尾不是完整句子）
        if chunk_content.strip() and chunk_content.strip()[-1] not in ['。', '！', '？', '.', '!', '?', '\n']:
            self.semantic_breaks += 1
    
    def get_report(self, strategy_name):
        """生成统计报告"""
        if not self.chunk_lengths:
            return "无分块数据"
        
        avg_length = sum(self.chunk_lengths) / len(self.chunk_lengths)
        min_length = min(self.chunk_lengths)
        max_length = max(self.chunk_lengths)
        
        report = f"""
{'='*60}
分块策略: {strategy_name}
{'='*60}
📊 基本统计:
  - 总分块数: {self.total_chunks}
  - 平均块长度: {avg_length:.0f} 字符
  - 最短块: {min_length} 字符
  - 最长块: {max_length} 字符
  - 原始文档数: {len(self.doc_chunk_counts)}
  - 平均每文档分块数: {self.total_chunks / len(self.doc_chunk_counts):.1f}

⚠️  质量指标:
  - 疑似语义断裂: {self.semantic_breaks} 个 ({self.semantic_breaks/self.total_chunks*100:.1f}%)
  
📈 长度分布:
  - 0-256字符: {sum(1 for l in self.chunk_lengths if l <= 256)} 个
  - 257-512字符: {sum(1 for l in self.chunk_lengths if 256 < l <= 512)} 个
  - 513-768字符: {sum(1 for l in self.chunk_lengths if 512 < l <= 768)} 个
  - 769+字符: {sum(1 for l in self.chunk_lengths if l > 768)} 个
{'='*60}
"""
        return report

# 4. 实现3种分块策略（带统计）
def chunk_corpus(corpus, chunk_strategy, save_chunked_jsonl):
    """
    对语料进行分块
    :param corpus: 加载后的原始语料（list of dict）
    :param chunk_strategy: 分块策略（"length"/"semantic"/"parent_child"）
    :param save_chunked_jsonl: 分块后JSONL保存路径
    :return: 统计对象
    """
    stats = ChunkStatistics()
    
    # 初始化分块器
    if chunk_strategy == "length":
        # 长度分块：每512个字符一块，重叠50字符（避免断句）
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,
            chunk_overlap=50,
            length_function=len,
            separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""]
        )
    elif chunk_strategy == "semantic":
        # 语义分块：用多语言Sentence-BERT模型（支持中文）
        text_splitter = SentenceTransformersTokenTextSplitter(
            chunk_size=512,
            chunk_overlap=50,
            model_name="paraphrase-multilingual-MiniLM-L12-v2"  # 多语言模型，支持中文
        )
    elif chunk_strategy == "parent_child":
        # 父子分块：先按1024字符分父块，再按256字符分子块
        parent_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1024, 
            chunk_overlap=100,
            separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""]
        )
        child_splitter = RecursiveCharacterTextSplitter(
            chunk_size=256, 
            chunk_overlap=20,
            separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""]
        )
    
    # 执行分块并保存
    print(f"🔄 开始 {chunk_strategy} 分块...")
    with open(save_chunked_jsonl, "w", encoding="utf-8") as f:
        for doc in corpus:
            if chunk_strategy != "parent_child":
                # 长度/语义分块：直接分
                chunks = text_splitter.split_text(doc["content"])
                for i, chunk in enumerate(chunks):
                    chunk_obj = {
                        "doc_id": doc["doc_id"],
                        "chunk_id": f"{doc['doc_id']}_chunk{i+1}",
                        "content": chunk,
                        "metadata": doc["metadata"],
                        "chunk_strategy": chunk_strategy
                    }
                    f.write(json.dumps(chunk_obj, ensure_ascii=False) + "\n")
                    stats.add_chunk(doc["doc_id"], chunk)
            else:
                # 父子分块：先分父块，再分子块
                parent_chunks = parent_splitter.split_text(doc["content"])
                for p_idx, parent_chunk in enumerate(parent_chunks):
                    child_chunks = child_splitter.split_text(parent_chunk)
                    for c_idx, child_chunk in enumerate(child_chunks):
                        chunk_obj = {
                            "doc_id": doc["doc_id"],
                            "parent_chunk_id": f"{doc['doc_id']}_parent{p_idx+1}",
                            "child_chunk_id": f"{doc['doc_id']}_parent{p_idx+1}_child{c_idx+1}",
                            "content": child_chunk,
                            "parent_content": parent_chunk,  # 保留父块内容，用于层级关联
                            "metadata": doc["metadata"],
                            "length": len(child_chunk),
                            "chunk_strategy": chunk_strategy
                        }
                        f.write(json.dumps(chunk_obj, ensure_ascii=False) + "\n")
                        stats.add_chunk(doc["doc_id"], child_chunk)
    
    print(f"✅ {chunk_strategy} 分块完成，保存路径：{save_chunked_jsonl}")
    return stats

# 5. 生成对比报告
def generate_comparison_report(all_stats, output_path):
    """
    生成3种策略的对比报告
    :param all_stats: 字典，key为策略名，value为统计对象
    :param output_path: 报告保存路径
    """
    report_lines = [
        "=" * 80,
        "分块策略对比报告",
        f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 80,
        ""
    ]
    
    # 添加每个策略的详细报告
    for strategy, stats in all_stats.items():
        report_lines.append(stats.get_report(strategy))
    
    # 添加对比总结
    report_lines.append("\n" + "=" * 80)
    report_lines.append("📋 策略对比总结")
    report_lines.append("=" * 80)
    
    comparison_table = "\n{:<20} {:<15} {:<15} {:<15}".format(
        "策略", "总分块数", "平均块长度", "语义断裂率"
    )
    comparison_table += "\n" + "-" * 80
    
    for strategy, stats in all_stats.items():
        if stats.chunk_lengths:
            avg_len = sum(stats.chunk_lengths) / len(stats.chunk_lengths)
            break_rate = stats.semantic_breaks / stats.total_chunks * 100
            comparison_table += "\n{:<20} {:<15} {:<15.0f} {:<15.1f}%".format(
                strategy, stats.total_chunks, avg_len, break_rate
            )
    
    report_lines.append(comparison_table)
    
    # 添加建议
    report_lines.append("\n\n💡 策略选择建议:")
    report_lines.append("-" * 80)
    report_lines.append("• length (长度分块): 适合结构简单的文档，速度快，但可能断句")
    report_lines.append("• semantic (语义分块): 适合保持语义完整性，但计算成本高")
    report_lines.append("• parent_child (父子分块): 适合有层级结构的文档，保留上下文关系")
    report_lines.append("=" * 80)
    
    # 保存报告
    report_content = "\n".join(report_lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print(f"\n📄 对比报告已保存: {output_path}")
    print(report_content)

# ============ 主程序 ============
if __name__ == "__main__":
    # 配置参数
    CORPUS_DIR = "jsonl_corpus/howtocook"  # JSONL文件所在目录
    OUTPUT_DIR = "chunked_corpus/howtocook"  # 分块结果输出目录
    
    # 创建输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("=" * 80)
    print("🚀 开始分块处理")
    print("=" * 80)
    
    # 1. 批量加载所有JSONL文件
    corpus = load_all_corpus(CORPUS_DIR)
    
    if not corpus:
        print("❌ 错误：未找到任何文档！")
        exit(1)
    
    # 2. 批量执行3种分块策略
    strategies = ["length", "semantic", "parent_child"]
    all_stats = {}
    
    for strategy in strategies:
        save_path = os.path.join(OUTPUT_DIR, f"chunked_corpus_{strategy}.jsonl")
        stats = chunk_corpus(corpus, strategy, save_path)
        all_stats[strategy] = stats
        print()  # 空行分隔
    
    # 3. 生成对比报告
    report_path = os.path.join(OUTPUT_DIR, "chunking_report.txt")
    generate_comparison_report(all_stats, report_path)
    
    print("\n✨ 所有分块任务完成！")
    print(f"📁 输出目录: {OUTPUT_DIR}")
    print(f"📄 对比报告: {report_path}")