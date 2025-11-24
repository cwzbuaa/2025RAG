import json
import re

def replace_recipe_titles_in_jsonl(input_file, output_file, target_chunk_suffix="_chunk1"):
    """
    在JSONL文件中查找所有chunk_id以"_chunk1"结尾的json数据，
    把child_content字段中的"# xxxx的做法"换成"## 简介"
    
    Args:
        input_file: 输入JSONL文件路径
        output_file: 输出JSONL文件路径
        target_chunk_suffix: 目标chunk_id的后缀
    """
    processed_count = 0
    pattern = r'# (.+)的做法'
    
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        for line_num, line in enumerate(infile, 1):
            try:
                data = json.loads(line.strip())
                
                # 检查chunk_id是否以指定后缀结尾
                chunk_id = data.get('chunk_id', '')
                if chunk_id.endswith(target_chunk_suffix):
                    # 替换child_content中的文本
                    if 'child_content' in data and isinstance(data['child_content'], str):
                        old_content = data['child_content']
                        
                        # 使用正则表达式替换所有"# 菜名做法"为"## 简介"
                        new_content = re.sub(pattern, '## 简介', data['child_content'])
                        
                        if old_content != new_content:
                            data['child_content'] = new_content
                            processed_count += 1
                            print(f"第 {line_num} 行 (chunk_id: {chunk_id}): 已替换标题")
                
                # 写入输出文件
                outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
                
            except json.JSONDecodeError as e:
                print(f"警告: 第 {line_num} 行JSON解析错误: {e}")
                outfile.write(line)
    
    print(f"\n处理完成! 共替换了 {processed_count} 条记录")
    print(f"输入文件: {input_file}")
    print(f"输出文件: {output_file}")

# 使用示例
if __name__ == "__main__":
    input_filename = "chunked_corpus/howtocook3.jsonl"      # 输入文件路径
    output_filename = "chunked_corpus/howtocook4.jsonl"    # 输出文件路径
    
    replace_recipe_titles_in_jsonl(input_filename, output_filename)