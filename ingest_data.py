from scraper import crawl_cppreference
from vector_store import VectorStore
import time

def ingest_core_knowledge():
    """
    抓取核心 C 语言页面并存入向量数据库。
    """
    urls = [
        "https://en.cppreference.com/w/c/language/basic_concepts",
        "https://en.cppreference.com/w/c/language/type",
        "https://en.cppreference.com/w/c/language/operator_precedence",
        "https://en.cppreference.com/w/c/language/if",
        "https://en.cppreference.com/w/c/language/for",
        "https://en.cppreference.com/w/c/language/switch",
        "https://en.cppreference.com/w/c/language/pointer",
        "https://en.cppreference.com/w/c/language/struct",
        "https://en.cppreference.com/w/c/language/union",
        "https://en.cppreference.com/w/c/language/function_declaration",
        "https://en.cppreference.com/w/c/memory",
        "https://en.cppreference.com/w/c/language/preprocessor",
        "https://en.cppreference.com/w/c/io"
    ]
    
    vs = VectorStore()
    all_docs = []
    
    for url in urls:
        docs = crawl_cppreference(url)
        all_docs.extend(docs)
        # 礼貌抓取，间隔 1 秒
        time.sleep(1)
        
    if all_docs:
        print(f"\n正在将共计 {len(all_docs)} 条文档导入向量数据库...")
        vs.add_documents(all_docs)
        print("✅ 知识库数据导入完成！")
        
        # 验证一下
        print("\n验证检索功能:")
        query = "Explain what a struct is in C."
        results = vs.search(query, top_k=2)
        for i, res in enumerate(results):
            print(f"结果 {i+1}: {res[:150]}...")
    else:
        print("❌ 未抓取到任何文档。")

if __name__ == "__main__":
    ingest_core_knowledge()
