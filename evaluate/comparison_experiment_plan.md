# DeepCook 对比实验实施计划

## 背景

用户已完成以下工作：
- SFT 微调了 Qwen2.5-7B 模型（`output/sft_lora/checkpoint-171`）
- 在云端训练了 BERT 检索器
- 有 100 道测评问题（10 类）

用户想对比 **5 个方案**，全面评估 SFT 和 RAG 的效果差异。

---

## 对比方案

| # | 方案 | 描述 |
|---|------|------|
| 1 | **SFT Only** | 仅用 SFT 微调后的 Qwen 直接回答，不使用检索 |
| 2 | **BERT-RAG + 通用Qwen** | 通用 Qwen（未微调）+ BERT 检索 |
| 3 | **BERT-RAG + SFT Qwen** | SFT 微调 Qwen + BERT 检索 |
| 4 | **Qwen-Embedding RAG** | 通用 Qwen + Qwen Embedding 检索 |
| 5 | **通用 Qwen** | 无检索 + 无 SFT 的 baseline |

---

## 评估指标

### 1. 生成质量指标（RAGAS）
- `faithfulness` - 答案事实准确性
- `answer_relevancy` - 答案与问题相关性
- `context_recall` - 上下文召回率（RAG 方案）
- `context_precision` - 上下文精确率（RAG 方案）

### 2. 检索质量指标
- **Hit Rate @K** - Top-K 检索结果中命中的比例
- **MRR** - 平均倒数排名
- 分类别计算（10 类问题分别统计）

### 3. 性能指标
- 平均响应时间
- 吞吐量（QPS）
- 成功率

### 4. 特殊场景指标
- **拒答率** - 边界问题（类型10）正确拒绝的比例
- **幻觉率** - 菜谱胡编的比例（需人工评估）

---

## 实现步骤

### 阶段 1：准备环境（需用户确认）

1. **确认检索器模型**
   - 用户需要将云端的 BERT 检索器模型下载到本地
   - 模型路径：`output/retriever/retriever_model.pt`
   - 或在脚本中配置云端模型访问方式

2. **确认 FAISS 索引**
   - 需要构建 FAISS 索引或确认索引位置
   - 索引路径：`index/retriever/`

3. **确认 API 配置**
   - DashScope API Key（用于 Qwen 模型调用）

### 阶段 2：编写对比实验脚本

创建 `evaluate/comparison_experiment.py`，包含：

```python
# 5 个系统的加载和调用函数
def load_sft_model(): ...       # 方案1
def load_general_qwen(): ...    # 方案5
def load_bert_retriever(): ...  # 方案2、3
def load_qwen_embedding(): ...  # 方案4

def run_sft_only(questions): ...           # 方案1
def run_bert_rag_general(questions): ...   # 方案2
def run_bert_rag_sft(questions): ...       # 方案3
def run_qwen_emb_rag(questions): ...       # 方案4
def run_general_qwen(questions): ...       # 方案5
```

### 阶段 3：统一评估模块

复用现有的 RAGAS 评估逻辑（参考 `evaluate/rag_evaluation_reporter-v10.py`），计算各方案的：
- RAGAS 指标
- 检索指标（Hit Rate、MRR）
- 性能指标

### 阶段 4：运行实验

```bash
python evaluate/comparison_experiment.py
```

### 阶段 5：生成报告

生成 `evaluation_results/comparison_report_*.json`，包含：
- 各方案指标对比表
- 分类别分析
- 性能对比

---

## 关键文件

| 文件 | 作用 |
|------|------|
| `output/sft_lora/` | SFT 微调模型 |
| `scripts/retriever/retrieve.py` | 检索器调用方式参考 |
| `evaluate/ragas_evaluation_questions_end.jsonl` | 100 道测试问题 |
| `evaluate/rag_evaluation_reporter-v10.py` | 现有评估逻辑参考 |
| `evaluate/comparison_experiment.py` | **新建**：对比实验主脚本 |

---

## 验证方式

1. 运行脚本后，检查生成的报告文件
2. 确认 5 个方案都能正常输出答案
3. 检查 RAGAS 指标是否合理计算

---

## 待确认

1. **BERT 检索器模型**：用户需要提供模型路径或下载方式
2. **FAISS 索引**：是否已构建？位置在哪里？
3. **Qwen Embedding**：使用 DashScope API（text-embedding-v4）

---

## 行动计划（本地 → 云端）

由于检索器和索引在云端，需要分两步：

### 步骤 1：本地生成计划文档（本文档）
- 本地分析现有代码结构
- 生成详细的实施计划

### 步骤 2：云端执行（用户主导）
- 用户将计划发给云端的 Claude Code
- 云端完成检索器模型和 FAISS 索引的本地化

### 步骤 3：本地运行对比实验
- 云端完成后，本地运行实验脚本

---

## 云端任务清单（供 Claude Code 阅读）

### 1. 下载/准备 BERT 检索器模型

需要确认以下文件存在：
- 检索器模型权重：`output/retriever/retriever_model.pt`
- 训练脚本参考：`scripts/retriever/train_retriever.py`

