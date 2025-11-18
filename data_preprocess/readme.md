# 说明
### 首次运行需要安装依赖
```bash
pip install -r requirements.txt
playwright install
```

## HowToCook 爬虫使用说明

**功能：** 爬取GitHub上的HowToCook项目（程序员做饭指南）

**爬取内容：**
1. 搭建环境模块（厨房准备、工具使用、烹饪技巧等14个文件）
2. 菜谱模块（素菜、荤菜、水产、早餐、主食等10大分类，排除按难度索引）
3. 进阶知识（辅料技巧、高级术语、糖色炒制、油温判断）

**使用方法：**
```bash
python crawler_howtocook.py
```

**输出：** `md_docs/howtocook/` 目录，按分类存放：
- `搭建环境/` - 环境准备相关
- `进阶知识/` - 高级烹饪技巧
- `菜谱-素菜/` - 素菜菜谱
- `菜谱-荤菜/` - 荤菜菜谱
- `菜谱-水产/` - 水产菜谱
- 等等...


## 数据流程
```
GitHub → Markdown → JSONL → 分块 → RAG 系统
   ↓          ↓         ↓        ↓
crawler  (直接保存)  converter2  splitter
```

