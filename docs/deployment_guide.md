# 云端部署说明

## 部署前准备

### 1. 数据准备
在部署到云端之前，需要先在本地完成以下步骤：

```bash
# 1. 生成SFT数据
python scripts/generate_sft_data.py

# 2. 合并SFT数据
python scripts/merge_sft_data.py
```

这将在`data`目录下生成：
- `sft_data_merged.jsonl` - 合并后的SFT训练数据
- `dataset_info.json` - LLaMA-Factory数据集配置文件

### 2. 文件检查
确保以下文件存在：
- `data/sft_data_merged.jsonl`
- `data/dataset_info.json`
- `requirements.txt`
- `scripts/run_sft.py`

## 云端部署步骤

### 1. 上传文件
将整个`deepcook`文件夹上传到云端服务器

### 2. 安装依赖
```bash
cd deepcook
pip install -r requirements.txt
```

### 3. 运行SFT训练
```bash
# 使用默认参数（Qwen2.5-7B基座模型）
python scripts/run_sft.py

# 或指定自定义模型路径
python scripts/run_sft.py --cpt_model_path /path/to/your/model --output_dir output/sft
```

## LLaMA-Factory配置说明

### dataset_info.json
该文件定义了数据集的格式和位置：
```json
{
  "sft_data": {
    "file_name": "sft_data_merged.jsonl",
    "formatting": "sharegpt",
    "columns": {
      "messages": "conversations"
    },
    "tags": {
      "role_tag": "role",
      "content_tag": "content",
      "user_tag": "user",
      "assistant_tag": "assistant"
    }
  }
}
```

### 训练配置
`run_sft.py`会自动生成训练配置文件，主要参数包括：
- `stage: sft` - 指令微调模式
- `dataset: sft_data` - 使用的数据集名称
- `dataset_dir: data` - 数据集目录
- `finetuning_type: lora` - 使用LoRA微调
- `learning_rate: 5e-5` - 学习率
- `num_train_epochs: 3.0` - 训练轮数

## 训练监控

训练过程中会生成：
- `output/sft/` - 输出目录
- 训练日志和检查点
- 损失曲线图（`plot_loss: True`）

## 常见问题

### 1. 数据集格式错误
确保`dataset_info.json`中的配置与实际数据格式匹配。

### 2. 显存不足
可以调整以下参数：
- `per_device_train_batch_size`: 减小batch size
- `gradient_accumulation_steps`: 增加梯度累积步数
- `lora_rank`: 减小LoRA秩

### 3. 模型下载慢
可以提前下载模型到本地，然后指定本地路径：
```bash
python scripts/run_sft.py --cpt_model_path /local/path/to/model
```

## 训练完成后

训练完成后，模型会保存在`output/sft/`目录中，可以：
1. 使用`evaluate_model.py`评估模型性能
2. 使用`deploy_app.py`部署Web界面
