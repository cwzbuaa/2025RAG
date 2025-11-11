import numpy as np
from pathlib import Path

# --- LangChain 核心组件 ---
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS

# --- LangChain Agent 组件 (新导入) ---
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, create_openai_tools_agent  # <-- 变更
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder # <-- 变更

# ----------------------------
# 1. 配置 DashScope 嵌入模型（与你原来一致）
# ----------------------------
embedding_model = DashScopeEmbeddings(
    model="text-embedding-v4",
    dashscope_api_key="sk-f1d25d991a2f4b1699daf8bc3c8d880b"
)
print("✅ 嵌入模型加载成功")

# ----------------------------
# 2. 测试嵌入模型维度（与你原来一致）
# ... (你的测试代码) ...
# ----------------------------

# ----------------------------
# 3. 加载 FAISS 向量库（与你原来一致）
# ----------------------------
vectorstore = FAISS.load_local("faiss_index2", embedding_model, allow_dangerous_deserialization=True)
print("✅ FAISS 向量库加载成功")

# ----------------------------
# 4. 配置 LLM（与你原来一致）
# ----------------------------
llm = ChatOpenAI(
    api_key="sk-f1d25d991a2f4b1699daf8bc3c8d880b",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-flash",
    temperature=0.1
)
print("✅ LLM 配置成功")


# ----------------------------------------------------
# 5. 【代码修改核心】: 定义 Agent 使用的“工具”
#    (这部分与你之前的 Agent 代码基本一致)
# ----------------------------------------------------

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

retriever_tool = Tool(
    name="search_recipe_database",
    func=retriever.invoke,
    description="用于检索菜谱数据库。当需要查找菜谱做法、食材清单、烹饪技巧，或者像'如何选择荤素菜'这样的规划问题时，必须使用此工具。输入一个具体的查询字符串。"
)

tools = [retriever_tool]

# ----------------------------------------------------
# 6. 【代码修改核心】: 创建 "Tools Agent" 提示词
#    这个提示词更简单、更直接。
#    我们将你所有的规则都放进 System Prompt 中。
# ----------------------------------------------------

# 这就是你原来的 "RetrievalQA" 提示词，我们现在把它用作 Agent 的系统提示词
# 我在顶部额外添加了一条【工具使用规则】，以确保它会去检索
system_prompt_string = """
# 角色 (Persona)
你是一个世界顶级的AI烹饪专家，名叫“航小厨”。你的唯一任务是基于用户提问，分析并整合【提供的菜谱上下文】，给出专业、安全、且绝对忠于上下文的回答。

# 核心指令 (Core Directives)
0.  **【工具使用规则】**
    你**必须**首先使用 `search_recipe_database` 工具来获取【提供的菜谱上下文】。你**不能**依赖自己的内部知识。
    如果用户问题复杂（例如“一荤一素”），你**必须**多次调用工具，一步一步地检索信息，直到收集到所有需要的信息后再回答。

1.  **绝对忠诚于上下文：** 你的 **首要且唯一** 的信息来源是 `search_recipe_database` 工具返回的【提供的菜谱上下文】。
2.  **严禁编造：** 绝对禁止在【提供的菜谱上下文】**之外** 编造任何食谱、步骤、食材用量、烹饪时间或技巧。
3.  **信息缺失处理：** 如果工具返回的【提供的菜谱上下文】中**没有**能回答用户问题的信息，你**必须**诚实地回答“实在抱歉，我只是一个厨师，根据我现有的菜谱资料库，我没有找到关于‘[用户问题]’的确切信息”。
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
* **语气：** 友好、专业、耐心且绝对可靠。
* **结构：** 优先使用项目符号（-）和编号列表（1., 2.）来呈现食材和步骤，确保回答清晰易读。
"""

PROMPT_AGENT = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt_string),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"), # Agent 存放思考和工具调用的地方
    ]
)

print("✅ Agent 提示词创建成功 (Tools Agent 模式)")

# ----------------------------------------------------
# 7. 【代码修改核心】: 创建 Agent 和 Agent 执行器
# ----------------------------------------------------

# 1. 创建 Agent (使用新的函数)
agent_runnable = create_openai_tools_agent(
    llm=llm,
    tools=tools,
    prompt=PROMPT_AGENT
)

# 2. 创建 Agent 执行器 (与之前相同)
agent_executor = AgentExecutor(
    agent=agent_runnable,
    tools=tools,
    verbose=True,  # 保持 True，观察思考过程
    handle_parsing_errors=True,
    return_intermediate_steps=True
)
print("✅ Agent 执行器创建成功")

# ----------------------------
# 8. 测试问答 (与你之前的 Agent 代码一致)
# ----------------------------
if __name__ == "__main__":
    query = input("请输入你的问题：")
    print(f"问题：{query}\n")
    
    # 执行 Agent
    result = agent_executor.invoke({"input": query})
    
    print("\n\n==========================================")
    print("           Agent 执行完毕")
    print("==========================================")

    # 打印所有中间步骤中召回的文档
    print("\n=== Retrieved Documents (All Steps) ===")
    if "intermediate_steps" in result and result["intermediate_steps"]:
        for step in result["intermediate_steps"]:
            # Tools Agent 的 'step' 格式是 (AgentAction, Observation)
            # ReAct Agent 的 'step' 格式是 (AgentStep)
            
            # 我们需要处理两种可能的格式，以确保健壮性
            if hasattr(step, 'tool_call'): # 新版 Tools Agent 格式
                action = step
                observation = "Tool call result not shown in this view" # 结果在 scratchpad 中
            elif isinstance(step, tuple): # 旧版 ReAct 或 LangChain 格式
                action, observation = step
            else:
                print(f"  无法解析的步骤: {step}")
                continue

            if hasattr(action, 'tool'):
                print(f"\n--- 检索工具: {action.tool} (输入: {action.tool_input}) ---")
                if isinstance(observation, list): # 我们的工具返回的是一个 Document 列表
                    for i, doc in enumerate(observation):
                        print(f"  Source {i+1}:", doc.page_content[:150] + "...")
                else:
                    print("  Observation (Raw):", str(observation)[:150] + "...")
            else:
                 print(f"  中间步骤 (非工具调用): {step}")

    else:
        print("... Agent 未使用检索工具或未返回中间步骤 ...")


    print("\n✅ 最终回答：")
    print(result["output"].strip())