import json
import os
import re

def chunk_jsonl_files(input_dir, output_file):
    """
    遍历文件夹中的所有jsonl文件，按照一级标题和二级标题进行分块
    
    :param input_dir: 输入文件夹路径
    :param output_file: 输出jsonl文件路径
    """
    # 获取所有jsonl文件
    jsonl_files = [f for f in os.listdir(input_dir) if f.endswith('.jsonl')]
    
    if not jsonl_files:
        print(f"在文件夹 {input_dir} 中未找到jsonl文件")
        return
    
    all_chunks = []
    
    for jsonl_file in jsonl_files:
        file_path = os.path.join(input_dir, jsonl_file)
        print(f"处理文件: {jsonl_file}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    # 解析JSON行
                    doc = json.loads(line.strip())
                    content = doc.get("content", "")
                    doc_id = doc.get("doc_id", "")
                    metadata = doc.get("metadata", {})
                    title = metadata.get("title", "")
                    
                    if not content:
                        continue
                    
                    # 按照一级标题和二级标题进行分块
                    chunks = split_by_headings(content)
                    
                    for c_idx, child_chunk in enumerate(chunks):
                        enhanced_child_content = f"【{title}】\n{child_chunk}"

                        chunk_obj = {
                            "doc_id": doc_id,
                            "chunk_id": f"{doc_id}_chunk{c_idx+1}",
                            "child_content": enhanced_child_content,
                            "parent_content": content,  # 保留父块内容
                            "length": len(enhanced_child_content),
                            "metadata": metadata  # 直接照抄原metadata
                        }
                        all_chunks.append(chunk_obj)
                        
                except json.JSONDecodeError as e:
                    print(f"文件 {jsonl_file} 第 {line_num} 行JSON解析错误: {e}")
                    continue
                except Exception as e:
                    print(f"处理文件 {jsonl_file} 第 {line_num} 行时发生错误: {e}")
                    continue
    
    # 将所有分块写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + '\n')
    
    print(f"分块完成！共处理 {len(jsonl_files)} 个文件，生成 {len(all_chunks)} 个分块")
    print(f"输出文件: {output_file}")

def split_by_headings(content):
    """
    只在一级(#)和二级(##)标题处切分（允许行首缩进）。
    保留代码块（fenced code block）内的内容不被切分。

    :param content: 原始文本内容（字符串）
    :return: 分块列表（每个块包含其起始标题（若有）及随后的内容）
    """
    # 匹配行首可选空白，接着1或2个#，至少一个空白，然后标题文本
    heading_pattern = re.compile(r'^\s*(#{1,2})\s+(.*)$')
    chunks = []

    lines = content.splitlines()
    current_chunk_lines = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        # 处理代码块开始/结束（保留原始行）
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            current_chunk_lines.append(line)
            continue

        # 如果在代码块内，直接加入，不做标题检测
        if in_code_block:
            current_chunk_lines.append(line)
            continue

        # 在代码块外，检测是否为一级/二级标题
        m = heading_pattern.match(line)
        if m:
            # 遇到新标题：若当前块非空，先保存当前块
            if current_chunk_lines:
                chunk_text = '\n'.join(current_chunk_lines).strip()
                if chunk_text:
                    chunks.append(chunk_text)
                current_chunk_lines = []

            # 将标题作为新块的第一行（保留原始格式）
            current_chunk_lines.append(line)
        else:
            # 普通行，累积到当前块
            current_chunk_lines.append(line)

    # 结束后把最后一块保存
    if current_chunk_lines:
        chunk_text = '\n'.join(current_chunk_lines).strip()
        if chunk_text:
            chunks.append(chunk_text)

    return chunks

# 使用示例
if __name__ == "__main__":
    input_directory = "jsonl/howtocook/test"  # 替换为您的输入文件夹路径
    output_path = "chunked_corpus/test.jsonl"  # 替换为您的输出文件路径
    
    chunk_jsonl_files(input_directory, output_path)