import streamlit as st
from src.config import config
import streamlit as st
from PIL import Image       
import time

config()

def display_banner():
    image = Image.open('./assets/images/itc_logo.png')
    image = image.resize((int(image.width * 0.5), int(image.height * 0.5)))
    st.image(image, use_column_width=True)


def show_button_and_message():
    st.text(" ")    
    st.text(" ")
    st.text("Comming soon!")

    # col1, col2, col3 = st.columns([1, 2, 1])

    # with col2:
    #     button = st.button("IT", use_container_width=True)

    #     if button:
    #         st.markdown("<h1 style='text-align: center;'>CCCCCC</h1>", unsafe_allow_html=True)
    #         st.markdown("<h3 style='text-align: center;'>Sharing is caring!</h1>", unsafe_allow_html=True)
    #         st.balloons()
            


def main():
    display_banner()
    show_button_and_message()


if __name__ == "__main__":
    main()