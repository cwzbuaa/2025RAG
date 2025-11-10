# 航小厨 - 基于 LangChain 的智能 RAG 烹饪助手

一个基于 LangChain 开发的智能检索增强生成（RAG）系统，专门用于烹饪领域的问答助手。系统集成了向量检索、重排模型和智能 Agent，能够基于菜谱数据库提供专业的烹饪建议。

## 📋 目录

- [项目介绍](#项目介绍)
- [功能特性](#功能特性)
- [技术栈](#技术栈)
- [安装步骤](#安装步骤)
- [配置说明](#配置说明)
- [使用方法](#使用方法)
- [项目结构](#项目结构)
- [性能监控](#性能监控)
- [常见问题](#常见问题)

## 🎯 项目介绍

航小厨是一个智能烹饪助手，采用 RAG（Retrieval-Augmented Generation）架构，结合了：

- **向量检索**：使用 FAISS 向量数据库进行快速相似度搜索
- **重排模型**：可选的重排功能，提升检索结果的相关性
- **智能 Agent**：基于 LangChain 的 Agent 框架，支持工具调用和记忆功能
- **交互界面**：基于 Streamlit 的友好 Web 界面

系统能够回答各种烹饪相关问题，包括：
- 具体菜谱做法
- 根据已有食材推荐菜谱
- 烹饪技巧和概念解释
- 菜谱推荐和修改建议

> **数据来源**：本项目的数据源自 GitHub 项目 [HowToCook](https://github.com/Anduin2017/HowToCook)，一个优秀的程序员在家做饭方法指南。

## ✨ 功能特性

### 核心功能

1. **智能检索**
   - 支持向量相似度检索
   - 可选的重排功能，提升检索精度
   - 可配置的召回数量（Top K）和重排后返回数量（Top N）

2. **智能 Agent**
   - 基于 LangChain 的 Tools Agent
   - 自动工具调用和决策
   - 支持对话记忆功能

3. **交互界面**
   - 友好的 Streamlit Web 界面
   - 实时性能监控
   - 可配置的检索参数
   - 新对话功能

4. **性能监控**
   - 检索时间统计
   - 生成时间统计
   - 总延迟监控
   - 吞吐量计算

### 高级特性

- ✅ **可选重排**：支持启用/禁用重排功能
- ✅ **参数可配置**：重排模型、Top K、Top N 等参数可在界面中调整
- ✅ **对话记忆**：支持多轮对话，保持上下文
- ✅ **性能报告**：详细的性能指标展示

## 🛠 技术栈

- **框架**：LangChain 0.3.x
- **向量数据库**：FAISS
- **嵌入模型**：DashScope text-embedding-v4
- **重排模型**：DashScope qwen3-rerank / qwen-rerank
- **LLM**：DashScope qwen-flash
- **Web 框架**：Streamlit
- **Python**：3.x

## 📦 安装步骤

### 1. 克隆项目

```bash
git clone <repository-url>
cd 2025RAG
```

### 2. 创建虚拟环境（推荐）

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

如果遇到依赖冲突，可以运行修复脚本：

```bash
bash fix_dependencies.sh
```

### 4. 配置 API Key

编辑 `retriever-generator/agent_backend.py` 文件，在第 123 行设置你的 DashScope API Key：

```python
API_KEY = "your-api-key-here"  # 在这里设置你的 API key
```

### 5. 准备向量索引

确保 `retriever-generator/faiss_index2/` 目录下存在向量索引文件：
- `index.faiss`
- `index.pkl`

如果没有，需要先运行索引构建脚本（参考 `faiss_index/build_index.py`）。

## ⚙️ 配置说明

### API Key 配置

在 `retriever-generator/agent_backend.py` 中配置：

```python
API_KEY = "sk-your-api-key-here"
```

### 检索参数配置

在 Streamlit 界面的侧边栏可以配置：

1. **启用重排**：选择是否使用重排模型
2. **重排模型**：选择重排模型（qwen3-rerank 或 qwen-rerank）
3. **Top K**：召回的文档数量（1-20）
4. **Rerank Top N**：重排后返回的文档数量（1-10，仅在启用重排时使用）

### 默认配置

- **重排模型**：qwen3-rerank
- **Top K**：5（启用重排时）或 3（不启用重排时）
- **Rerank Top N**：3
- **LLM 模型**：qwen-flash
- **温度参数**：0.1

## 🚀 使用方法

### 方式一：在线使用（推荐）

#### 使用 Streamlit Cloud 部署（推荐）

**Streamlit Cloud** 是 Streamlit 官方提供的免费云服务，可以直接从 GitHub 部署你的应用。

**部署步骤：**

1. **访问 Streamlit Cloud**
   - 打开 [https://streamlit.io/cloud](https://streamlit.io/cloud)
   - 使用 GitHub 账号登录（需要授权 Streamlit Cloud 访问你的仓库）

2. **创建新应用**
   - 点击 "New app" 按钮
   - 选择你的 GitHub 仓库：`cwzbuaa/2025RAG`
   - 设置分支：`main`
   - 设置应用路径：`retriever-generator/app.py`
   - 点击 "Deploy" 开始部署

3. **等待部署完成**
   - 首次部署可能需要几分钟时间
   - Streamlit Cloud 会自动安装 `requirements.txt` 中的依赖

4. **配置 API Key（重要）**
   - 部署前，确保在 `retriever-generator/agent_backend.py` 中设置了 API Key
   - 或者使用 Streamlit Cloud 的 Secrets 功能（推荐）：
     - 在应用设置中找到 "Secrets" 选项
     - 添加 `DASH_API_KEY` 环境变量
     - 修改代码使用 `st.secrets["DASH_API_KEY"]` 读取

5. **访问应用**
   - 部署完成后，Streamlit Cloud 会提供一个公开的 URL
   - 格式：`https://your-app-name.streamlit.app`
   - 你可以将这个链接分享给任何人使用

**优点：**
- ✅ 完全免费（个人使用）
- ✅ 无需下载代码，直接在浏览器中使用
- ✅ 自动更新（代码推送到 GitHub 后自动重新部署）
- ✅ 公开访问链接，可分享给他人
- ✅ 无需服务器配置和维护
- ✅ 支持自定义域名（付费版）

**注意事项：**
- ⚠️ 首次部署需要几分钟时间
- ⚠️ 确保 API Key 已正确配置
- ⚠️ 确保 `requirements.txt` 包含所有依赖
- ⚠️ 确保向量索引文件已上传到 GitHub（如果文件较大，可能需要使用 Git LFS）

#### 使用 Hugging Face Spaces

1. **创建 Space**
   - 访问 [https://huggingface.co/spaces](https://huggingface.co/spaces)
   - 点击 "Create new Space"
   - 选择 "Streamlit" SDK
   - 连接到你的 GitHub 仓库

2. **配置应用**
   - 设置应用路径为 `retriever-generator/app.py`
   - 配置依赖文件 `requirements.txt`

3. **部署**
   - 点击 "Create Space" 完成部署

### 方式二：本地运行

#### 启动应用

```bash
cd retriever-generator
streamlit run app.py
```

应用将在浏览器中自动打开，默认地址为：`http://localhost:8501`

### 使用步骤

1. **配置参数**（侧边栏）
   - 选择是否启用重排
   - 如果启用重排，选择重排模型和设置参数
   - 设置 Top K 和 Top N 参数

2. **开始对话**
   - 在输入框中输入你的问题
   - 系统会自动检索相关文档并生成回答

3. **查看性能指标**
   - 侧边栏显示平均性能指标
   - 每次查询后显示本次查询的性能指标

4. **开始新对话**
   - 点击侧边栏的"🔄 开始新对话"按钮
   - 清空对话历史，开始新的会话

### 使用示例

**示例 1：查询具体菜谱**
```
用户：宫保鸡丁怎么做？
系统：根据检索到的菜谱，提供详细的食材清单和烹饪步骤
```

**示例 2：根据食材推荐**
```
用户：我只有鸡蛋和番茄，能做什么？
系统：推荐番茄炒蛋等相关菜谱
```

**示例 3：烹饪技巧**
```
用户：什么是焯水？
系统：解释焯水的概念和用途
```

## 📁 项目结构

```
2025RAG/
├── retriever-generator/          # 主要应用目录
│   ├── app.py                    # Streamlit 主应用
│   ├── agent_backend.py         # Agent 后端逻辑
│   ├── agentrag.py              # Agent RAG 示例
│   ├── Rerank_A_G.py            # 重排 RAG 示例
│   ├── faiss_index2/            # FAISS 向量索引
│   │   ├── index.faiss
│   │   └── index.pkl
│   └── __pycache__/
├── faiss_index/                  # 索引构建脚本
│   ├── build_index.py
│   ├── index.faiss
│   └── index.pkl
├── data/                         # 数据目录
│   ├── chunked_corpus_fuzi/
│   └── howtocook/
├── requirements.txt              # 依赖列表
├── fix_dependencies.sh          # 依赖修复脚本
└── README.md                    # 本文件
```

### 核心文件说明

- **`app.py`**：Streamlit Web 应用主文件，包含界面和交互逻辑
- **`agent_backend.py`**：Agent 后端，包含检索器、重排模型和 Agent 执行器的初始化
- **`agentrag.py`**：Agent RAG 的示例代码
- **`Rerank_A_G.py`**：带重排功能的 RAG 示例代码

## 📊 性能监控

系统提供详细的性能监控功能：

### 实时指标

- **检索时间**：向量检索和重排的总耗时
- **生成时间**：LLM 生成回答的耗时
- **总延迟**：从查询到回答的总时间
- **吞吐量**：每秒处理的请求数

### 查看方式

1. **单次查询指标**：每次查询后，在回答下方展开"📊 本次查询性能指标"
2. **平均指标**：侧边栏显示所有查询的平均性能指标

## ❓ 常见问题

### 1. 依赖冲突问题

如果遇到 LangChain 版本冲突，运行：

```bash
bash fix_dependencies.sh
```

### 2. API Key 错误

确保在 `agent_backend.py` 中正确设置了 API Key，并且 API Key 有效。

### 3. 向量索引不存在

如果提示找不到向量索引，需要先构建索引：

```bash
python faiss_index/build_index.py
```

### 4. 重排功能不工作

检查：
- 是否在界面中启用了重排
- API Key 是否有重排模型的权限
- 网络连接是否正常

### 5. 性能问题

如果响应较慢，可以尝试：
- 减少 Top K 值
- 禁用重排功能
- 检查网络连接

## 🔧 开发说明

### 修改 API Key

编辑 `retriever-generator/agent_backend.py`：

```python
API_KEY = "your-new-api-key"
```

### 修改默认参数

在 `agent_backend.py` 的 `load_agent_executor` 函数中修改默认值：

```python
def load_agent_executor(
    memory: ConversationBufferMemory = None,
    enable_rerank: bool = True,
    rerank_model: str = "qwen3-rerank",
    top_k: int = 5,
    rerank_top_n: int = 3
):
```

### 添加新的重排模型

在 `app.py` 的侧边栏配置中添加新的选项：

```python
rerank_model = st.selectbox(
    "重排模型",
    options=["qwen3-rerank", "qwen-rerank", "new-model"],  # 添加新模型
    ...
)
```

## 📝 许可证

本项目仅供学习和研究使用。

## 🙏 致谢

本项目的数据源自 GitHub 项目 [HowToCook](https://github.com/Anduin2017/HowToCook)，感谢原作者和所有贡献者的辛勤工作！

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系方式

如有问题，请提交 Issue 或联系项目维护者。

---

**祝您使用愉快！🍳**
