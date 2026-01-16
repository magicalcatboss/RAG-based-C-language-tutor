import google.generativeai as genai
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def generate_answer(query: str, context: list[str], api_key: str = None):
    """
    使用 Gemini API 基于检索到的上下文生成 C 语言教学回答。
    """
    # 优先使用传入的 key，其次使用环境变量
    key = api_key or os.getenv("GEMINI_API_KEY")
    
    if not key:
        return "错误: 未配置 GEMINI_API_KEY。请在 .env 文件中设置。"

    try:
        # 配置 SDK
        genai.configure(api_key=key)
        
        # 初始化模型
        # 注意：有些环境下需要 models/ 前缀，有些不需要。这里用最通用的写法。
        model_name = 'gemini-2.5-flash'
        model = genai.GenerativeModel(model_name)
        
        # 整合上下文
        context_text = "\n\n".join(context)
        
        # 构建 Prompt (用户指定的导师角色)
        prompt = f"""你是一个资深的 C 语言导师。请基于以下参考资料回答学生的问题。
如果参考资料里没有直接答案，请结合你作为资深导师的专业知识给出最准确的回答，并注明哪些是基于参考资料的。
如果学生的问题完全超出了 C 语言和参考资料的范畴，请礼貌地指出。

---
参考资料：
{context_text}
---

学生问题：{query}

请以专业、易懂且富有逻辑的方式回答。"""

        # 调用生成
        response = model.generate_content(prompt)
        
        return response.text

    except Exception as e:
        return f"调用 Gemini API 时出错: {str(e)}"

if __name__ == "__main__":
    # 测试代码 (如果没有 KEY，这会返回报错提示)
    test_query = "What is a pointer?"
    test_context = ["A pointer is a variable that stores memory address."]
    print(generate_answer(test_query, test_context))
