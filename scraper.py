import requests
from bs4 import BeautifulSoup
import time

def crawl_cppreference(url: str) -> list[str]:
    """
    抓取 CppReference 页面正文内容。
    提取 div#mw-content-text 下的所有 <p> 和 <li> 文本。
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print(f"正在抓取: {url} ...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # CppReference 的主要内容通常在 div#mw-content-text
        content_area = soup.find('div', id='mw-content-text')
        if not content_area:
            # 备选方案：有些页面可能结构略有不同
            content_area = soup.find('div', id='cpp-content-base')
            
        if not content_area:
            print(f"警告: 未能在 {url} 中找到正文区域。")
            return []
            
        documents = []
        
        # 提取所有段落 <p>
        for p in content_area.find_all('p'):
            text = p.get_text(strip=True)
            if len(text) > 20: # 过滤掉太短的片段
                documents.append(text)
                
        # 提取所有列表项 <li>
        for li in content_area.find_all('li'):
            text = li.get_text(strip=True)
            if len(text) > 20:
                documents.append(text)
                
        print(f"成功抓取 {len(documents)} 条文档片段。")
        return documents
        
    except Exception as e:
        print(f"抓取 {url} 时出错: {e}")
        return []

if __name__ == "__main__":
    # 测试代码
    test_url = "https://en.cppreference.com/w/c/language/pointer"
    docs = crawl_cppreference(test_url)
    for i, d in enumerate(docs[:3]):
        print(f"{i+1}: {d[:100]}...")
