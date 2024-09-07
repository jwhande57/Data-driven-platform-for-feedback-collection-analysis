import streamlit as st

def login():
    if st.session_state.get('logged_in', False):
        return True
    else:
        with st.form("Logged"):
            st.markdown("""
                <center>
                    <h3>🔒 Please log in to access this exclusive section</h3>
                </center>
                """, unsafe_allow_html=True)
            
            username = st.text_input("👤 Username")
            password = st.text_input("🔑 Password", type="password")
            
            if st.form_submit_button('🔓 Login', type="primary", use_container_width=True):
                if username == "admin" and password == "admin":
                    st.success("✅ Welcome to the platform!")
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("❌ Incorrect credentials. Please try again.")
                    return False

        st.markdown("<center>🌐 Developed with care by Jerald Whande</center>", unsafe_allow_html=True)
