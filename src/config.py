import streamlit as st
import os
from dotenv import load_dotenv

def config():
    load_dotenv()

    st.set_page_config(
    page_title = os.getenv('STREAMLIT_APP_NAME'),
    
    layout="centered"
)