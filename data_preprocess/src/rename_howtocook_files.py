# HowToCook 文件重命名工具
# 将URL编码的文件名改为中文标题

import os
import re
import urllib.parse

def extract_title_from_md(file_path):
    """从Markdown文件中提取第一个一级标题作为文件名"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 查找第一个一级标题（# 开头）
                if line.startswith('# '):
                    title = line[2:].strip()
                    # 清理文件名中的非法字符
                    title = re.sub(r'[<>:"/\\|?*]', '', title)
                    # 去除结尾可能的"的做法"，保持简洁
                    # title = title.replace('的做法', '')
                    return title
        return None
    except Exception as e:
        print(f"  ✗ 读取文件失败: {e}")
        return None

def rename_files_in_directory(base_dir, dry_run=True):
    """
    递归重命名目录下的所有URL编码的文件
    
    Args:
        base_dir: 基础目录
        dry_run: True时只预览，不实际重命名
    """
    renamed_list = []
    failed_list = []
    skipped_list = []
    
    print(f"\n{'='*80}")
    print(f"扫描目录: {base_dir}")
    print(f"模式: {'预览模式 (不会真正重命名)' if dry_run else '执行模式 (将真正重命名)'}")
    print(f"{'='*80}\n")
    
    for root, dirs, files in os.walk(base_dir):
        # 显示当前处理的目录
        relative_dir = os.path.relpath(root, base_dir)
        if relative_dir != '.':
            print(f"\n📁 目录: {relative_dir}")
        
        for filename in files:
            if not filename.endswith('.md'):
                continue
            
            # 检查是否是URL编码的文件名（包含%）
            if '%' not in filename:
                continue
            
            old_path = os.path.join(root, filename)
            
            # 从文件内容提取标题
            title = extract_title_from_md(old_path)
            
            if title:
                new_filename = f"{title}.md"
                new_path = os.path.join(root, new_filename)
                
                # 避免文件名冲突
                if os.path.exists(new_path) and old_path != new_path:
                    print(f"  ⚠️  跳过（目标文件已存在）:")
                    print(f"      {filename}")
                    print(f"      -> {new_filename}")
                    skipped_list.append((filename, new_filename, "目标文件已存在"))
                    continue
                
                # 预览或执行重命名
                if dry_run:
                    print(f"  👁️  预览:")
                    print(f"      {filename}")
                    print(f"      -> {new_filename}")
                    renamed_list.append((filename, new_filename))
                else:
                    try:
                        os.rename(old_path, new_path)
                        print(f"  ✓ 成功:")
                        print(f"      {filename}")
                        print(f"      -> {new_filename}")
                        renamed_list.append((filename, new_filename))
                    except Exception as e:
                        print(f"  ✗ 失败:")
                        print(f"      {filename}")
                        print(f"      错误: {e}")
                        failed_list.append((filename, str(e)))
            else:
                # 如果无法提取标题，尝试URL解码作为备选
                try:
                    decoded_name = urllib.parse.unquote(filename)
                    if decoded_name != filename:
                        print(f"  ⚠️  无标题，使用URL解码:")
                        print(f"      {filename}")
                        print(f"      -> {decoded_name}")
                        
                        new_path = os.path.join(root, decoded_name)
                        
                        if not os.path.exists(new_path):
                            if not dry_run:
                                os.rename(old_path, new_path)
                            renamed_list.append((filename, decoded_name))
                        else:
                            skipped_list.append((filename, decoded_name, "目标文件已存在"))
                except Exception as e:
                    print(f"  ✗ 解码失败: {filename} - {e}")
                    failed_list.append((filename, str(e)))
    
    return renamed_list, failed_list, skipped_list

def print_summary(renamed_list, failed_list, skipped_list, dry_run=True):
    """打印统计摘要"""
    print(f"\n{'='*80}")
    print(f"{'预览' if dry_run else '执行'}结果统计")
    print(f"{'='*80}")
    print(f"✓ 将{'会' if dry_run else '已'}重命名: {len(renamed_list)} 个")
    print(f"⚠️  跳过: {len(skipped_list)} 个")
    print(f"✗ 失败: {len(failed_list)} 个")
    print(f"{'='*80}")
    
    if skipped_list:
        print("\n跳过的文件:")
        for old, new, reason in skipped_list:
            print(f"  - {old} ({reason})")
    
    if failed_list:
        print("\n失败的文件:")
        for filename, error in failed_list:
            print(f"  - {filename}: {error}")

if __name__ == "__main__":
    base_dir = "md_docs/howtocook"
    
    print("="*80)
    print("HowToCook 文件重命名工具")
    print("="*80)
    
    if not os.path.exists(base_dir):
        print(f"❌ 错误：目录不存在 {base_dir}")
        exit(1)
    
    # 第一步：预览模式
    print("\n第一步：预览重命名结果...")
    renamed, failed, skipped = rename_files_in_directory(base_dir, dry_run=True)
    print_summary(renamed, failed, skipped, dry_run=True)
    
    # 询问是否执行
    if renamed or failed:
        print(f"\n{'='*80}")
        response = input("是否执行重命名？(输入 yes 确认): ").strip().lower()
        
        if response in ['yes', 'y', '是']:
            print("\n第二步：执行重命名...")
            renamed, failed, skipped = rename_files_in_directory(base_dir, dry_run=False)
            print_summary(renamed, failed, skipped, dry_run=False)
            print(f"\n✅ 重命名完成！")
        else:
            print("\n❌ 已取消重命名操作")
    else:
        print("\n✅ 没有需要重命名的文件")

