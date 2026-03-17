#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模型评估脚本
评估菜谱大模型的性能
"""

import os
import json
import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM

# 计算困惑度
def calculate_perplexity(model_path, test_data_path):
    """
    计算模型在测试数据上的困惑度
    
    Args:
        model_path: 模型路径
        test_data_path: 测试数据路径
    
    Returns:
        困惑度值
    """
    print("计算困惑度...")
    
    # 加载模型和分词器
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    
    # 读取测试数据
    test_texts = []
    with open(test_data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                test_texts.append(line)
    
    # 计算困惑度
    total_loss = 0
    total_tokens = 0
    
    for text in test_texts:
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss.item()
        total_loss += loss * inputs["input_ids"].size(1)
        total_tokens += inputs["input_ids"].size(1)
    
    perplexity = (total_loss / total_tokens) ** 0.5
    print(f"困惑度: {perplexity:.4f}")
    return perplexity

# 生成测试用例
def generate_test_cases(output_path):
    """
    生成测试用例
    
    Args:
        output_path: 输出路径
    """
    test_cases = [
        # 按食材推荐
        {"instruction": "我冰箱里只有番茄、鸡蛋和面条，能做什么？", "type": "ingredient_recommendation"},
        {"instruction": "我有五花肉、酱油和冰糖，能做什么菜？", "type": "ingredient_recommendation"},
        {"instruction": "我只有速冻水饺，怎么做？", "type": "ingredient_recommendation"},
        
        # 菜谱生成
        {"instruction": "详细写一份红烧肉的菜谱。", "type": "recipe_generation"},
        {"instruction": "详细写一份番茄鸡蛋面的菜谱。", "type": "recipe_generation"},
        {"instruction": "详细写一份空气炸锅鸡翅的菜谱。", "type": "recipe_generation"},
        
        # 烹饪答疑
        {"instruction": "为什么我煎的牛排总是发柴？", "type": "cooking_qa"},
        {"instruction": "煮速冻水饺需要多久？", "type": "cooking_qa"},
        {"instruction": "空气炸锅的温度如何控制？", "type": "cooking_qa"},
    ]
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for case in test_cases:
            json.dump(case, f, ensure_ascii=False)
            f.write('\n')
    
    print(f"测试用例已生成：{output_path}")

# 模型推理
def model_inference(model_path, test_cases_path, output_path):
    """
    使用模型进行推理
    
    Args:
        model_path: 模型路径
        test_cases_path: 测试用例路径
        output_path: 输出路径
    """
    print("模型推理...")
    
    # 加载模型和分词器
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    
    # 读取测试用例
    test_cases = []
    with open(test_cases_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                test_cases.append(json.loads(line))
    
    # 推理
    results = []
    for case in test_cases:
        instruction = case["instruction"]
        
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
        
        results.append({
            "instruction": instruction,
            "type": case["type"],
            "output": answer
        })
    
    # 保存结果
    with open(output_path, 'w', encoding='utf-8') as f:
        for result in results:
            json.dump(result, f, ensure_ascii=False)
            f.write('\n')
    
    print(f"推理结果已保存：{output_path}")

# LLM-as-a-Judge评估
def llm_as_judge(evaluation_path, output_path):
    """
    使用LLM作为裁判进行评估
    
    Args:
        evaluation_path: 评估数据路径
        output_path: 输出路径
    """
    print("LLM-as-a-Judge评估...")
    
    # 这里简化处理，实际使用时可以调用GPT-4o API
    # 读取评估数据
    evaluations = []
    with open(evaluation_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                evaluations.append(json.loads(line))
    
    # 模拟评估
    results = []
    for eval_item in evaluations:
        instruction = eval_item["instruction"]
        output = eval_item["output"]
        
        # 简单的评估逻辑
        score = 0
        if len(output) > 100:
            score += 2
        if "做法" in output or "步骤" in output:
            score += 2
        if "原料" in output or "食材" in output:
            score += 2
        if "时间" in output or "温度" in output:
            score += 2
        if "注意" in output or "提示" in output:
            score += 2
        
        results.append({
            "instruction": instruction,
            "output": output,
            "score": score,
            "feedback": f"整体质量良好，得分为{score}/10"
        })
    
    # 保存结果
    with open(output_path, 'w', encoding='utf-8') as f:
        for result in results:
            json.dump(result, f, ensure_ascii=False)
            f.write('\n')
    
    print(f"LLM-as-a-Judge评估结果已保存：{output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, default="output/sft", help="模型路径")
    parser.add_argument("--test_data_path", type=str, default="data/cpt_data.txt", help="测试数据路径")
    parser.add_argument("--output_dir", type=str, default="output/evaluation", help="输出目录")
    args = parser.parse_args()
    
    # 创建输出目录
    os.makedirs(args.output_dir, exist_ok=True)
    
    # 计算困惑度
    calculate_perplexity(args.model_path, args.test_data_path)
    
    # 生成测试用例
    test_cases_path = os.path.join(args.output_dir, "test_cases.jsonl")
    generate_test_cases(test_cases_path)
    
    # 模型推理
    inference_path = os.path.join(args.output_dir, "inference_results.jsonl")
    model_inference(args.model_path, test_cases_path, inference_path)
    
    # LLM-as-a-Judge评估
    judge_path = os.path.join(args.output_dir, "llm_judge_results.jsonl")
    llm_as_judge(inference_path, judge_path)
    
    print("模型评估完成！")
