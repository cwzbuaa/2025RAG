#!/bin/bash
# 修复 LangChain 依赖冲突的脚本

echo "🔧 开始修复 LangChain 依赖冲突..."

# 1. 卸载不兼容的包（这些包需要 langchain-core>=1.0.0）
echo "📦 卸载不兼容的包..."
pip uninstall -y langchain-classic langgraph langgraph-prebuilt langgraph-checkpoint langgraph-sdk 2>/dev/null

# 2. 卸载现有的 LangChain 相关包
echo "📦 卸载现有的 LangChain 包..."
pip uninstall -y langchain langchain-core langchain-community langchain-openai langchain-text-splitters langsmith 2>/dev/null

# 3. 先安装核心包（确保版本兼容）
echo "📦 安装 LangChain 核心包..."
pip install "langchain-core>=0.3.72,<1.0.0" "langchain==0.3.27" "langchain-community==0.3.27" "langchain-openai==0.3.27" "langchain-text-splitters==0.3.11" "langsmith>=0.3.45,<1.0.0" "openai>=1.86.0,<2.0.0"

# 4. 安装其他依赖
echo "📦 安装其他依赖..."
pip install -r requirements.txt

echo "✅ 依赖修复完成！"
echo ""
echo "请运行以下命令验证："
echo "pip list | grep -E 'langchain|langsmith'"

