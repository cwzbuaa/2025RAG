#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
合并SFT数据脚本
将sft_data目录中的所有jsonl文件合并成一个文件
"""

import os
import glob

def merge_sft_data(input_dir, output_file):
    """
    合并SFT数据
    
    Args:
        input_dir: 输入目录路径
        output_file: 输出文件路径
    """
    # 查找所有jsonl文件
    jsonl_files = glob.glob(os.path.join(input_dir, "*.jsonl"))
    
    if not jsonl_files:
        print(f"在{input_dir}目录中未找到jsonl文件")
        return
    
    # 合并数据
    total_lines = 0
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for jsonl_file in jsonl_files:
            filename = os.path.basename(jsonl_file)
            print(f"正在处理: {filename}")
            
            with open(jsonl_file, 'r', encoding='utf-8') as f_in:
                lines = f_in.readlines()
                f_out.writelines(lines)
                total_lines += len(lines)
    
    print(f"\n合并完成！")
    print(f"总共处理了 {len(jsonl_files)} 个文件")
    print(f"总共合并了 {total_lines} 条数据")
    print(f"输出文件: {output_file}")

if __name__ == "__main__":
    input_dir = "sft_data"
    output_file = "data/sft_data_merged.jsonl"
    merge_sft_data(input_dir, output_file)
