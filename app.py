import streamlit as st
from bootstrap.init import bootstrap_app
from database import init_db
from src.services.pagination_service import PaginationService
from components.banner import render_banner
from components.memory_form import render_upload_form
from components.memory_feed import render_feed

# 1. Initialize Application Configuration
bootstrap_app()

# 2. Ensure Database is ready
init_db.execute()

# 3. Setup Session State for Pagination
PaginationService.init_state()

def main():
    # --- Component 1: Banner Layout ---
    render_banner()
    
    st.markdown("<h2 style='text-align: center;'>The Wall of Memories</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # --- Component 2: Memory Creation Form ---
    render_upload_form()
    st.markdown("---")
    
    # Fetch Database Records via Service
    memories, limit = PaginationService.get_current_page_memories()
    
    # --- Component 3: Feed and Layout Switcher ---
    render_feed(memories, limit)

if __name__ == "__main__":
    main()