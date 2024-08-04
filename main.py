import streamlit as st
from langchain_helper import get_few_shot_db_chain
st.markdown(
    """
    <style>
    .title {
        font-size: 35px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">DreamWear T-Shirts: Database Q&A 👕</h1>', unsafe_allow_html=True)

question = st.text_input("Question: ")

if question:
    try:
        chain = get_few_shot_db_chain()
        response = chain.run(question)

        st.header("Answer")
        st.write(response)
    except Exception as e:
        st.error("Please enter your question again.")
else:
    st.info("Please enter a question.")
