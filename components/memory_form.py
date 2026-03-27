import streamlit as st
from src.actions import save_uploaded_file_action
from src.actions import save_memory_action

def render_upload_form():
    st.subheader("Add Your Memory!")
    
    with st.form("add_memory_form", clear_on_submit=True):
        title = st.text_input("Memory Title", max_chars=100)
        name = st.text_input("Your Name / Nickname", max_chars=50)
        text = st.text_area("What is your memory?", max_chars=250)
        uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
        
        submitted = st.form_submit_button("Submit Memory")
        
        if submitted:
            if not name or not text or not title:
                st.warning("Please fill out the title, your name, and the memory text.")
                return
            
            image_path = None
            if uploaded_file:
                result = save_uploaded_file_action.execute(uploaded_file)
                if isinstance(result, tuple) and result[0] is None:
                    st.error(result[1])
                    return
                elif isinstance(result, tuple) and result[0] is not None:
                    image_path = result[0]
            
            success, msg = save_memory_action.execute(title, name, text, image_path)
            
            if success:
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)
