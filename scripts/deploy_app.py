#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
部署应用脚本
使用Gradio创建一个简单的AI私人主厨Web界面
"""

import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import os

# 加载模型和分词器
model_path = "output/sft"  # SFT后的模型路径
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

def generate_recipe(instruction):
    """
    生成菜谱
    
    Args:
        instruction: 用户指令
    
    Returns:
        生成的菜谱
    """
    # 构建输入
    input_text = f"### 指令:\n{instruction}\n\n### 回答:\n"
    inputs = tokenizer(input_text, return_tensors="pt")
    
    # 生成回答
    outputs = model.generate(
        **inputs,
        max_new_tokens=1024,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.1
    )
    
    # 解码回答
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    answer = answer.split("### 回答:\n")[-1].strip()
    
    return answer

# 创建Gradio界面
with gr.Blocks(title="AI私人主厨") as app:
    gr.Markdown("""
    # AI私人主厨
    基于菜谱大模型的智能烹饪助手
    
    你可以：
    - 根据食材推荐菜谱
    - 生成详细的菜谱
    - 咨询烹饪问题
    """)
    
    with gr.Tab("根据食材推荐菜谱"):
        ingredients = gr.Textbox(label="输入你拥有的食材（用逗号分隔）", placeholder="例如：番茄,鸡蛋,面条")
        recommend_button = gr.Button("推荐菜谱")
        recommend_output = gr.Textbox(label="推荐结果", lines=10)
        
        def recommend_recipe(ingredients):
            instruction = f"我有{ingredients}，能做什么菜？"
            return generate_recipe(instruction)
        
        recommend_button.click(fn=recommend_recipe, inputs=ingredients, outputs=recommend_output)
    
    with gr.Tab("生成菜谱"):
        dish_name = gr.Textbox(label="输入菜名", placeholder="例如：红烧肉")
        generate_button = gr.Button("生成菜谱")
        generate_output = gr.Textbox(label="菜谱详情", lines=10)
        
        def generate_detailed_recipe(dish_name):
            instruction = f"详细写一份{dish_name}的菜谱。"
            return generate_recipe(instruction)
        
        generate_button.click(fn=generate_detailed_recipe, inputs=dish_name, outputs=generate_output)
    
    with gr.Tab("烹饪答疑"):
        question = gr.Textbox(label="输入你的烹饪问题", placeholder="例如：为什么我煎的牛排总是发柴？")
        qa_button = gr.Button("解答")
        qa_output = gr.Textbox(label="解答结果", lines=10)
        
        def answer_cooking_question(question):
            return generate_recipe(question)
        
        qa_button.click(fn=answer_cooking_question, inputs=question, outputs=qa_output)
    
    gr.Markdown("""
    ---
    提示：
    - 请尽量详细地描述你的需求
    - 模型可能会产生一些不准确的信息，请谨慎参考
    - 烹饪时请注意安全
    """)

if __name__ == "__main__":
    # 启动应用
    app.launch(share=True)
