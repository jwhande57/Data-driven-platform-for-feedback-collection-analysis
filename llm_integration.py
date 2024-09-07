import openai
import streamlit as st

openai.api_key = st.secrets["API_KEY"]

def analyze_generate_response(prompt):
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a data scientist responsible for generating structured ans insightful analysis reports based  on the provided data. Ensure that your analysis is comprehensive, well-organized, and highlights key findings, trends and actionable recommendations",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        report_text = response.choices[0].message.content.strip()
        st.markdown(report_text)
    except Exception as e:
        st.error(f"An error occurred: {e}")
