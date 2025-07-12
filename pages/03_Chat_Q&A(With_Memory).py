# pages/chatbot.py (두 번째 페이지)
import streamlit as st
import openai
import os
from dotenv import load_dotenv

# 환경변수 불러오기
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("💬 GPT 채팅 챗봇 (with Memory)")
st.markdown(
    """
    이번 챗봇은 이전 대화내역을 **3개까지 기억**합니다.
    이전 질문과 연결되는 질문을 해보고 결과를 확인해보세요.
    """
)

# chat_history 키를 페이지별로 다르게!
if "chat_history_page2" not in st.session_state:
    st.session_state["chat_history_page2"] = []

chat_history = st.session_state["chat_history_page2"]

# 채팅 내역 출력 (최신 메시지가 아래로)
for msg in chat_history:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# 채팅 입력창
user_input = st.chat_input("질문을 입력하세요.")

if user_input:
    # 유저 메시지 추가
    chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # 이전 대화 전체를 messages로 변환 (system 프롬프트 추가)
    messages = [{"role": "system", "content": "너는 친절한 AI 챗봇이야. 사용자 질문에만 간결하고 친절하게 답변해줘."}]
    messages.extend(chat_history[-3:])

    # OpenAI API 호출
    with st.spinner("답변 생성 중..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=512,
                temperature=0.7,
            )
            bot_reply = response.choices[0].message.content.strip()
        except Exception as e:
            bot_reply = f"에러 발생: {e}"

    # 답변 메시지 추가 및 출력
    chat_history.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
