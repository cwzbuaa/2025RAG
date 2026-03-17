"""
Retrieve Script
基于 FAISS 索引的检索功能
"""

import os
import json
import argparse
import torch
import numpy as np
import faiss
from transformers import BertModel, BertTokenizer


class Retriever:
    """检索器类"""

    def __init__(self, index_dir, device=None):
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')

        # 加载配置
        config_path = os.path.join(index_dir, 'index_config.json')
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        # 加载模型
        print(f"Loading model from {self.config['model_path']}...")
        self.tokenizer = BertTokenizer.from_pretrained(self.config['model_name'])
        self.model = BertModel.from_pretrained(self.config['model_name'])
        self.projection = torch.nn.Linear(768, 768)

        # 加载训练好的权重
        state_dict = torch.load(self.config['model_path'], map_location=self.device)
        self.model.load_state_dict(state_dict.get('bert', state_dict))
        if 'projection.weight' in state_dict:
            self.projection.load_state_dict({
                'weight': state_dict['projection.weight'],
                'bias': state_dict.get('projection.bias', torch.zeros(768))
            })

        self.model = self.model.to(self.device)
        self.model.eval()

        # 加载 FAISS 索引
        index_path = os.path.join(index_dir, 'faiss_index.bin')
        print(f"Loading index from {index_path}...")
        self.index = faiss.read_index(index_path)

        # 加载元数据
        metadata_path = os.path.join(index_dir, 'metadata.json')
        with open(metadata_path, 'r', encoding='utf-8') as f:
            self.metadata = json.load(f)

        print(f"Loaded index with {self.index.ntotal} documents")

    @torch.no_grad()
    def encode_query(self, query):
        """编码查询"""
        encoding = self.tokenizer(
            query,
            max_length=128,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        input_ids = encoding['input_ids'].to(self.device)
        attention_mask = encoding['attention_mask'].to(self.device)

        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = outputs.last_hidden_state[:, 0, :]
        projected = self.projection(cls_output)
        embedding = torch.nn.functional.normalize(projected, p=2, dim=1)

        return embedding.cpu().numpy().astype('float32')

    def retrieve(self, query, top_k=5):
        """检索相关文档"""
        # 编码查询
        query_embedding = self.encode_query(query)

        # 搜索
        distances, indices = self.index.search(query_embedding, top_k)

        # 整理结果
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx >= 0:  # 有效的索引
                results.append({
                    'rank': len(results) + 1,
                    'index': int(idx),
                    'score': float(distance),
                    'instruction': self.metadata[idx]['instruction'],
                    'doc_preview': self.metadata[idx]['doc_preview']
                })

        return results


def interactive_search(retriever):
    """交互式搜索"""
    print("\n" + "="*50)
    print("Interactive Recipe Search")
    print("="*50)
    print("Enter your query (e.g., '我有土豆和番茄，能做什么菜？')")
    print("Type 'quit' or 'exit' to exit")
    print("="*50 + "\n")

    while True:
        query = input("\nQuery: ").strip()

        if query.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break

        if not query:
            continue

        results = retriever.retrieve(query, top_k=5)

        print("\n" + "-"*50)
        print(f"Top {len(results)} Results:")
        print("-"*50)

        for r in results:
            print(f"\n[Rank {r['rank']}] Score: {r['score']:.4f}")
            print(f"Query: {r['instruction']}")
            print(f"Preview: {r['doc_preview'][:150]}...")


def main():
    parser = argparse.ArgumentParser(description='Retrieve Recipes')
    parser.add_argument('--index_dir', type=str, default='index/retriever',
                        help='Directory containing FAISS index')
    parser.add_argument('--query', type=str, default=None,
                        help='Query string')
    parser.add_argument('--top_k', type=int, default=5,
                        help='Number of results to return')
    parser.add_argument('--interactive', action='store_true',
                        help='Interactive search mode')

    args = parser.parse_args()

    # 初始化检索器
    retriever = Retriever(args.index_dir)

    if args.interactive:
        interactive_search(retriever)
    elif args.query:
        results = retriever.retrieve(args.query, top_k=args.top_k)

        print("\n" + "="*50)
        print(f"Query: {args.query}")
        print(f"Top {len(results)} Results:")
        print("="*50)

        for r in results:
            print(f"\n[Rank {r['rank']}] Score: {r['score']:.4f}")
            print(f"Query: {r['instruction']}")
            print(f"Preview: {r['doc_preview'][:200]}...")
            print("-"*50)
    else:
        # 默认交互模式
        interactive_search(retriever)


if __name__ == '__main__':
    main()
