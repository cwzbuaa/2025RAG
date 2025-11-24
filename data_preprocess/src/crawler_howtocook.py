# HowToCook 爬虫 - 程序员做饭指南

import asyncio
import os
import re
from playwright.async_api import async_playwright
import time

# 配置
BASE_URL = "https://raw.githubusercontent.com/Anduin2017/HowToCook/master"
SAVE_DIR = "md_docs/howtocook"

# 需要爬取的文件路径（使用GitHub API获取完整路径列表）
TARGET_PATHS = {
    "搭建环境": [
        "tips/厨房准备.md",
        "tips/如何选择现在吃什么.md",
        "tips/食材相克与禁忌.md",
        "tips/learn/高压力锅.md",
        "tips/learn/空气炸锅.md",
        "tips/learn/去腥.md",
        "tips/learn/食品安全.md",
        "tips/learn/微波炉.md",
        "tips/learn/学习焯水.md",
        "tips/learn/学习炒与煎.md",
        "tips/learn/学习凉拌.md",
        "tips/learn/学习腌.md",
        "tips/learn/学习蒸.md",
        "tips/learn/学习煮.md",
    ],
    "进阶知识": [
        "tips/advanced/辅料技巧.md",
        "tips/advanced/高级专业术语.md",
        "tips/advanced/糖色的炒制.md",
        "tips/advanced/油温判断技巧.md",
    ]
}

# 菜谱分类（从主页提取的所有菜谱链接）
RECIPE_CATEGORIES = [
    "vegetable_dish",  # 素菜
    "meat_dish",       # 荤菜
    "aquatic",         # 水产
    "breakfast",       # 早餐
    "staple",          # 主食
    "semi-finished",   # 半成品加工
    "soup",            # 汤与粥
    "drink",           # 饮料
    "condiment",       # 酱料和其它材料
    "dessert"          # 甜品
]

# 创建保存目录
os.makedirs(SAVE_DIR, exist_ok=True)

def sanitize_filename(filename):
    """
    清理文件名，去除特殊字符
    """
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = filename.replace(" ", "_")
    return filename

async def get_recipe_links_from_readme(page):
    """
    从README页面获取所有菜谱链接
    """
    print("正在获取菜谱列表...")
    
    await page.goto("https://github.com/Anduin2017/HowToCook?tab=readme-ov-file", wait_until="networkidle", timeout=30000)
    await page.wait_for_selector("article", timeout=10000)
    
    # 获取所有菜谱链接
    recipe_links = []
    
    # 使用JavaScript获取所有链接
    links = await page.evaluate("""
        () => {
            const links = [];
            const article = document.querySelector('article');
            if (!article) return links;
            
            // 获取所有链接
            const allLinks = article.querySelectorAll('a[href*="/blob/master/dishes/"]');
            
            allLinks.forEach(link => {
                const href = link.getAttribute('href');
                // 排除按难度索引的链接
                if (href && !href.includes('/starsystem/') && href.includes('.md')) {
                    links.push({
                        href: href,
                        text: link.textContent.trim()
                    });
                }
            });
            
            return links;
        }
    """)
    
    print(f"找到 {len(links)} 个菜谱链接")
    return links

async def download_markdown_from_github(page, file_path, save_path):
    """
    从GitHub获取原始Markdown内容
    """
    try:
        # 构建raw.githubusercontent.com URL
        raw_url = f"https://raw.githubusercontent.com/Anduin2017/HowToCook/master/{file_path}"
        
        print(f"  访问：{raw_url}")
        await page.goto(raw_url, wait_until="networkidle", timeout=30000)
        
        # 获取页面文本内容
        content = await page.evaluate("() => document.body.textContent")
        
        if content and content.strip():
            # 保存Markdown文件
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(content.strip())
            print(f"  ✓ 已保存：{save_path}")
            return True
        else:
            print(f"  ✗ 内容为空")
            return False
            
    except Exception as e:
        print(f"  ✗ 下载失败：{e}")
        return False

async def main():
    """
    主函数：批量下载HowToCook的Markdown文件
    """
    print("=" * 60)
    print("HowToCook 爬虫启动")
    print("=" * 60)
    
    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        success_count = 0
        fail_count = 0
        total_count = 0
        
        # 1. 下载搭建环境和进阶知识的固定文件
        print("\n[1/2] 下载搭建环境和进阶知识...")
        for category, paths in TARGET_PATHS.items():
            print(f"\n处理类别：{category}")
            for file_path in paths:
                total_count += 1
                
                # 构建保存路径
                filename = os.path.basename(file_path)
                category_dir = os.path.join(SAVE_DIR, category)
                save_path = os.path.join(category_dir, filename)
                
                print(f"[{total_count}] {filename}")
                
                success = await download_markdown_from_github(page, file_path, save_path)
                
                if success:
                    success_count += 1
                else:
                    fail_count += 1
                
                # 延时避免请求过快
                await asyncio.sleep(0.5)
        
        # 2. 获取并下载所有菜谱
        print("\n[2/2] 下载菜谱...")
        recipe_links = await get_recipe_links_from_readme(page)
        
        for idx, link_info in enumerate(recipe_links, 1):
            total_count += 1
            href = link_info['href']
            title = link_info['text']
            
            # 从href提取文件路径
            # href格式: /Anduin2017/HowToCook/blob/master/dishes/dessert/红柚蛋糕/红柚蛋糕.md
            match = re.search(r'/blob/master/(.+\.md)', href)
            if not match:
                continue
            
            file_path = match.group(1)
            
            # 提取分类
            category_match = re.search(r'dishes/([^/]+)/', file_path)
            if category_match:
                category = category_match.group(1)
                category_name = {
                    'vegetable_dish': '素菜',
                    'meat_dish': '荤菜',
                    'aquatic': '水产',
                    'breakfast': '早餐',
                    'staple': '主食',
                    'semi-finished': '半成品加工',
                    'soup': '汤与粥',
                    'drink': '饮料',
                    'condiment': '酱料',
                    'dessert': '甜品'
                }.get(category, category)
            else:
                category_name = '其他'
            
            # 构建保存路径
            filename = os.path.basename(file_path)
            safe_filename = sanitize_filename(filename)
            category_dir = os.path.join(SAVE_DIR, f"菜谱-{category_name}")
            save_path = os.path.join(category_dir, safe_filename)
            
            print(f"[{idx}/{len(recipe_links)}] {title}")
            
            success = await download_markdown_from_github(page, file_path, save_path)
            
            if success:
                success_count += 1
            else:
                fail_count += 1
            
            # 延时避免请求过快
            await asyncio.sleep(0.5)
        
        await browser.close()
    
    # 输出统计信息
    print(f"\n{'='*60}")
    print(f"下载完成！")
    print(f"成功：{success_count} 个")
    print(f"失败：{fail_count} 个")
    print(f"总计：{total_count} 个")
    print(f"保存路径：{os.path.abspath(SAVE_DIR)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    asyncio.run(main())

