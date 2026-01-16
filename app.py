import streamlit as st
import requests
import json

# 设置页面配置
st.set_page_config(
    page_title="C Language RAG Tutor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 RAG-based C Language Tutor")
st.markdown("""
Welcome to your AI-powered C programming tutor! This system uses **Gemini 2.5 Flash** 
and **CppReference** documentation to provide high-quality answers.
""")

# 定义后端地址
API_URL = "http://127.0.0.1:8899/ask"

# 初始化聊天历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 侧边栏：显示参考资料
with st.sidebar:
    st.header("Reference Sources")
    st.info("When you ask a question, the most relevant documentation snippets will appear here.")
    source_placeholder = st.empty()

# 显示历史消息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 聊天输入
if prompt := st.chat_input("Ask a C programming question..."):
    # 添加用户消息到界面
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 调用后端接口
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🤔 Thinking...")
        
        try:
            response = requests.post(
                API_URL, 
                json={"question": prompt},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data["answer"]
                sources = data.get("source_docs", [])
                
                # 更新回答
                message_placeholder.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
                # 更新侧边栏参考资料
                with source_placeholder.container():
                    for i, src in enumerate(sources):
                        st.markdown(f"**Source {i+1}:**")
                        st.caption(f"{src[:200]}...")
                        st.divider()
            else:
                message_placeholder.error(f"Error: Backend returned status code {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            message_placeholder.error("Error: Could not connect to the backend server. Please make sure the FastAPI server (main.py) is running on port 8000.")
        except Exception as e:
            message_placeholder.error(f"An unexpected error occurred: {str(e)}")
