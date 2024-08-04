import streamlit as st
from langchain_helper import get_few_shot_db_chain
import sqlite3

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
        st.write("Initializing the chain...")
        chain = get_few_shot_db_chain()
        st.write("Chain initialized successfully.")

        st.write("Running the chain with the input question...")
        response = chain.run(question)

        st.header("Answer")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please enter a question.")
