import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = 'sk-proj-EH5zKkQqNqLPmrksxJbGT3BlbkFJCiWotwUvgGgkhYvrEqas'

# Define a function to convert English to SQL
def english_to_sql(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app interface
st.title("English to SQL Converter")
st.write("Enter an English sentence to convert it to an SQL query.")

# Input text box for English sentence
user_input = st.text_area("English Sentence", "")

if st.button("Convert"):
    if user_input:
        sql_query = english_to_sql(user_input)
        st.write("Generated SQL Query:")
        st.code(sql_query)
    else:
        st.write("Please enter an English sentence.")

