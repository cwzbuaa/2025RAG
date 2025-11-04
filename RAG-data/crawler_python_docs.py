# Python 官方文档爬虫 - 将教程页面转换为 PDF

import asyncio
import os
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import requests
import time

# 配置
BASE_URL = "https://docs.python.org/zh-cn/3.14/tutorial/"
INDEX_URL = BASE_URL + "index.html"
SAVE_DIR = "python_docs_pdf"

# 创建保存目录
os.makedirs(SAVE_DIR, exist_ok=True)

def get_tutorial_links():
    """
    从目录页提取所有教程链接
    :return: [(章节编号, 标题, 链接文件名), ...]
    """
    print(f"正在获取目录页：{INDEX_URL}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(INDEX_URL, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        
        # 定位目录结构
        toctree = soup.find("div", class_="toctree-wrapper")
        if not toctree:
            print("未找到目录结构")
            return []
        
        # 提取所有一级章节链接（toctree-l1）
        links = []
        for item in toctree.find_all("li", class_="toctree-l1"):
            link_tag = item.find("a", class_="reference internal")
            if link_tag and link_tag.get("href"):
                href = link_tag.get("href")
                title = link_tag.get_text(strip=True)
                
                # 提取章节编号（如果有）
                match = re.match(r"^(\d+)\.\s+(.+)$", title)
                if match:
                    chapter_num = match.group(1).zfill(2)  # 补零，如 01, 02
                    chapter_title = match.group(2)
                else:
                    chapter_num = "00"
                    chapter_title = title
                
                links.append((chapter_num, chapter_title, href))
        
        print(f"找到 {len(links)} 个教程章节")
        return links
    
    except Exception as e:
        print(f"获取目录页失败：{e}")
        return []

def sanitize_filename(filename):
    """
    清理文件名，去除特殊字符
    """
    # 移除或替换不允许的字符
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = filename.replace(" ", "_")
    return filename

async def save_page_as_pdf(page, url, save_path):
    """
    使用 Playwright 将页面保存为 PDF
    """
    try:
        print(f"  正在访问：{url}")
        await page.goto(url, wait_until="networkidle", timeout=30000)
        
        # 等待主要内容加载
        await page.wait_for_selector(".body", timeout=10000)
        
        # 保存为 PDF
        await page.pdf(
            path=save_path,
            format="A4",
            margin={
                "top": "20mm",
                "right": "20mm",
                "bottom": "20mm",
                "left": "20mm"
            },
            print_background=True  # 保留背景色和图片
        )
        
        print(f"  ✓ 已保存：{save_path}")
        return True
    
    except Exception as e:
        print(f"  ✗ 保存失败：{e}")
        return False

async def main():
    """
    主函数：批量下载所有教程页面为 PDF
    """
    # 1. 获取所有教程链接
    tutorial_links = get_tutorial_links()
    
    if not tutorial_links:
        print("没有找到教程链接，退出")
        return
    
    print(f"\n开始下载 {len(tutorial_links)} 个教程页面...\n")
    
    # 2. 使用 Playwright 批量转换
    async with async_playwright() as p:
        # 启动浏览器（使用 chromium）
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        success_count = 0
        fail_count = 0
        
        for idx, (chapter_num, title, href) in enumerate(tutorial_links, 1):
            # 构建完整 URL
            full_url = BASE_URL + href
            
            # 构建保存文件名
            safe_title = sanitize_filename(title)
            pdf_filename = f"{chapter_num}_{safe_title}.pdf"
            pdf_path = os.path.join(SAVE_DIR, pdf_filename)
            
            print(f"[{idx}/{len(tutorial_links)}] {chapter_num}. {title}")
            
            # 保存为 PDF
            success = await save_page_as_pdf(page, full_url, pdf_path)
            
            if success:
                success_count += 1
            else:
                fail_count += 1
            
            # 延时，避免请求过快
            if idx < len(tutorial_links):
                await asyncio.sleep(1.5)
        
        await browser.close()
    
    # 3. 输出统计信息
    print(f"\n{'='*50}")
    print(f"下载完成！")
    print(f"成功：{success_count} 个")
    print(f"失败：{fail_count} 个")
    print(f"保存路径：{os.path.abspath(SAVE_DIR)}")
    print(f"{'='*50}")

if __name__ == "__main__":
    asyncio.run(main())
