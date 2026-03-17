#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CPT训练脚本
使用LLaMA-Factory进行继续预训练
"""

import os
import argparse

# 安装LLaMA-Factory
def install_llama_factory():
    print("安装LLaMA-Factory...")
    os.system("pip install -U llama-factory")

# 准备CPT配置文件
def prepare_cpt_config(output_dir):
    config_content = f"""
# CPT训练配置文件

# 基本设置
model_name_or_path: str = "Qwen/Qwen2.5-7B"
output_dir: str = "{output_dir}"

# 训练设置
training_type: str = "pt"  # 预训练模式
dataset: list = ["cpt_data"]  # 使用自定义CPT数据集
data_seed: int = 42
train_batch_size: int = 4
gradient_accumulation_steps: int = 4
learning_rate: float = 2e-5
num_train_epochs: int = 3
warmup_ratio: float = 0.03

# 模型设置
max_seq_length: int = 2048
truncation_side: str = "right"

# 优化器设置
optimizer_type: str = "adamw_torch"
weight_decay: float = 0.01
device_map: str = "auto"

# 日志设置
logging_steps: int = 10

datasets:
  cpt_data:
    type: "text"
    path: "data/cpt_data.txt"
"""
    
    config_path = os.path.join(output_dir, "cpt_config.yaml")
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(config_content)
    return config_path

# 运行CPT训练
def run_cpt(config_path):
    print("开始CPT训练...")
    command = f"llama-factory-cli train {config_path}"
    os.system(command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str, default="output/cpt", help="输出目录")
    args = parser.parse_args()
    
    # 创建输出目录
    os.makedirs(args.output_dir, exist_ok=True)
    
    # 安装LLaMA-Factory
    install_llama_factory()
    
    # 准备配置文件
    config_path = prepare_cpt_config(args.output_dir)
    print(f"配置文件已生成：{config_path}")
    
    # 运行CPT训练
    run_cpt(config_path)
    
    print("CPT训练完成！")
