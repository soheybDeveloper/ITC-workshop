import streamlit as st
from dotenv import load_dotenv
import os
from .config import Config

def bootstrap_app():
    # Load environment variables
    load_dotenv()
    
    # Ensure assets directory exists for uploads
    os.makedirs("assets/uploads", exist_ok=True)
    
    # Initialize Streamlit Page Config once
    st.set_page_config(
        page_title=Config.APP_NAME,
        page_icon="🎫",
        layout="centered"
    )
