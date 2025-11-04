## 说明

目前实现了多个爬虫代码，从python的官方文档进行爬取，

```
如果想要更改其他领域的文档，需要做：

1、写专属于他的爬虫，并且记录保存的文件夹路径

2、在convert1的110行将文件夹路径添加进去

3、运行splitter，第一次运行需要魔法下载多语言模型，大约400M
```
introduce文件为微信里发的那个步骤流程

html结构文件夹为爬取的页面的html结构，不用管

chunked_corpus文件夹下为分块结果以及分块报告，此文件夹下新创建了howtocook文件夹

docs_pdf文件夹下为python官方的英文文档，内容较多

jsonl_corpus为从md转换到jsonl的目标目录，此文件夹下新创建了howtocook文件夹

md_docs为从pdf转换到md的目标目录，，此文件夹下新创建了howtocook文件夹

其他带有pdf后标的为爬取到的中文pdf文档
爬取了 7 个文档板块的 PDF：
- `python_docs_pdf/` - Python 教程
- `python_reference_pdf/` - Python 语言参考
- `python_library_pdf/` - Python 标准库
- `python_howto_pdf/` - Python 指南
- `python_faq_pdf/` - 常见问题
- `python_extending_pdf/` - 扩展和嵌入
- `python_c-api_pdf/` - C API
- `docs-pdf/` - 英文官方文档（可选）

运行流程：
1、爬取文档或者下载文档

此处改为运行crawer_howtocook.py，下载好后运行rename文件将下载的文件进行重命名

2、，配置好converter1的文件夹后，使用converter1 和 converter2 进行转换

3、使用splitter进行分块即可

## 未完成

第四步准备测评数据集没有完成，因为需要和评测组进行对接



## 环境配置

### 首次运行需要安装依赖
```bash
pip install -r requirements.txt
playwright install
```


## 项目结构



### 数据转换

#### converter1.py - PDF 转 Markdown
**功能：** 将 PDF 文档批量转换为 Markdown 格式


**使用方法：**
```bash
python converter1.py
```

**输出：** `md_docs/` 目录下的各个子文件夹

#### converter2.py - Markdown 转 JSONL
**功能：** 将 Markdown 文档转换为 JSONL 格式（RAG 系统标准输入）

**使用方法：**
```bash
python converter2.py
```

**输出：** `jsonl_corpus/` 目录下的各个 JSONL 文件



## 爬虫代码说明

### 爬虫文件列表
- `crawler_python_docs.py` - Python 教程
- `crawler_python_reference.py` - Python 语言参考
- `crawler_python_library.py` - Python 标准库
- `crawler_python_howto.py` - Python 指南（使用特殊解析逻辑）
- `crawler_python_faq.py` - 常见问题
- `crawler_python_extending.py` - 扩展和嵌入
- `crawler_python_c-api.py` - C API
- `crawler_howtocook.py` - HowToCook程序员做饭指南（直接保存Markdown）

### HowToCook 爬虫使用说明

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

### Python文档流程
```
PDF 文档 → Markdown → JSONL → 分块 → RAG 系统
   ↓           ↓         ↓        ↓
crawler    converter1  converter2  splitter
```

### HowToCook流程
```
GitHub → Markdown → JSONL → 分块 → RAG 系统
   ↓          ↓         ↓        ↓
crawler  (直接保存)  converter2  splitter
```

