#爬虫

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import os

# 目标URL
url = "https://www.runoob.com/python/python-basic-syntax.html"
save_dir = "runoob_python_docs"
os.makedirs(save_dir, exist_ok=True)

# 完善请求头，加Referer.模拟从菜鸟教程首页跳转过来
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Host": "www.runoob.com",
    "Referer": "https://www.runoob.com/python/"  # 模拟来源页面，降低反爬概率
}

# 重试机制
session = requests.Session()
retry = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504]
)
session.mount("http://", HTTPAdapter(max_retries=retry))
session.mount("https://", HTTPAdapter(max_retries=retry))

try:
    response = session.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"  # 确保中文不乱码
    soup = BeautifulSoup(response.text, "lxml")

except requests.exceptions.RequestException as e:
    print(f"请求失败：{e}")
    exit()

# 1. 提取标题
title_tag = soup.find("h1")
title = title_tag.text.strip().replace("/", "_").replace("\\", "_") if title_tag else "unknown_title"

# 2. 提取内容（关键修改：class从article-content改为article-body）
content_tag = soup.find("div", class_="article-body")
if not content_tag:
    print("未找到内容标签，可检查页面div的class列表")
    exit()

# 清理内容（去除多余空行和空格）
content = "\n".join([line.strip() for line in content_tag.text.splitlines() if line.strip()])

# 保存内容
with open(f"{save_dir}/{title}.txt", "w", encoding="utf-8") as f:
    f.write(content)

print(f"已爬取：{title}")
print(f"保存路径：{save_dir}/{title}.txt")