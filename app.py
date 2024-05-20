# import streamlit as st
# from langchain.llms import OpenAI

import openai
import streamlit as st

st.title('English to SQL Converter')

api_key = st.sidebar.text_input('Enter your OpenAI API key: ', type='password')

client = openai.OpenAI(
    api_key= api_key,
    base_url="https://api.aimlapi.com/",
)

def generate_response(english_query):
    chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": "You are an assistant that converts English to SQL."},
            {"role": "user", "content": english_query},
        ],
        temperature=0.7,
        max_tokens=512,
    )
    chat_completion.choices[0].messages.content

with st.form('my_form'):

    english_query = st.text_input("Enter your English query:")

    submitted = st.form_submit_button('Submit')
   
    if submitted:
        try:
            generate_response(english_query)
        except Exception as e:
            print('Failed to generate : %s', repr(e))

