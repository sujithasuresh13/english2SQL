import streamlit as st
from langchain.llms import OpenAI
#from langchain_community.llms import OpenAI
#from openai import OpenAI

# Streamlit app
st.title("English to SQL Converter")

# API Key input
# openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Function to convert English to SQL
def english_to_sql(query):
    #OpenAI.api_key = api_key
   
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(query))
    
    # response = llm.chats.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are an assistant that converts English to SQL."},
    #         {"role": "user", "content": query}
    #     ]
    # )
    # return response['choices'][0]['message']['content']

# Input for English query

with st.form('my_form'):
    english_query = st.text_area("Enter your English query:", "top sales in the last quarter")
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        english_to_sql(english_query)

# if st.button("Convert to SQL"):
#     if not openai_api_key:
#         st.error("Please enter your OpenAI API key.")
#     elif not english_query:
#         st.error("Please enter an English query.")
#     else:
#         with st.spinner("Converting..."):
#             try:
#                 sql_query = english_to_sql(openai_api_key, english_query)
#                 st.success("SQL Query:")
#                 st.code(sql_query, language="sql")
#             except Exception as e:
#                 st.error(f"Error from the code :: {e}")

# # Display a footer
# st.markdown(
#     """
#     <style>
#     .footer {
#         position: fixed;
#         bottom: 0;
#         width: 100%;
#         color: white;
#         background-color: #f63366;
#         text-align: center;
#     }
#     </style>
#     <div class="footer">
#         <p>Powered by OpenAI and Streamlit</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
