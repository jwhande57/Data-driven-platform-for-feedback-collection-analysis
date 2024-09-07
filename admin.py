import streamlit as st
from auth import login
from dashboard import dashboard

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = None
    if st.session_state.logged_in:
        if st.button('Logout', type='primary'):
            st.session_state.logged_in = False
            st.rerun()
        dashboard()
    else:
        login()

