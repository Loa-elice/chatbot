import streamlit as st

st.set_page_config(page_title="Home", page_icon=":house:")

st.title("OpenAI API를 활용한 챗봇 구현")

st.markdown(
    """
    OpenAI의 API를 활용하면 다양한 GPT 모델들을 불러와 사용할 수 있습니다.

    > **Note:**  
    > OpenAI API를 활용하려면 **API Key**가 반드시 필요합니다.

    - **API Key**는 `.env` 파일에 저장해야 실습이 원활하게 실행됩니다.
        - 예시:  
        ```env
        OPENAI_API_KEY="sk-proj-2fc35478m2..."
        ```

    - 이번 실습에서는 **GPT-4o-mini** 모델을 사용합니다.
        - GPT-4o-mini는 작고 빠르면서도 준수한 성능을 보이는 모델입니다.

    ---

    **Tip:**  
    API Key는 외부에 노출되지 않도록 주의하세요!
    """
)
