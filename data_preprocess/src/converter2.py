import json
import os
import re
from uuid import uuid4
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def clean_markdown_content(content):
    """
    清洗Markdown内容
    :param content: 原始Markdown文本
    :return: 清洗后的文本
    """
    # 1. 删除页码标记（如 "### 第1页"）
    content = re.sub(r'###\s*第\d+页\s*\n', '', content)
    
    # 2. 将星号难度转换为文字描述（如 ★★★ → 3星）
    content = re.sub(r'预估烹饪难度：★+', lambda m: f"预估烹饪难度：{len(m.group(0).split('：')[1])}星", content)
    
    # 3. 删除固定的免责声明
    content = re.sub(r'\n\n如果您遵循本指南的制作流程而发现有问题或可以改进的流程，请提出 Issue 或 Pull request 。', '', content)
    
    # 4. 删除多余空行（保留段落间的单个空行）
    lines = content.splitlines()
    cleaned_lines = []
    prev_empty = False
    
    for line in lines:
        line_stripped = line.strip()
        if line_stripped:
            cleaned_lines.append(line_stripped)
            prev_empty = False
        elif not prev_empty:
            cleaned_lines.append("")
            prev_empty = True
    
    # 5. 合并结果
    content = "\n".join(cleaned_lines).strip()
    
    return content

def get_doc_type_from_folder(folder_name):
    """
    根据文件夹名称推断文档类型
    """
    type_mapping = {
        "菜谱-半成品加工": "菜谱-半成品加工",
        "菜谱-荤菜": "菜谱-荤菜",
        "菜谱-酱料": "菜谱-酱料",
        "菜谱-水产": "菜谱-水产",
        "菜谱-素菜": "菜谱-素菜",
        "菜谱-汤与粥": "菜谱-汤与粥",
        "菜谱-甜品": "菜谱-甜品",
        "菜谱-饮料": "菜谱-饮料",
        "菜谱-早餐": "菜谱-早餐",
        "菜谱-主食": "菜谱-主食",
        "菜谱-template": "菜谱-template",
        "搭建环境": "搭建环境",
        "进阶知识": "进阶知识"
    }
    
    for key, value in type_mapping.items():
        if key in folder_name:
            return value
    return "未知"

def md_to_jsonl(md_dir, jsonl_save_path, doc_type=None, language="中文"):
    """
    把MD文件夹里的所有文件转成一个JSONL
    :param md_dir: MD文件所在文件夹（如"md_docs/python_docs_md/"）
    :param jsonl_save_path: 输出JSONL路径（如"corpus_python_docs.jsonl"）
    :param doc_type: 文档类型（如"教程"、"参考"等）
    :param language: 文档语言（默认"中文"）
    """
    if not os.path.exists(md_dir):
        logger.error(f"文件夹不存在：{md_dir}")
        return 0
    
    md_files = [f for f in os.listdir(md_dir) if f.endswith(".md")]
    if not md_files:
        logger.warning(f"文件夹中没有MD文件：{md_dir}")
        return 0
    
    # 如果没有指定文档类型，从文件夹名推断
    if doc_type is None:
        doc_type = get_doc_type_from_folder(md_dir)
    
    processed_count = 0
    
    with open(jsonl_save_path, "w", encoding="utf-8") as jsonl_f:
        for md_file in md_files:
            md_path = os.path.join(md_dir, md_file)
            
            try:
                # 1. 读取MD内容
                with open(md_path, "r", encoding="utf-8") as md_f:
                    content = md_f.read().strip()
                
                # 2. 清洗内容
                content = clean_markdown_content(content)
                
                if not content:
                    logger.warning(f"跳过空文件：{md_file}")
                    continue
                
                # 3. 构建元数据
                doc_id = str(uuid4())[:8]
                metadata = {
                    "title": os.path.splitext(md_file)[0],  # 文件名作为标题
                    "source": md_path,                       # 文件路径
                    "recpie_type": doc_type,                # 菜谱类型
                    "length": len(content)                  # 字符串长度
                }
                
                # 4. 写入JSONL（每行一个JSON对象）
                json_obj = {
                    "doc_id": doc_id,
                    "content": content,
                    "metadata": metadata
                }
                jsonl_f.write(json.dumps(json_obj, ensure_ascii=False) + "\n")
                processed_count += 1
            
            except Exception as e:
                logger.error(f"处理 {md_file} 失败：{e}")
                continue
    
    logger.info(f"✓ MD转JSONL完成：{jsonl_save_path}，共处理 {processed_count} 个文件")
    return processed_count

def batch_convert_mds(md_base_dir="md_docs", output_dir="jsonl_corpus"):
    """
    批量处理多个MD文件夹，每个文件夹生成一个JSONL文件
    :param md_base_dir: MD文件基础目录
    :param output_dir: JSONL输出目录
    """
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists(md_base_dir):
        logger.error(f"MD基础目录不存在：{md_base_dir}")
        return
    
    # 获取所有MD子文件夹
    md_folders = [f for f in os.listdir(md_base_dir) 
                  if os.path.isdir(os.path.join(md_base_dir, f))]
    
    if not md_folders:
        logger.warning(f"在 {md_base_dir} 中没有找到MD文件夹")
        return
    
    logger.info(f"\n{'='*60}")
    logger.info(f"开始批量转换MD到JSONL")
    logger.info(f"找到 {len(md_folders)} 个MD文件夹")
    logger.info(f"{'='*60}\n")
    
    total_files = 0
    
    for folder in md_folders:
        md_dir = os.path.join(md_base_dir, folder)
        jsonl_filename = f"corpus_{folder.replace('_md', '')}.jsonl"
        jsonl_save_path = os.path.join(output_dir, jsonl_filename)
        
        logger.info(f"处理：{folder} -> {jsonl_filename}")
        count = md_to_jsonl(md_dir, jsonl_save_path)
        total_files += count
    
    # 输出统计信息
    logger.info(f"\n{'='*60}")
    logger.info(f"批量转换完成！")
    logger.info(f"总共处理：{total_files} 个文档")
    logger.info(f"输出目录：{os.path.abspath(output_dir)}")
    logger.info(f"{'='*60}")

if __name__ == "__main__":
    # 批量转换所有MD文件夹
    batch_convert_mds(md_base_dir="md_docs/howtocook", output_dir="jsonl_corpus/howtocook4")