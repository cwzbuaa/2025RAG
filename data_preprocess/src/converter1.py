import pdfplumber
import os
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def pdf_to_md(pdf_path, save_md_dir):
    """
    把单个PDF转成Markdown
    :param pdf_path: 原始PDF路径（如"python_docs_pdf/01_课前甜点.pdf"）
    :param save_md_dir: MD文件保存文件夹（如"md_docs/"）
    """
    os.makedirs(save_md_dir, exist_ok=True)
    # 获取PDF文件名（不含后缀）
    md_filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".md"
    md_save_path = os.path.join(save_md_dir, md_filename)

    try:
        with pdfplumber.open(pdf_path) as pdf, open(md_save_path, "w", encoding="utf-8") as md_f:
            for page_num, page in enumerate(pdf.pages, 1):
                try:
                    # 1. 裁剪页面（去除页眉页脚区域）
                    # 裁剪边距：上下左右各留 50 像素
                    cropped_page = page.crop((50, 50, page.width - 50, page.height - 50))
                    
                    # 2. 提取页面文字
                    text = cropped_page.extract_text()
                    if not text or not text.strip():
                        continue  # 跳过空白页
                    
                    # 3. 提取页面表格，转成Markdown表格
                    tables = cropped_page.extract_tables()
                    if tables:
                        # 在文本末尾添加表格
                        for table in tables:
                            if table and len(table) > 0:
                                md_table = "\n\n"
                                # 表格头部
                                if table[0]:
                                    md_table += "| " + " | ".join([str(cell) if cell else "" for cell in table[0]]) + " |\n"
                                    # 表格分隔线
                                    md_table += "| " + " | ".join(["---"] * len(table[0])) + " |\n"
                                # 表格内容
                                for row in table[1:]:
                                    if row:
                                        md_table += "| " + " | ".join([str(cell) if cell else "" for cell in row]) + " |\n"
                                text += md_table
                    
                    # 4. 写入MD文件（标注页码，方便后续溯源）
                    md_f.write(f"### 第{page_num}页\n\n")
                    md_f.write(text.strip() + "\n\n")
                
                except Exception as e:
                    logger.warning(f"处理 {pdf_path} 第 {page_num} 页时出错：{e}")
                    continue
        
        logger.info(f"✓ PDF转MD完成：{md_save_path}")
        return True
    
    except Exception as e:
        logger.error(f"✗ 处理 {pdf_path} 失败：{e}")
        return False

def batch_convert_pdfs(pdf_folders, output_base_dir="md_docs"):
    """
    批量处理多个PDF文件夹
    :param pdf_folders: PDF文件夹列表（如 ["python_docs_pdf", "python_reference_pdf"]）
    :param output_base_dir: 输出基础目录
    """
    total_success = 0
    total_fail = 0
    
    for pdf_folder in pdf_folders:
        if not os.path.exists(pdf_folder):
            logger.warning(f"文件夹不存在，跳过：{pdf_folder}")
            continue
        
        # 为每个源文件夹创建对应的MD输出文件夹
        folder_name = os.path.basename(pdf_folder.rstrip('/'))
        save_md_dir = os.path.join(output_base_dir, folder_name.replace('_pdf', '_md'))
        
        logger.info(f"\n{'='*60}")
        logger.info(f"开始处理文件夹：{pdf_folder} -> {save_md_dir}")
        logger.info(f"{'='*60}")
        
        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        logger.info(f"找到 {len(pdf_files)} 个PDF文件")
        
        for idx, pdf_file in enumerate(pdf_files, 1):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            logger.info(f"[{idx}/{len(pdf_files)}] 处理：{pdf_file}")
            
            if pdf_to_md(pdf_path, save_md_dir):
                total_success += 1
            else:
                total_fail += 1
    
    # 输出统计信息
    logger.info(f"\n{'='*60}")
    logger.info(f"批量转换完成！")
    logger.info(f"成功：{total_success} 个")
    logger.info(f"失败：{total_fail} 个")
    logger.info(f"输出目录：{os.path.abspath(output_base_dir)}")
    logger.info(f"{'='*60}")

if __name__ == "__main__":
    # 定义要处理的PDF文件夹列表（中文文档）
    pdf_folders = [
        "python_docs_pdf",          # Python 教程
        "python_reference_pdf",     # Python 语言参考
        "python_library_pdf",       # Python 标准库
        "python_howto_pdf",         # Python 指南
        "python_faq_pdf",           # 常见问题
        "python_extending_pdf",     # 扩展和嵌入
        "python_c-api_pdf",         # C API
        "docs-pdf",                 # 英文官方文档（可选）
        # 注意：howtocook文件夹已经是md格式，不需要通过此脚本转换
        # 它会直接被converter2.py处理
    ]
    
    # 批量转换
    batch_convert_pdfs(pdf_folders, output_base_dir="md_docs")