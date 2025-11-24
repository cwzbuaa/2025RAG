import json

def filter_jsonl_by_metadata(input_file, output_file, exclude_types=None):
    """
    过滤 jsonl 文件，移除 metadata 中 recipe_type 为指定类型的内容，并统计数量。
    
    :param input_file: 输入 jsonl 文件路径
    :param output_file: 输出 jsonl 文件路径
    :param exclude_types: 需要排除的 recipe_type 列表
    """
    if exclude_types is None:
        exclude_types = ["搭建环境", "进阶知识"]

    total_count = 0
    kept_count = 0

    with open(input_file, "r", encoding="utf-8") as f_in, \
         open(output_file, "w", encoding="utf-8") as f_out:
        for line in f_in:
            total_count += 1
            data = json.loads(line)
            rec_type = data.get("metadata", {}).get("recpie_type")
            if rec_type not in exclude_types:
                f_out.write(json.dumps(data, ensure_ascii=False) + "\n")
                kept_count += 1

    print(f"原始数据量: {total_count}")
    print(f"保留数据量: {kept_count}")
    print(f"过滤掉的数据量: {total_count - kept_count}")
# 示例调用
input_path = "chunked_corpus/chunked_corpus.jsonl"
output_path = "chunked_corpus/chunked_corpus2.jsonl"
filter_jsonl_by_metadata(input_path, output_path)