检索器模型结构（参考 `retrieve.py`）：
```python
# 需要加载的内容
state_dict = torch.load(model_path, map_location=device)
# 包含: bert模型权重, projection权重
```

### 2. 构建 FAISS 索引

如果索引不存在，需要运行：
```bash
python scripts/retriever/build_faiss_index.py
```

输出目录：`index/retriever/`，需要包含：
- `faiss_index.bin` - FAISS 索引文件
- `metadata.json` - 文档元数据
- `index_config.json` - 配置信息

### 3. 导出必要文件到本地

需要下载到本地的文件：
```
output/retriever/retriever_model.pt  # 检索器模型
index/retriever/                    # FAISS 索引目录
```

### 4. 确认 Qwen Embedding 可用

使用 DashScope API：
- 模型：`text-embedding-v4`
- API：通义千问的 embedding 接口
- API Key 与通用千问一致（`sk-20f1...`）

---

## 实现细节

### 方案1：SFT Only

```python
def run_sft_only(questions):
    """仅用 SFT 微调后的 Qwen 直接回答"""
    # 加载 SFT 模型
    model = AutoModelForCausalLM.from_pretrained("output/sft_lora")
    tokenizer = AutoTokenizer.from_pretrained("output/sft_lora")

    for q in questions:
        # 直接推理，不使用检索
        inputs = tokenizer(f"### 指令:\n{q}\n\n### 回答:", return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=1024)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### 方案2：BERT-RAG + 通用Qwen

```python
def run_bert_rag_general(questions):
    """通用 Qwen + BERT 检索"""
    # 使用通用 Qwen (qwen-flash)
    llm = ChatOpenAI(model="qwen-flash", api_key=API_KEY)

    # 使用 BERT 检索器
    retriever = Retriever("index/retriever")

    for q in questions:
        # 检索上下文
        docs = retriever.retrieve(q, top_k=3)
        context = "\n".join([d["doc_preview"] for d in docs])

        # 构建 prompt
        prompt = f"基于以下菜谱信息回答问题。\n\n{context}\n\n问题：{q}"

        # 生成回答
        answer = llm.invoke(prompt)
```

### 方案3：BERT-RAG + SFT Qwen

```python
def run_bert_rag_sft(questions):
    """SFT Qwen + BERT 检索"""
    # 使用 SFT 后的 Qwen
    model = AutoModelForCausalLM.from_pretrained("output/sft_lora")
    tokenizer = AutoTokenizer.from_pretrained("output/sft_lora")

    # 使用 BERT 检索器
    retriever = Retriever("index/retriever")

    for q in questions:
        # 检索上下文
        docs = retriever.retrieve(q, top_k=3)
        context = "\n".join([d["doc_preview"] for d in docs])

        # 构建 prompt（参考 SFT 训练格式）
        prompt = f"### 指令:\n基于以下菜谱信息回答：{context}\n\n问题：{q}\n\n### 回答:"

        # 生成回答
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=1024)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### 方案4：Qwen-Embedding RAG

```python
def run_qwen_emb_rag(questions):
    """通用 Qwen + Qwen Embedding 检索"""
    # 使用通用 Qwen
    llm = ChatOpenAI(model="qwen-flash", api_key=API_KEY)

    # 使用 Qwen Embedding
    embeddings = DashScopeEmbeddings(
        model="text-embedding-v4",
        dashscope_api_key=API_KEY
    )

    # 使用 FAISS 索引（用 Qwen Embedding 构建）
    index = faiss.read_index("index/retriever/faiss_index_qwen.bin")
    # 检索时使用 Qwen Embedding
    query_vec = embeddings.embed_query(q)
    distances, indices = index.search(np.array([query_vec]), top_k=3)

    # 后续与方案2相同
```

### 方案5：通用 Qwen

```python
def run_general_qwen(questions):
    """无检索 + 无 SFT 的 baseline"""
    # 使用通用 Qwen (qwen-flash)
    llm = ChatOpenAI(model="qwen-flash", api_key=API_KEY)

    for q in questions:
        prompt = f"你是一个AI烹饪助手。\n\n问题：{q}\n\n回答："
        answer = llm.invoke(prompt)
```

---

## 评估结果结构

```json
{
  "metadata": {
    "timestamp": "20260318_143000",
    "total_questions": 100,
    "question_types": 10
  },
  "results": {
    "sft_only": {
      "metrics": {
        "faithfulness": 0.75,
        "answer_relevancy": 0.82,
        "avg_response_time": 2.3,
        "success_rate": 0.98
      },
      "per_type": {...}
    },
    "bert_rag_general": {
      "metrics": {
        "faithfulness": 0.88,
        "answer_relevancy": 0.91,
        "context_recall": 0.85,
        "context_precision": 0.89,
        "hit_rate@3": 0.92,
        "mrr": 0.87,
        "avg_response_time": 3.1,
        "success_rate": 0.99
      },
      "per_type": {...}
    },
    "bert_rag_sft": {...},
    "qwen_emb_rag": {...},
    "general_qwen": {...}
  },
  "comparison": {
    "best_ragas": "bert_rag_sft",
    "best_retrieval": "bert_rag_sft",
    "best_performance": "general_qwen",
    "summary_table": "..."
  }
}
```
