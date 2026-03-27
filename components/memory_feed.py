import streamlit as st
from components.memory_card import render_memory_ticket
from src.services.pagination_service import PaginationService

def render_feed(memories, limit):
    """Renders the view switcher and the list/gallery of memories."""
    # View Switcher Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.header("Recent Memories")
    with col2:
        view_type = st.selectbox("View As", ["List", "Gallery", "Table"])
        
    if not memories:
        st.info("No memories yet. Be the first to add one!")
        return

    # Render Layouts Based on Selected View
    if view_type == "Gallery":
        cols = st.columns(2)
        for i, mem in enumerate(memories):
            with cols[i % 2]:
                render_memory_ticket(mem, view_type="kanban")
                
    elif view_type == "Table":
        # Format list of dicts for cleanly displaying in native Streamlit dataframe
        display_data = [
            {
                "ID": m["id"],
                "Title": m["title"],
                "Author": m["name"],
                "Memory": m["text"],
                "Date": m["created_at"]
            }
            for m in memories
        ]
        st.dataframe(display_data, use_container_width=True)
            
    else:
        for mem in memories:
            render_memory_ticket(mem, view_type="list")
    
    # Pagination Button
    if len(memories) == limit:
        st.button("Load More Memories...", on_click=PaginationService.load_more, use_container_width=True)
