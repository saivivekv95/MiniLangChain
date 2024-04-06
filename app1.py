### Conversational Q&A Chatbot

import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_openai import ChatOpenAI
import os


###streamliui

st.set_page_config(page_title="Conversational Q&A")
st.header("Hey lets chat!!!")

from dotenv import load_dotenv
load_dotenv()

chat=ChatOpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),temperature = 0.7)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You are a comedian AI assistant")
    ]

def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content


input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Generate")
### If generate button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)