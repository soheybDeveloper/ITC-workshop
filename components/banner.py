import os
import streamlit as st
from PIL import Image

@st.cache_resource
def load_banner_image(path: str):
    if os.path.exists(path):
        return Image.open(path)

    return None

def render_banner():
    """Renders the top banner or a fallback title."""
    banner_path = "./assets/images/itc_banner_incorrect_name.png"
    banner_image = load_banner_image(banner_path)

    if banner_image:
        st.image(banner_image, use_column_width=True)
        return
    
    st.markdown(
        "<h1 style='text-align: center; color: #ff4b4b;'>ITC Workshop</h1>",
        unsafe_allow_html=True
    )