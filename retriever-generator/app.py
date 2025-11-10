import streamlit as st
import time
from agent_backend import load_agent_executor
from langchain.memory import ConversationBufferMemory
#   streamlit run retriever-generator/app.py
# --- 1. 页面设置 ---
st.set_page_config(
    page_title="航小厨 - 你的AI烹饪助手",
    page_icon="🍳",
    layout="wide"
)
st.title("航小厨 🍳 - 你的AI烹饪助手")

# --- 2. 侧边栏：配置 ---
with st.sidebar:
    st.header("⚙️ 配置")
    
    # 是否启用重排
    enable_rerank = st.checkbox(
        "启用重排",
        value=st.session_state.get("enable_rerank", True),
        help="是否使用重排模型对检索结果进行重排"
    )
    st.session_state.enable_rerank = enable_rerank
    
    if enable_rerank:
        # 重排模型选择
        rerank_model = st.selectbox(
            "重排模型",
            options=["qwen3-rerank", "qwen-rerank"],
            index=0,
            help="选择用于重排的模型"
        )
        st.session_state.rerank_model = rerank_model
        
        # Top K 参数（重排时使用）
        top_k = st.number_input(
            "Top K (召回文档数)",
            min_value=1,
            max_value=20,
            value=st.session_state.get("top_k", 5),
            step=1,
            help="先从向量库召回的文档数量"
        )
        st.session_state.top_k = top_k
        
        # Rerank Top N 参数
        rerank_top_n = st.number_input(
            "Rerank Top N (重排后返回数)",
            min_value=1,
            max_value=10,
            value=st.session_state.get("rerank_top_n", 3),
            step=1,
            help="重排后返回的文档数量"
        )
        st.session_state.rerank_top_n = rerank_top_n
    else:
        # 不使用重排时，直接设置返回文档数
        top_k = st.number_input(
            "Top K (返回文档数)",
            min_value=1,
            max_value=20,
            value=st.session_state.get("top_k", 3),
            step=1,
            help="直接从向量库返回的文档数量"
        )
        st.session_state.top_k = top_k
        # 不使用重排时，设置默认值
        st.session_state.rerank_model = "qwen3-rerank"
        st.session_state.rerank_top_n = top_k
    
    st.divider()
    
    # 新对话按钮
    if st.button("🔄 开始新对话", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "你好！我是航小厨，一个AI烹饪专家。你想做什么菜？或者告诉我你有什么食材？"}
        ]
        st.session_state.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        # 清除 agent_executor，强制重新加载（使用新的 memory）
        if "agent_executor" in st.session_state:
            del st.session_state.agent_executor
        if "rerank_retriever" in st.session_state:
            del st.session_state.rerank_retriever
        st.session_state.performance_metrics = []  # 重置性能指标
        st.rerun()
    
    st.divider()
    
    # 性能指标显示
    st.header("📊 性能指标")
    if "performance_metrics" in st.session_state and st.session_state.performance_metrics:
        metrics = st.session_state.performance_metrics
        avg_retrieval_time = sum(m["retrieval_time"] for m in metrics) / len(metrics)
        avg_generation_time = sum(m["generation_time"] for m in metrics) / len(metrics)
        avg_total_time = sum(m["total_time"] for m in metrics) / len(metrics)
        throughput = len(metrics) / sum(m["total_time"] for m in metrics) if sum(m["total_time"] for m in metrics) > 0 else 0
        
        st.metric("平均检索时间", f"{avg_retrieval_time:.3f}秒")
        st.metric("平均生成时间", f"{avg_generation_time:.3f}秒")
        st.metric("平均总延迟", f"{avg_total_time:.3f}秒")
        st.metric("吞吐量", f"{throughput:.2f} 请求/秒")
    else:
        st.info("暂无性能数据")

# --- 3. 初始化会话状态 ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "你好！我是航小厨，一个AI烹饪专家。你想做什么菜？或者告诉我你有什么食材？"}
    ]

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

if "performance_metrics" not in st.session_state:
    st.session_state.performance_metrics = []

# 初始化配置参数
if "enable_rerank" not in st.session_state:
    st.session_state.enable_rerank = True
if "rerank_model" not in st.session_state:
    st.session_state.rerank_model = "qwen3-rerank"
if "top_k" not in st.session_state:
    st.session_state.top_k = 5
if "rerank_top_n" not in st.session_state:
    st.session_state.rerank_top_n = 3

# --- 4. 加载 Agent ---
try:
    # 检查是否需要重新加载 Agent（参数改变时或 agent_executor 不存在/为 None）
    config_changed = (
        st.session_state.get("current_enable_rerank") != st.session_state.enable_rerank
        or st.session_state.get("current_rerank_model") != st.session_state.rerank_model
        or st.session_state.get("current_top_k") != st.session_state.top_k
        or st.session_state.get("current_rerank_top_n") != st.session_state.rerank_top_n
    )
    
    if ("agent_executor" not in st.session_state 
        or st.session_state.get("agent_executor") is None
        or config_changed):
        with st.spinner("正在加载模型和 Agent..."):
            agent_executor, retriever, memory = load_agent_executor(
                memory=st.session_state.memory,
                enable_rerank=st.session_state.enable_rerank,
                rerank_model=st.session_state.rerank_model,
                top_k=st.session_state.top_k,
                rerank_top_n=st.session_state.rerank_top_n
            )
            st.session_state.agent_executor = agent_executor
            st.session_state.rerank_retriever = retriever  # 可能是 rerank_retriever 或普通 retriever
            st.session_state.memory = memory
            st.session_state.current_enable_rerank = st.session_state.enable_rerank
            st.session_state.current_rerank_model = st.session_state.rerank_model
            st.session_state.current_top_k = st.session_state.top_k
            st.session_state.current_rerank_top_n = st.session_state.rerank_top_n
            st.success("✅ Agent 加载成功！")
