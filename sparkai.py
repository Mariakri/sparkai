#create a custom LLMS like chat with UI (web browser) with saving history sessions 

import streamlit as st
from openai import OpenAI
client = OpenAI(
    api_key=""
)

st.title("SPARK ai")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt:=st.chat_input("Ask Anything... "):
    st.session_state.messages.append({"role":"user","content":prompt})

    with st.chat_message("user"):
        st.write(prompt)

    response=client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)

    answer=response.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append({"role":"assistant","content":answer})


