import streamlit as st
import numpy as np
from pathlib import Path
import time
import requests
from typing import List, Dict, Tuple
import json
import re

# --- LangChain 核心组件 ---
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from pydantic.v1 import BaseModel, Field
from pydantic import ConfigDict

# --- LangChain Agent 组件 ---
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

# --- 重排模型类 ---
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

class RerankRetriever(BaseRetriever):
    """带重排功能的检索器"""
    vectorstore: object = Field(default=None, description="向量存储")
    rerank_chain: object = Field(default=None, description="重排链")
    top_k: int = Field(default=5, description="先召回的文档数量")
    rerank_top_n: int = Field(default=3, description="重排后返回的文档数量")
    retrieval_times: List[float] = Field(default_factory=list, description="记录所有检索时间")
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        retrieval_start = time.time()
        
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
        
        # 记录检索时间
        retrieval_time = time.time() - retrieval_start
        self.retrieval_times.append(retrieval_time)
        
        return reranked_docs
    
    def get_total_retrieval_time(self):
        """获取总检索时间"""
        return sum(self.retrieval_times)
    
    def reset_retrieval_times(self):
        """重置检索时间记录"""
        self.retrieval_times = []

# 注意：API key 在代码中配置
API_KEY = "sk"  # 在这里设置你的 API key

