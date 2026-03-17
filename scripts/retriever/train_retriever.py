"""
RAG Retriever Training Script
基于 BERT 的双编码器对比学习检索器训练
"""

import os
import json
import argparse
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import BertModel, BertTokenizer
from tqdm import tqdm
import random
import numpy as np


def set_seed(seed=42):
    """设置随机种子"""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


class RecipeDataset(Dataset):
    """菜谱检索数据集"""

    def __init__(self, data_path, tokenizer, max_query_len=128, max_doc_len=512):
        self.data = []
        self.tokenizer = tokenizer
        self.max_query_len = max_query_len
        self.max_doc_len = max_doc_len

        # 加载数据
        print(f"Loading data from {data_path}...")
        with open(data_path, 'r', encoding='utf-8') as f:
            for line in f:
                item = json.loads(line.strip())
                self.data.append(item)

        print(f"Loaded {len(self.data)} samples")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        query = item['instruction']
        doc = item['output']

        # Tokenize query
        query_encoding = self.tokenizer(
            query,
            max_length=self.max_query_len,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        # Tokenize doc
        doc_encoding = self.tokenizer(
            doc,
            max_length=self.max_doc_len,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        return {
            'query_input_ids': query_encoding['input_ids'].squeeze(0),
            'query_attention_mask': query_encoding['attention_mask'].squeeze(0),
            'doc_input_ids': doc_encoding['input_ids'].squeeze(0),
            'doc_attention_mask': doc_encoding['attention_mask'].squeeze(0),
        }


class BiEncoder(nn.Module):
    """双编码器模型 - Query 和 Doc 共享 BERT 编码器"""

    def __init__(self, model_name='bert-base-chinese', hidden_dim=768):
        super().__init__()
        self.bert = BertModel.from_pretrained(model_name)
        self.hidden_dim = hidden_dim

        # 投影层，将 BERT 输出投影到统一向量空间
        self.projection = nn.Linear(hidden_dim, hidden_dim)

    def encode_query(self, input_ids, attention_mask):
        """编码查询"""
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        # 使用 [CLS] 向量
        cls_output = outputs.last_hidden_state[:, 0, :]
        # 投影并 L2 归一化
        projected = self.projection(cls_output)
        return nn.functional.normalize(projected, p=2, dim=1)

    def encode_doc(self, input_ids, attention_mask):
        """编码文档"""
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        # 使用 [CLS] 向量
        cls_output = outputs.last_hidden_state[:, 0, :]
        # 投影并 L2 归一化
        projected = self.projection(cls_output)
        return nn.functional.normalize(projected, p=2, dim=1)

    def forward(self, query_input_ids, query_attention_mask, doc_input_ids, doc_attention_mask):
        """前向传播"""
        query_embeds = self.encode_query(query_input_ids, query_attention_mask)
        doc_embeds = self.encode_doc(doc_input_ids, doc_attention_mask)
        return query_embeds, doc_embeds


class ContrastiveLoss(nn.Module):
    """对比学习损失 (InfoNCE)"""

    def __init__(self, temperature=0.07):
        super().__init__()
        self.temperature = temperature

    def forward(self, query_embeds, doc_embeds):
        """
        计算对比损失
        query_embeds: (batch_size, hidden_dim)
        doc_embeds: (batch_size, hidden_dim)
        """
        # 计算相似度矩阵
        logits = torch.matmul(query_embeds, doc_embeds.T) / self.temperature
        # 对角线为正样本
        labels = torch.arange(len(query_embeds), device=query_embeds.device)

        loss = nn.CrossEntropyLoss()(logits, labels)
        return loss


def train(args):
    """训练函数"""
    set_seed(args.seed)

    # 设置设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    # 加载 tokenizer
    print(f"Loading tokenizer: {args.model_name}")
    tokenizer = BertTokenizer.from_pretrained(args.model_name)

    # 加载数据集
    dataset = RecipeDataset(
        data_path=args.data_path,
        tokenizer=tokenizer,
        max_query_len=args.max_query_len,
        max_doc_len=args.max_doc_len
    )

    dataloader = DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=args.num_workers
    )

    # 初始化模型
    model = BiEncoder(model_name=args.model_name, hidden_dim=args.hidden_dim)
    model = model.to(device)

    # 初始化优化器和学习率调度器
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, weight_decay=args.weight_decay)

    # 损失函数
    criterion = ContrastiveLoss(temperature=args.temperature)

    # 训练循环
    print("\n" + "="*50)
    print("Starting training...")
    print("="*50)

    global_step = 0
    for epoch in range(args.num_epochs):
        model.train()
        epoch_loss = 0.0

        progress_bar = tqdm(dataloader, desc=f"Epoch {epoch+1}/{args.num_epochs}")

        for batch in progress_bar:
            # 将数据移到设备
            query_input_ids = batch['query_input_ids'].to(device)
            query_attention_mask = batch['query_attention_mask'].to(device)
            doc_input_ids = batch['doc_input_ids'].to(device)
            doc_attention_mask = batch['doc_attention_mask'].to(device)

            # 前向传播
            query_embeds, doc_embeds = model(
                query_input_ids, query_attention_mask,
                doc_input_ids, doc_attention_mask
            )

            # 计算损失
            loss = criterion(query_embeds, doc_embeds)

            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)
            optimizer.step()

            # 记录
            epoch_loss += loss.item()
            global_step += 1

            progress_bar.set_postfix({'loss': f'{loss.item():.4f}'})

            # 定期保存
            if global_step % args.save_steps == 0:
                save_path = os.path.join(args.output_dir, f'checkpoint-{global_step}')
                os.makedirs(save_path, exist_ok=True)
                torch.save(model.state_dict(), os.path.join(save_path, 'model.pt'))
                print(f"\nSaved checkpoint to {save_path}")

        avg_loss = epoch_loss / len(dataloader)
        print(f"Epoch {epoch+1} - Average Loss: {avg_loss:.4f}")

    # 保存最终模型
    os.makedirs(args.output_dir, exist_ok=True)
    final_path = os.path.join(args.output_dir, 'retriever_model.pt')
    torch.save(model.state_dict(), final_path)
    print(f"\nTraining completed! Model saved to {final_path}")

    # 保存配置文件
    config = {
        'model_name': args.model_name,
        'hidden_dim': args.hidden_dim,
        'max_query_len': args.max_query_len,
        'max_doc_len': args.max_doc_len,
    }
    with open(os.path.join(args.output_dir, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    print(f"Config saved to {os.path.join(args.output_dir, 'config.json')}")


def main():
    parser = argparse.ArgumentParser(description='Train RAG Retriever')
    parser.add_argument('--data_path', type=str, default='data/sft_data_merged.jsonl',
                        help='Path to training data')
    parser.add_argument('--model_name', type=str, default='bert-base-chinese',
                        help='Pretrained model name')
    parser.add_argument('--output_dir', type=str, default='output/retriever',
                        help='Output directory')
    parser.add_argument('--batch_size', type=int, default=16,
                        help='Batch size')
    parser.add_argument('--num_epochs', type=int, default=3,
                        help='Number of epochs')
    parser.add_argument('--learning_rate', type=float, default=2e-5,
                        help='Learning rate')
    parser.add_argument('--weight_decay', type=float, default=0.01,
                        help='Weight decay')
    parser.add_argument('--max_grad_norm', type=float, default=1.0,
                        help='Max gradient norm')
    parser.add_argument('--temperature', type=float, default=0.07,
                        help='Temperature for contrastive loss')
    parser.add_argument('--hidden_dim', type=int, default=768,
                        help='Hidden dimension')
    parser.add_argument('--max_query_len', type=int, default=128,
                        help='Max query length')
    parser.add_argument('--max_doc_len', type=int, default=512,
                        help='Max document length')
    parser.add_argument('--save_steps', type=int, default=500,
                        help='Save checkpoint every N steps')
    parser.add_argument('--num_workers', type=int, default=2,
                        help='Number of dataloader workers')
    parser.add_argument('--seed', type=int, default=42,
                        help='Random seed')

    args = parser.parse_args()
    train(args)


if __name__ == '__main__':
    main()
