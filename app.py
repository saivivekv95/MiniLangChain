###Q&A Chatbot
from langchain.llms import OpenAI
import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv()


#### Function to load OpenAI model and  get response


def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response = llm(question)
    return response

#####Initialise streamlit app##
st.set_page_config(page_title="Q&A Demo")

st.header("LangChain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Generate")
### If generate button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)