except Exception as e:
    st.error(f"加载 Agent 时出错: {e}")
    st.stop()

# 确保 agent_executor 已加载
if st.session_state.get("agent_executor") is None:
    st.error("❌ Agent 未正确加载，请刷新页面重试")
    st.stop()

# --- 5. 显示聊天历史 ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 6. 处理用户输入 ---
if prompt := st.chat_input("请输入你的问题..."):
    
    # 6.1 将用户消息添加到历史并显示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 6.2 获取 Agent 的回答（带性能监控）
    with st.chat_message("assistant"):
        with st.spinner("航小厨正在思考中..."):
            try:
                # 重置检索时间记录
                if hasattr(st.session_state.rerank_retriever, 'reset_retrieval_times'):
                    st.session_state.rerank_retriever.reset_retrieval_times()
                
                # 记录开始时间
                total_start_time = time.time()
                
                # 准备输入（包含历史消息）
                input_dict = {"input": prompt}
                if st.session_state.memory:
                    # 获取历史消息（即使为空也要传递，因为 prompt 需要 chat_history 变量）
                    chat_history = st.session_state.memory.chat_memory.messages
                    input_dict["chat_history"] = chat_history if chat_history else []
                
                # 执行Agent（包含检索和生成）
                response = st.session_state.agent_executor.invoke(input_dict)
                total_end_time = time.time()
                total_time = total_end_time - total_start_time
                
                # 计算检索时间（从检索器中获取）
                retrieval_time = 0
                if hasattr(st.session_state.rerank_retriever, 'get_total_retrieval_time'):
                    retrieval_time = st.session_state.rerank_retriever.get_total_retrieval_time()
                else:
                    # 如果没有记录，则通过中间步骤数量估算
                    if "intermediate_steps" in response and response["intermediate_steps"]:
                        num_retrieval_steps = len([s for s in response["intermediate_steps"] 
                                                   if isinstance(s, tuple) and hasattr(s[0], 'tool')])
                        # 估算：每次检索（包括向量检索和重排）大约需要0.3-0.5秒
                        retrieval_time = num_retrieval_steps * 0.4
                        # 如果总时间很短，则按比例分配
                        if retrieval_time > total_time * 0.8:
                            retrieval_time = total_time * 0.6  # 检索占60%
                
                # 计算生成时间（总时间减去检索时间）
                generation_time = max(0, total_time - retrieval_time)
                
                # 记录性能指标
                performance_metric = {
                    "retrieval_time": retrieval_time,
                    "generation_time": generation_time,
                    "total_time": total_time
                }
                st.session_state.performance_metrics.append(performance_metric)
                
                final_answer = response["output"]
                
                # 更新记忆
                if st.session_state.memory:
                    st.session_state.memory.chat_memory.add_user_message(prompt)
                    st.session_state.memory.chat_memory.add_ai_message(final_answer)
                
                # 显示最终答案
                st.markdown(final_answer)
                
                # 显示性能指标
                with st.expander("📊 本次查询性能指标"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("检索时间", f"{retrieval_time:.3f}秒")
                    with col2:
                        st.metric("生成时间", f"{generation_time:.3f}秒")
                    with col3:
                        st.metric("总延迟", f"{total_time:.3f}秒")

                # [可选] 显示 Agent 的思考过程和检索到的上下文
                with st.expander("🔍 点击查看航小厨的思考过程 (检索到的资料)"):
                    if "intermediate_steps" in response and response["intermediate_steps"]:
                        for i, step in enumerate(response["intermediate_steps"]):
                            # Streamlit 在处理 LangChain 的 AgentAction 和 Observation 时需要一点帮助
                            if isinstance(step, tuple):
                                action, observation = step
                                
                                if hasattr(action, 'tool'):
                                    st.markdown(f"**步骤 {i+1}: 检索**")
                                    st.code(f"工具: {action.tool}\n输入: {action.tool_input}", language="text")
                                    st.markdown(f"**检索结果:**")
                                    if isinstance(observation, list):
                                        for j, doc in enumerate(observation):
                                            score = doc.metadata.get('score', 0) if hasattr(doc, 'metadata') else 0
                                            st.info(f"**文档 {j+1}** (相关性分数: {score:.4f})\n\n{doc.page_content[:300]}...")
                                    else:
                                        st.write(observation)
                                else:
                                    st.write(f"步骤 {i+1} (非工具调用): {step}")
                            else:
                                st.write(f"步骤 {i+1}: {step}")
                    else:
                        st.write("Agent 未使用检索工具或未返回中间步骤。")

                # 6.3 将 Agent 的回答添加到历史
                st.session_state.messages.append({"role": "assistant", "content": final_answer})

            except Exception as e:
                st.error(f"Agent 执行出错: {e}")
                import traceback
                st.code(traceback.format_exc())
