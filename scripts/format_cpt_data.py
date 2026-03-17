#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CPT数据格式化脚本
将菜谱JSONL文件转换为适合继续预训练的文本格式
"""

import json
import re

def format_cpt_data(input_file, output_file):
    """
    将菜谱JSONL文件转换为CPT训练格式
    
    Args:
        input_file: 输入JSONL文件路径
        output_file: 输出文本文件路径
    """
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            line = line.strip()
            if not line:
                continue
            
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue
            
            # 提取菜谱内容
            content = data.get('content', '')
            metadata = data.get('metadata', {})
            title = metadata.get('title', '')
            
            # 清理内容，去除特殊字符和多余空白
            content = re.sub(r'\s+', ' ', content)
            content = re.sub(r'[\\`]', '', content)
            
            # 格式化CPT数据
            cpt_text = f"菜名：{title}\n"
            cpt_text += f"{content}\n\n"
            
            # 写入输出文件
            f_out.write(cpt_text)

if __name__ == "__main__":
    input_file = "data/corpus_菜谱-半成品加工.jsonl"
    output_file = "data/cpt_data.txt"
    format_cpt_data(input_file, output_file)
    print(f"CPT数据格式化完成，输出到 {output_file}")
