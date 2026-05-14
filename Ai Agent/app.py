import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

st.title("AI Chat Box")

llm = ChatOpenAI(model="gpt-4o-mini")

user_input = st.text_input("Ask anything you like!")

if st.button("Send") and user_input:
    response = llm.invoke(user_input)
    st.write(response.content)
