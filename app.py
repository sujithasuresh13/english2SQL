import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-EH5zKkQqNqLPmrksxJbGT3BlbkFJCiWotwUvgGgkhYvrEqas'

def generate_sql(query):
    prompt = f"Translate the following English description into an SQL query:\n\n{query}\n\nSQL Query:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    sql_query = response.choices[0].text.strip()
    return sql_query

st.title("English to SQL Converter")

query = st.text_area("Enter your English query here:")

if st.button("Convert to SQL"):
    if query:
        with st.spinner('Generating SQL...'):
            sql_query = generate_sql(query)
            st.success("SQL Query:")
            st.code(sql_query)
    else:
        st.error("Please enter a query.")