# 注意：由于需要动态参数，不使用@st.cache_resource装饰器
def load_agent_executor(
    memory: ConversationBufferMemory = None,
    enable_rerank: bool = True,
    rerank_model: str = "qwen3-rerank",
    top_k: int = 5,
    rerank_top_n: int = 3
):
    """
    加载所有模型和 Agent 执行器。
    支持记忆功能和可配置的重排参数。
    
    Args:
        memory: 对话记忆对象
        enable_rerank: 是否启用重排，默认为 True
        rerank_model: 重排模型名称，默认为 "qwen3-rerank"（仅在启用重排时使用）
        top_k: 召回的文档数量，默认为 5（启用重排时为召回数，不启用时为返回数）
        rerank_top_n: 重排后返回的文档数量，默认为 3（仅在启用重排时使用）
    """
    print("🚀 [缓存缺失] 正在加载模型和 Agent ...") # 这个只会打印一次

    # 1. 配置嵌入模型
    embedding_model = DashScopeEmbeddings(
        model="text-embedding-v4",
        dashscope_api_key=API_KEY
    )

    # 2. 加载 FAISS 向量库
    vectorstore = FAISS.load_local(
        "retriever-generator/faiss_index3", 
        embedding_model, 
        allow_dangerous_deserialization=True
    )

    # 3. 载入语料索引（用于父文档提升与溯源）
    corpus_path = Path(__file__).resolve().parents[1] / "data" / "chunked_corpus_fuzi" / "chunked_corpus.jsonl"
    docid_to_parent: Dict[str, str] = {}
    docid_to_meta: Dict[str, Dict] = {}
    child_to_docid: Dict[str, str] = {}
    child_prefix_to_candidates: Dict[str, List[Tuple[str, str]]] = {}

    if corpus_path.exists():
        with corpus_path.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    item = json.loads(line)
                except Exception:
                    continue
                doc_id = item.get("doc_id")
                child_content = item.get("child_content", "")
                parent_content = item.get("parent_content", "")
                meta = item.get("metadata", {}) or {}
                if not doc_id:
                    continue
                if parent_content:
                    docid_to_parent[doc_id] = parent_content
                docid_to_meta[doc_id] = meta
                if child_content:
                    child_to_docid[child_content] = doc_id
                    prefix = child_content[:120]
                    child_prefix_to_candidates.setdefault(prefix, []).append((doc_id, child_content))
        print(f"✅ 语料映射加载完成：doc_id={len(docid_to_parent)}, child条目={len(child_to_docid)}")
    else:
        print(f"⚠️ 未找到语料文件：{corpus_path}")

    def find_doc_id_by_child(text: str) -> str:
        """根据子块内容查找 doc_id，先精确匹配，再前缀候选匹配。"""
        if text in child_to_docid:
            return child_to_docid[text]
        prefix = text[:120]
        candidates = child_prefix_to_candidates.get(prefix, [])
        for cid, full in candidates:
            if text == full or text in full or full in text:
                return cid
        return ""

    def extract_key_sections(parent_text: str) -> Dict[str, str]:
        """从父文档中提取关键段：标题、食材（必备原料和工具）、操作步骤。"""
        sections = {"title": "", "ingredients": "", "steps": ""}
        lines = parent_text.splitlines()
        # 标题
        if lines:
            first = lines[0].strip()
            if first.startswith("#"):
                sections["title"] = first.lstrip("# ").strip()
        # 简单规则抽取
        text = parent_text
        # 食材段
        m_ing = re.search(r"##\s*必备原料和工具[\s\S]*?(?=\n##\s|\Z)", text)
        if m_ing:
            sections["ingredients"] = m_ing.group(0).strip()
        # 操作/步骤段
        m_steps = re.search(r"##\s*(操作|步骤)[\s\S]*?(?=\n##\s|\Z)", text)
        if m_steps:
            sections["steps"] = m_steps.group(0).strip()
        return sections

    def enrich_and_dedupe(docs: List[Document]) -> List[Document]:
        """将命中子块提升为父文档关键段，按 doc_id 去重并保留最高分。"""
        best_by_doc: Dict[str, Tuple[float, Document]] = {}
        for d in docs:
            score = 0.0
            if isinstance(d.metadata, dict):
                score = float(d.metadata.get("score", 0.0) or 0.0)
            child_text = d.page_content or ""
            doc_id = d.metadata.get("doc_id") if isinstance(d.metadata, dict) else None
            if not doc_id:
                doc_id = find_doc_id_by_child(child_text)
            title = ""
            source = ""
            parent_text = ""
            if doc_id and doc_id in docid_to_parent:
                parent_text = docid_to_parent.get(doc_id, "")
                meta = docid_to_meta.get(doc_id, {}) or {}
                title = meta.get("title", "")
                source = meta.get("source", "")
                ks = extract_key_sections(parent_text)
                # 组装 enriched 内容（限制长度以控制 tokens）
                enriched_parts = []
                if title:
                    enriched_parts.append(f"# {title}")
                enriched_parts.append("## 子块摘录\n" + (child_text[:800] + ("..." if len(child_text) > 800 else "")))
                if ks.get("ingredients"):
                    enriched_parts.append(ks["ingredients"][:1200])
                if ks.get("steps"):
                    enriched_parts.append(ks["steps"][:2000])
                enriched_text = "\n\n".join(enriched_parts)
                new_meta = dict(d.metadata or {})
                new_meta.update({
                    "doc_id": doc_id,
                    "title": title,
                    "source": source,
                    "score": score
                })
                enriched_doc = Document(page_content=enriched_text, metadata=new_meta)
            else:
                # 找不到父文档时，保留原子块，至少补齐可用的元数据
                new_meta = dict(d.metadata or {})
                if doc_id:
                    new_meta["doc_id"] = doc_id
                enriched_doc = Document(page_content=child_text, metadata=new_meta)

            key = enriched_doc.metadata.get("doc_id", f"__child_{id(enriched_doc)}")
            prev = best_by_doc.get(key)
            if prev is None or score > prev[0]:
                best_by_doc[key] = (score, enriched_doc)

        # 按分数降序返回
        result = [v[1] for v in sorted(best_by_doc.values(), key=lambda x: x[0], reverse=True)]
        # 控制返回数量不超过 rerank_top_n 或 top_k（根据是否启用重排）
        limit = rerank_top_n if enable_rerank else top_k
        return result[:limit]

    def child_only_with_meta(docs: List[Document]) -> List[Document]:
        """仅返回子块，但补齐 doc_id/title/source，并按父文档去重保留最高分的子块。"""
        best_by_doc: Dict[str, Tuple[float, Document]] = {}
        for d in docs:
            score = 0.0
            if isinstance(d.metadata, dict):
                score = float(d.metadata.get("score", 0.0) or 0.0)
            child_text = d.page_content or ""
            doc_id = d.metadata.get("doc_id") if isinstance(d.metadata, dict) else None
            if not doc_id:
                doc_id = find_doc_id_by_child(child_text)
            title = ""
            source = ""
            if doc_id:
                meta = docid_to_meta.get(doc_id, {}) or {}
                title = meta.get("title", "")
                source = meta.get("source", "")
            new_meta = dict(d.metadata or {})
            if doc_id:
                new_meta["doc_id"] = doc_id
            if title:
                new_meta["title"] = title
            if source:
                new_meta["source"] = source
            new_meta["score"] = score
            child_doc = Document(page_content=child_text, metadata=new_meta)
            key = doc_id or f"__child_{id(child_doc)}"
            prev = best_by_doc.get(key)
            if prev is None or score > prev[0]:
                best_by_doc[key] = (score, child_doc)
        # 排序与截断（与上面一致）
        result = [v[1] for v in sorted(best_by_doc.values(), key=lambda x: x[0], reverse=True)]
        limit = rerank_top_n if enable_rerank else top_k
        return result[:limit]

    def needs_parent_expansion(query: str) -> bool:
        """当问题涉及'做法/步骤/怎么做/做/如何做/recipe'等才使用父文档扩展。"""
        if not query:
            return False
        keywords = [
            r"做法", r"步骤", r"怎么做", r"如何做", r"做.*(菜|法)", r"recipe", r"教程", r"烹饪步骤"
        ]
        q = query.lower()
        for kw in keywords:
            if re.search(kw, query) or re.search(kw, q):
                return True
        return False

    # 4. 根据是否启用重排创建不同的检索器
    if enable_rerank:
        # 使用重排模型
        rerank_chain = RerankChain(api_key=API_KEY, model=rerank_model)
        retriever = RerankRetriever(
            vectorstore=vectorstore,
            rerank_chain=rerank_chain,
            top_k=top_k,        # 先召回 top_k 个
            rerank_top_n=rerank_top_n  # 重排后返回 rerank_top_n 个
        )
    else:
        # 不使用重排，直接使用普通检索器
        retriever = vectorstore.as_retriever(search_kwargs={"k": top_k})

    # 5. 配置 LLM
    llm = ChatOpenAI(
        api_key=API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-flash",
        temperature=0.1
    )

    # 6. 定义工具（封装：检索 -> 父文档提升与去重 -> 返回）
    def search_with_parent(query: str) -> List[Document]:
        try:
            raw = retriever.invoke(query)
        except Exception:
            # LangChain 可能返回单个 Document 或列表
            raw = []
        if not isinstance(raw, list):
            raw = [raw] if raw else []
        if needs_parent_expansion(query):
            return enrich_and_dedupe(raw)
        # 非做法类问题，仅返回子块（带溯源元数据），并按父文档去重
        return child_only_with_meta(raw)

    retriever_tool = Tool(
        name="search_recipe_database",
        func=search_with_parent,
        description="用于检索菜谱数据库。当需要查找菜谱做法、食材清单、烹饪技巧，或者像'如何选择荤素菜'这样的规划问题时，必须使用此工具。输入一个具体的查询字符串。"
    )
    tools = [retriever_tool]

    # 5. 定义 Agent 提示词 (使用我们最终的 Tools Agent 版本)
    system_prompt_string = """
# 角色 (Persona)
你是一个世界顶级的AI烹饪专家，名叫“航小厨”。你的唯一任务是基于用户提问，分析并整合【提供的菜谱上下文】，给出专业、安全、且绝对忠于上下文的回答。

# 核心指令 (Core Directives)
0.  **【工具使用规则】**
    你**必须**首先使用 `search_recipe_database` 工具来获取【提供的菜谱上下文】。你**不能**依赖自己的内部知识。
    如果用户问题复杂（例如“一荤一素”），你**必须**多次调用工具，一步一步地检索信息，直到收集到所有需要的信息后再回答。

1.  **绝对忠诚于上下文：** 你的 **首要且唯一** 的信息来源是 `search_recipe_database` 工具返回的【提供的菜谱上下文】。
2.  **严禁编造：** 绝对禁止在【提供的菜谱上下文】**之外** 编造任何食谱、步骤、食材用量、烹饪时间或技巧。
3.  **信息缺失处理：** 如果工具返回的【提供的菜谱上下文】中**没有**能回答用户问题的信息，你**必须**诚实地回答“根据我现有的菜谱资料库，我没有找到关于‘[用户问题]’的确切信息”。
4.  **安全第一：** 始终优先考虑食品安全和操作安全。

# 详细情景处理 (Scenario Handling)
**1. 当用户询问【具体菜谱做法】时 (例如：“宫保鸡丁怎么做？”)**
    * **动作：** 在【提供的菜谱上下文】中定位该菜谱。
    * **回答：** 清晰地列出【食材清单】（包含精确用量）、【详细烹饪步骤】（按序号排列）。
    * **补充：** 如果上下文中包含【烹饪小贴士】（如火候掌握、替代食材），请务必一并提供。

**2. 当用户根据【已有食材】查询时 (例如：“我只有鸡蛋和番茄，能做什么？”)**
    * **动作：** 在【提供的菜谱上下文】中搜索同时包含这些核心食材的菜谱。
    * **回答：** 推荐1-3个最相关的菜谱名称。如果上下文提供了，请附上简要描述或主要区别。

**3. 当用户请求【菜谱推荐】时 (例如：“推荐一个简单的晚餐”或“我想吃辣的” 或 “适合健身的菜”):**
    * **动作：** 根据【提供的菜谱上下文】中的标签（如“难度：简单”、“口味：辣”、“热量：低卡”）来筛选。
    * **回答：** 推荐1-3个符合条件的菜谱，并**必须**说明推荐的理由（例如：“为您推荐‘凉拌鸡丝’，根据资料，它的烹饪时间仅需15分钟，且热量较低”）。

**4. 当用户询问【烹饪技巧】或【概念】时 (例如：“什么是‘焯水’？”)**
    * **动作：** 在【提供的菜谱上下文】中查找相关的定义、目的或步骤。
    * **回答：** 基于上下文进行总结和解释。如果上下文中有多个菜谱都提到了这个技巧，可以综合说明。

**5. 当用户请求【菜谱修改】或【食材替换】时 (例如：“这道菜能不做辣吗？”或“没有XX食材怎么办？”)**
    * **动作：**
        1.  首先，检查【提供的菜谱上下文】中是否有关于“变体”（Variations）或“替代品”（Substitutions）的**明确说明**。
        2.  如果有，**必须**按照上下文的说明回答。
        3.  如果**没有**明确说明，你**不能**自己创造修改方案。你应该回答：“这份菜谱资料中没有提到关于[修改/替换]的具体建议。为了保证最佳风味和效果，建议您尽量遵循原菜谱。”

**6. 当用户问题【模糊不清】时 (例如：“晚饭”、“吃点啥”):**
    * **动作：** 不要强行推荐。
    * **回答：** 必须主动反问，以收集更多信息。例如：“为了帮您找到最合适的菜谱，您能告诉我您今天的口味偏好（比如酸甜、香辣）？或者您有多少烹饪时间吗？”

**7. 当用户问题【超出烹饪范围】时 (例如：“今天天气怎么样？”或“你是谁？”):**
    * **动作：** 礼貌地拒绝，并重申你的身份。
    * **回答：** “我是一个AI烹饪助手航小厨，我的任务是帮您处理关于菜谱的问题。很抱歉，我无法回答烹饪之外的问题。”

# 输出格式 (Output Format)
* **语气：** 友好、专业、耐心且可靠。
* **结构：** 优先使用项目符号（-）和编号列表（1., 2.）来呈现食材和步骤，确保回答清晰易读。
"""

    # 如果有memory，在prompt中添加历史消息
    if memory is not None:
        PROMPT_AGENT = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt_string),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
    else:
        PROMPT_AGENT = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt_string),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

    # 7. 创建 Agent 和执行器
    agent_runnable = create_openai_tools_agent(
        llm=llm,
        tools=tools,
        prompt=PROMPT_AGENT
    )
    
    # 创建AgentExecutor（注意：AgentExecutor不直接支持memory参数，我们需要手动管理）
    agent_executor = AgentExecutor(
        agent=agent_runnable,
        tools=tools,
        verbose=True, # 让 Agent 在终端打印思考过程
        handle_parsing_errors=True,
        return_intermediate_steps=True
    )
    
    print("✅ Agent 加载并缓存成功！")
    return agent_executor, retriever, memory