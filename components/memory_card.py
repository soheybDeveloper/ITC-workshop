import streamlit as st

def _render_image_safe(image_path: str):
    """Helper to safely render an image."""
    try:
        st.image(image_path, use_column_width=True)
    except Exception:
        st.error("Image not found")

def _render_kanban_view(memory: dict):
    with st.container(border=True):
        st.markdown(f"**{memory['title']}**")
        st.caption(f"By {memory['name']} | 🕒 *{memory['created_at']}*")
        st.write(memory['text'])
        
        image_path = memory.get('image_path')
        if image_path:
            _render_image_safe(image_path)

def _render_list_view(memory: dict):
    with st.container(border=True):
        image_path = memory.get('image_path')
        if image_path:
            _render_image_safe(image_path)
        else:
            st.markdown("<h1 style='text-align: center; color: gray;'>🎫</h1>", unsafe_allow_html=True)
            
        st.markdown(f"<h3 style='text-align: center;'>{memory['title']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'><b>Author:</b> {memory['name']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'><i>\"{memory['text']}\"</i></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: gray; font-size: small;'>🕒 {memory['created_at']}</p>", unsafe_allow_html=True)

def render_memory_ticket(memory: dict, view_type="list"):
    """
    Renders a single memory by routing it to the appropriate view component.
    """
    if view_type == "kanban":
        return _render_kanban_view(memory)
        
    return _render_list_view(memory)
