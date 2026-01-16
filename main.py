from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from vector_store import VectorStore
from gemini_engine import generate_answer
import os
from dotenv import load_dotenv

# 加载配置
load_dotenv()

app = FastAPI(title="RAG-based C Language Tutor API")

# 全局初始化向量库
# 注意：这可能会因为加载模型而耗时几秒
print("--- 正在初始化向量库和模型 ---")
vs = VectorStore()
print("--- 向量库初始化完成 ---")

class QueryRequest(BaseModel):
    question: str

@app.on_event("startup")
async def startup_event():
    if not vs.documents:
        print("警告: 知识库为空。请确保已运行 ingest_data.py")
    else:
        print(f"知识库已预热，当前加载了 {len(vs.documents)} 条文档片段。")

@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        print(f"收到问题: {request.question}")
        context = vs.search(request.question, top_k=3)
        
        if not context:
            context = ["No specific reference in the local documentation."]

        api_key = os.getenv("GEMINI_API_KEY")
        answer = generate_answer(request.question, context, api_key)
        
        return {
            "question": request.question,
            "answer": answer,
            "source_docs": context
        }
    except Exception as e:
        print(f"处理请求时出错: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("\n[BACKEND] 正在启动 FastAPI 服务 at http://127.0.0.1:8899")
    print("[BACKEND] 请确保终端保持打开状态...")
    uvicorn.run(app, host="127.0.0.1", port=8899)
