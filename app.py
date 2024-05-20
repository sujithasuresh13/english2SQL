import streamlit as st
from langchain.llms import OpenAI
#from langchain_community.llms import OpenAI
#from openai import OpenAI
'''
# Streamlit app
st.title("English to SQL Converter")

# API Key input
# openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Function to convert English to SQL
def english_to_sql(query):
    #OpenAI.api_key = api_key
    st.warning('englist to sql..', icon='⚠')
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.warning(llm(query))
    
    
    # response = llm.chats.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are an assistant that converts English to SQL."},
    #         {"role": "user", "content": query}
    #     ]
    # )
    # return response['choices'][0]['message']['content']

# Input for English query
english_query = st.text_area("Enter your English query:", "top sales in the last quarter")

if st.button("Convert to SQL"):
    with st.spinner("Converting..."):
        st.warning('processing..', icon='⚠')
        sql_query = english_to_sql(english_query)
        st.success("SQL Query:")
        st.code(sql_query, language="sql")
'''    
#---------------------------------------

st.title('👩‍💼 Welcome to AI-Powered Resume Builder')

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
    chat_completion.choices[0].message.content

with st.form('my_form'):

    english_query = st.text_input("Enter your English query:", "top sales in the last quarter")

    submitted = st.form_submit_button('Submit')
   
    if submitted:
        try:
            generate_response(english_query)
        except Exception as e:
            print('Failed to generate : %s', repr(e))


#---------------------------------------

# with st.form('my_form'):
#     english_query = st.text_area("Enter your English query:", "top sales in the last quarter")
#     submitted = st.form_submit_button('Submit')
#     if not openai_api_key.startswith('sk-'):
#         st.warning('Please enter your OpenAI API key!', icon='⚠')
#     if submitted and openai_api_key.startswith('sk-'):
#         english_to_sql(english_query)




# if st.button("Convert to SQL"):
#     if not openai_api_key.startswith('sk-'):
#         st.warning('Please enter your OpenAI API key!', icon='⚠')
#     elif not english_query:
#          st.warning('Please enter query!', icon='⚠')
#          st.error("Please enter an English query.")
#     else:
#         st.warning('converting..', icon='⚠')
#         with st.spinner("Converting..."):
#             try:
#                 st.warning('processing..', icon='⚠')
#                 sql_query = english_to_sql(english_query)
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
