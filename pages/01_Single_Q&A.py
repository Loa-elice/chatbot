# pages/chatbot.py
import streamlit as st
import openai
import os
from dotenv import load_dotenv

# .env 파일에서 OPENAI_API_KEY를 불러옴
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧑‍💻 GPT API를 활용한 간단 챗봇")
st.markdown(
    """
    아래 입력창에 질문을 작성하면 OpenAI GPT 모델이 답변해줍니다.
    """
)
st.write("")

# 입력창
user_input = st.text_input("질문을 입력하세요.", key="question_input")

# 답변 출력
if user_input:
    with st.spinner("답변 생성 중..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "너는 친절한 AI 챗봇이야. 사용자 질문에만 간결하고 친절하게 답변해줘."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=512,
                temperature=0.7,
            )
            st.markdown(f"**답변:**\n\n{response.choices[0].message.content}")
        except Exception as e:
            st.error(f"에러가 발생했습니다: {e}")
