import os
import streamlit as st

def render_banner():
    """Renders the top banner for the application."""
    if os.path.exists("./assets/images/itc_logo.png"):
        st.image("./assets/images/itc_logo.png", use_container_width=True)
        return
    st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>ITC Workshop</h1>", unsafe_allow_html=True)
