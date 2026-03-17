"""
Build FAISS Index Script
使用训练好的检索器模型构建 FAISS 向量索引
"""

import os
import json
import argparse
import torch
import numpy as np
import faiss
from transformers import BertModel, BertTokenizer
from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader


class DocumentDataset(Dataset):
    """文档数据集 - 用于批量编码"""

    def __init__(self, data_path, tokenizer, max_len=512, batch_size=32):
        self.data = []
        self.tokenizer = tokenizer
        self.max_len = max_len
        self.batch_size = batch_size

        # 加载数据
        print(f"Loading documents from {data_path}...")
        with open(data_path, 'r', encoding='utf-8') as f:
            for line in f:
                item = json.loads(line.strip())
                self.data.append(item)

        print(f"Loaded {len(self.data)} documents")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        doc = item['output']

        encoding = self.tokenizer(
            doc,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encoding['input_ids'].squeeze(0),
            'attention_mask': encoding['attention_mask'].squeeze(0),
            'text': doc[:200],  # 保存文本摘要用于显示
            'instruction': item['instruction']
        }


class BiEncoder:
    """双编码器推理类"""

    def __init__(self, model_path, model_name='bert-base-chinese', device=None):
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = BertTokenizer.from_pretrained(model_name)

        # 加载模型
        print(f"Loading model from {model_path}...")
        self.model = BertModel.from_pretrained(model_name)
        self.projection = torch.nn.Linear(768, 768)

        # 加载训练好的权重
        state_dict = torch.load(model_path, map_location=self.device)
        self.model.load_state_dict(state_dict.get('bert', state_dict))
        # 尝试加载 projection 层
        if 'projection.weight' in state_dict:
            self.projection.load_state_dict({
                'weight': state_dict['projection.weight'],
                'bias': state_dict.get('projection.bias', torch.zeros(768))
            })

        self.model = self.model.to(self.device)
        self.model.eval()

    @torch.no_grad()
    def encode(self, input_ids, attention_mask):
        """编码向量"""
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = outputs.last_hidden_state[:, 0, :]
        projected = self.projection(cls_output)
        return torch.nn.functional.normalize(projected, p=2, dim=1)


def build_index(args):
    """构建 FAISS 索引"""
    # 初始化编码器
    encoder = BiEncoder(
        model_path=args.model_path,
        model_name=args.model_name,
        device=args.device
    )

    # 加载文档数据
    tokenizer = BertTokenizer.from_pretrained(args.model_name)
    dataset = DocumentDataset(
        data_path=args.data_path,
        tokenizer=tokenizer,
        max_len=args.max_doc_len,
        batch_size=args.batch_size
    )

    dataloader = DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=args.num_workers
    )

    # 编码所有文档
    print("\nEncoding documents...")
    all_embeddings = []

    for batch in tqdm(dataloader, desc="Encoding"):
        input_ids = batch['input_ids'].to(encoder.device)
        attention_mask = batch['attention_mask'].to(encoder.device)

        embeddings = encoder.encode(input_ids, attention_mask)
        all_embeddings.append(embeddings.cpu().numpy())

    # 合并所有 embedding
    all_embeddings = np.vstack(all_embeddings).astype('float32')
    print(f"Encoded {len(all_embeddings)} documents, shape: {all_embeddings.shape}")

    # 构建 FAISS 索引
    print("\nBuilding FAISS index...")

    if args.index_type == 'flat':
        # 精确搜索 (适合小数据集)
        index = faiss.IndexFlatIP(args.hidden_dim)  # Inner Product (余弦相似度，因为向量已经归一化)
    elif args.index_type == 'ivf':
        # 倒排索引 (适合大数据集)
        quantizer = faiss.IndexFlatIP(args.hidden_dim)
        index = faiss.IndexIVFFlat(quantizer, args.hidden_dim, args.nlist)
        index.train(all_embeddings)
        index.add(all_embeddings)
    else:
        raise ValueError(f"Unknown index type: {args.index_type}")

    if args.index_type == 'flat':
        index.add(all_embeddings)

    print(f"Index built! Total vectors: {index.ntotal}")

    # 保存索引
    os.makedirs(args.output_dir, exist_ok=True)
    index_path = os.path.join(args.output_dir, 'faiss_index.bin')
    faiss.write_index(index, index_path)
    print(f"Index saved to {index_path}")

    # 保存文档元数据
    metadata = []
    for item in dataset.data:
        metadata.append({
            'instruction': item['instruction'],
            'doc_preview': item['output'][:300]  # 保存预览文本
        })

    metadata_path = os.path.join(args.output_dir, 'metadata.json')
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    print(f"Metadata saved to {metadata_path}")

    # 保存配置
    config = {
        'model_path': args.model_path,
        'model_name': args.model_name,
        'data_path': args.data_path,
        'num_documents': len(dataset.data),
        'embedding_dim': args.hidden_dim,
        'index_type': args.index_type,
    }

    config_path = os.path.join(args.output_dir, 'index_config.json')
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    print(f"Config saved to {config_path}")

    print("\n" + "="*50)
    print("Index building completed!")
    print("="*50)


def main():
    parser = argparse.ArgumentParser(description='Build FAISS Index')
    parser.add_argument('--data_path', type=str, default='data/sft_data_merged.jsonl',
                        help='Path to document data')
    parser.add_argument('--model_path', type=str, default='output/retriever/retriever_model.pt',
                        help='Path to trained retriever model')
    parser.add_argument('--model_name', type=str, default='bert-base-chinese',
                        help='Pretrained model name')
    parser.add_argument('--output_dir', type=str, default='index/retriever',
                        help='Output directory for index')
    parser.add_argument('--index_type', type=str, default='flat', choices=['flat', 'ivf'],
                        help='Type of FAISS index')
    parser.add_argument('--nlist', type=int, default=100,
                        help='Number of clusters for IVF index')
    parser.add_argument('--hidden_dim', type=int, default=768,
                        help='Embedding dimension')
    parser.add_argument('--max_doc_len', type=int, default=512,
                        help='Max document length')
    parser.add_argument('--batch_size', type=int, default=32,
                        help='Batch size for encoding')
    parser.add_argument('--num_workers', type=int, default=2,
                        help='Number of dataloader workers')
    parser.add_argument('--device', type=str, default=None,
                        help='Device to use (cuda/cpu)')

    args = parser.parse_args()
    build_index(args)


if __name__ == '__main__':
    main()
