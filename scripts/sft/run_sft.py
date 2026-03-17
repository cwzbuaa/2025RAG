#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SFT训练脚本 - 适配 4090 D & Qwen2.5-7B
"""

import os
import argparse

def prepare_sft_config(output_dir, cpt_model_path):
    # 彻底移除所有中文注释，防止 Windows 读取时产生编码冲突
    # 注意：dataset 已经修改为 sft_data_merged 以对齐 info 文件
    config_content = f"""
model_name_or_path: {cpt_model_path}
output_dir: {output_dir}

stage: sft
do_train: true
dataset: sft_data_merged
dataset_dir: data
template: qwen
cutoff_len: 2048
overwrite_output_dir: true
preprocessing_num_workers: 4

per_device_train_batch_size: 4
gradient_accumulation_steps: 4
learning_rate: 0.00005
num_train_epochs: 3.0
lr_scheduler_type: cosine
warmup_ratio: 0.1
bf16: true
fp16: false

finetuning_type: lora
lora_rank: 8
lora_alpha: 16
lora_dropout: 0.1
lora_target: all

logging_steps: 5
save_steps: 100
plot_loss: true

val_size: 0.1
per_device_eval_batch_size: 4
eval_strategy: steps
eval_steps: 100
"""

    os.makedirs(output_dir, exist_ok=True)
    config_path = os.path.join(output_dir, "sft_config.yaml")

    # 显式使用 utf-8 写入
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(config_content.strip())
    return config_path


def run_sft(config_path):
    print("启动 LLaMA-Factory 训练进程...")
    # 使用 python -m llamafactory.cli 确保环境兼容性
    command = f"python -m llamafactory.cli train {config_path}"
    os.system(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str, default="output/recipe_sft", help="输出目录")
    parser.add_argument("--cpt_model_path", type=str, default="E:/models/qwen2_5_7b", help="基座模型路径")
    args = parser.parse_args()

    # 1. 生成配置
    config_p = prepare_sft_config(args.output_dir, args.cpt_model_path)
    print(f"配置文件已就绪: {config_p}")

    # 2. 执行训练
    run_sft(config_p)
