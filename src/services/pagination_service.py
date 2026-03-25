import streamlit as st
from src.actions import fetch_memories_action

class PaginationService:
    @staticmethod
    def init_state():
        if "offset" not in st.session_state:
            st.session_state.offset = 0
            
    @staticmethod
    def load_more():
        st.session_state.offset += 10
        
    @staticmethod
    def get_current_page_memories():
        limit = st.session_state.offset + 10
        return fetch_memories_action.execute(limit=limit, offset=0), limit
