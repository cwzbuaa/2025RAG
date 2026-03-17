#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SFT数据生成脚本
根据菜谱数据生成指令微调训练数据
"""

import json
import random
import os
import glob

def extract_ingredients(content):
    """
    从菜谱内容中提取食材
    
    Args:
        content: 菜谱内容
    
    Returns:
        食材列表
    """
    ingredients = []
    # 简单提取食材部分
    lines = content.split('\n')
    in_ingredients = False
    
    for line in lines:
        line = line.strip()
        if '必备原料和工具' in line:
            in_ingredients = True
            continue
        elif line.startswith('## ') and in_ingredients:
            break
        
        if in_ingredients and line:
            # 提取食材名称
            if line.startswith('* ') or line.startswith('- '):
                ingredient = line[2:].strip()
                # 去除数量和括号内容
                ingredient = ingredient.split('（')[0].split('(')[0].strip()
                ingredient = ingredient.split(' ')[0].strip()
                if ingredient:
                    ingredients.append(ingredient)
    
    return ingredients

def generate_sft_data(input_file, output_file):
    """
    根据菜谱数据生成SFT训练数据
    
    Args:
        input_file: 输入JSONL文件路径
        output_file: 输出JSONL文件路径
    """
    recipes = []
    
    # 读取菜谱数据
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            try:
                data = json.loads(line)
                recipes.append(data)
            except json.JSONDecodeError:
                pass
    
    # 生成SFT数据
    sft_data = []
    
    for recipe in recipes:
        title = recipe['metadata'].get('title', '')
        content = recipe.get('content', '')
        ingredients = extract_ingredients(content)
        
        # 场景1：按食材推荐菜谱
        if ingredients:
            # 随机选择2-3种食材
            sample_ingredients = random.sample(ingredients, min(3, len(ingredients)))
            instruction = f"我有{','.join(sample_ingredients)}，能做什么菜？"
            output = f"你可以做{title}。{content}"
            sft_data.append({
                "instruction": instruction,
                "output": output
            })
        
        # 场景2：菜谱生成
        instruction = f"详细写一份{title}的菜谱。"
        output = content
        sft_data.append({
            "instruction": instruction,
            "output": output
        })
        
        # 场景3：烹饪答疑（简单生成）
        if '烹饪难度' in content:
            instruction = f"{title}的烹饪难度如何？"
            # 提取烹饪难度
            import re
            difficulty_match = re.search(r'预估烹饪难度：(.*?)星', content)
            if difficulty_match:
                difficulty = difficulty_match.group(1)
                output = f"{title}的预估烹饪难度为{difficulty}星，属于{['非常简单', '简单', '中等', '较难', '困难'][int(difficulty)-1]}的水平。"
                sft_data.append({
                    "instruction": instruction,
                    "output": output
                })
    
    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in sft_data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

if __name__ == "__main__":
    # 创建sft_data目录
    output_dir = "sft_data"
    os.makedirs(output_dir, exist_ok=True)
    
    # 查找data目录中的所有jsonl文件
    jsonl_files = glob.glob("data/*.jsonl")
    
    if not jsonl_files:
        print("在data目录中未找到jsonl文件")
    else:
        for input_file in jsonl_files:
            # 获取文件名
            filename = os.path.basename(input_file)
            # 生成输出文件路径
            output_file = os.path.join(output_dir, filename)
            # 生成SFT数据
            generate_sft_data(input_file, output_file)
            print(f"SFT数据生成完成，输出到 {output_file}")
