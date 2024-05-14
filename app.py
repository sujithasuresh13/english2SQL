import streamlit as st
import openai

# Function to convert English to SQL using OpenAI's API
def english_to_sql(api_key, english_text):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Convert the following English text to SQL: {english_text}",
        max_tokens=150
    )
    sql_query = response.choices[0].text.strip()
    return sql_query

# Streamlit app
def main():
    st.title("English to SQL Converter")
    
    api_key = st.text_input("Enter your OpenAI API key", type="password")
    english_text = st.text_area("Enter the English text", placeholder="e.g., Show me the total sales for the last quarter")
    
    if st.button("Convert to SQL"):
        if not api_key:
            st.error("Please enter your OpenAI API key.")
        elif not english_text:
            st.error("Please enter some English text to convert.")
        else:
            sql_query = english_to_sql(api_key, english_text)
            st.text_area("Generated SQL Query", value=sql_query, height=200)

if __name__ == "__main__":
    main()
