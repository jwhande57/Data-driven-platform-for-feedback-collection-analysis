import streamlit as st
from feedback_form import show_questionnaire
from admin import main

st.set_page_config(page_icon=":material/edit:",layout="wide")
pages = [
    st.Page(show_questionnaire, title="Share Your Feedback", default=True),
    st.Page(main, title="Administrator Dashboard")
]
pg = st.navigation(pages)
pg.run()