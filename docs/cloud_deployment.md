# 云端部署指南 - 仅SFT训练

## 准备工作

### 1. 上传文件
将整个`deepcook`文件夹上传到云端服务器。

### 2. 安装依赖
```bash
cd deepcook
pip install -r requirements.txt
```

### 3. 检查数据文件
确保以下文件存在：
- `data/sft_data_merged.jsonl` - 合并后的SFT训练数据
- `data/dataset_info.json` - LLaMA-Factory数据集配置文件

## 开始SFT训练

### 1. 直接运行（推荐）
使用默认参数运行训练：
```bash
python scripts/run_sft.py
```

### 2. 自定义参数运行
如果需要自定义模型路径或输出目录：
```bash
# 使用其他模型
python scripts/run_sft.py --cpt_model_path "your/model/path" --output_dir "your/output/dir"

# 例如使用ChatGLM模型
python scripts/run_sft.py --cpt_model_path "THUDM/chatglm3-6b" --output_dir "output/chatglm_sft"
```

## 配置说明

### 1. 数据集配置 (`data/dataset_info.json`)
```json
{
  "sft_data_merged": {
    "file_name": "sft_data_merged.jsonl",
    "columns": {
      "prompt": "instruction",
      "response": "output"
    }
  }
}
```
- `file_name`: 训练数据文件名
- `columns`: 数据格式映射，`instruction`对应输入，`output`对应输出

### 2. 训练配置
`run_sft.py`会自动生成训练配置，主要参数包括：
- `model_name_or_path`: 模型路径（默认为`Qwen/Qwen2.5-7B`）
- `dataset`: 数据集名称（`sft_data_merged`）
- `finetuning_type`: 微调方式（`lora`）
- `per_device_train_batch_size`: 批量大小（4）
- `gradient_accumulation_steps`: 梯度累积步数（4）
- `learning_rate`: 学习率（5e-5）
- `num_train_epochs`: 训练轮数（3.0）

## 训练过程

1. **模型下载**：首次运行时，会自动从Hugging Face下载指定的模型
2. **数据预处理**：LLaMA-Factory会读取并预处理训练数据
3. **训练执行**：开始LoRA微调训练
4. **保存模型**：训练完成后，模型会保存在指定的输出目录

## 监控训练

- 训练过程中会输出日志，显示损失值和评估指标
- 每100步会保存一个检查点
- 训练完成后会生成损失曲线图

## 常见问题

### 1. 模型下载失败
- 确保网络连接正常
- 可以尝试使用`HF_ENDPOINT`环境变量设置国内镜像
  ```bash
export HF_ENDPOINT=https://hf-mirror.com
python scripts/run_sft.py
  ```

### 2. 显存不足
- 减小`per_device_train_batch_size`参数
- 增加`gradient_accumulation_steps`参数
- 减小`lora_rank`参数

### 3. 数据格式错误
- 确保`data/sft_data_merged.jsonl`文件格式正确
- 每行应该是一个包含`instruction`和`output`字段的JSON对象

## 训练完成后

训练完成后，模型会保存在`output/recipe_sft/`目录中，可以：
1. 使用`scripts/evaluate_model.py`评估模型性能
2. 使用`scripts/deploy_app.py`部署Web界面

## 示例输出

```
🚀 正在启动 LLaMA-Factory 训练进程...
✅ 配置文件已就绪: output/recipe_sft/sft_config.yaml
Loading checkpoint shards: 100%|██████████| 8/8 [00:15<00:00,  1.93s/it]
***** Running training *****  
  Num examples = 1000
  Num Epochs = 3
  Instantaneous batch size per device = 4
  Total train batch size (w. parallel, distributed & accumulation) = 16
  Gradient Accumulation steps = 4
  Total optimization steps = 188

Epoch 0:  10%|█         | 19/188 [01:00<09:00,  3.16s/it, loss=1.234]
```
