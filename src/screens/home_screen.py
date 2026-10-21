import streamlit as st 
from src.components.footer import footer_home
from src.components.header import header_home
from src.ui.base_layout import style_background_home, style_base_layout

def home_screen(): 
     

    header_home()
    style_base_layout()
    style_background_home()

    col1, col2 = st.columns(2, gap="large")

    with col1: 
        st.header("I'm Teacher")
        st.image("https://png.pngtree.com/png-vector/20240126/ourmid/pngtree-adorable-teacher-character-png-image_11557342.png", width=130)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'): 
            st.session_state['login_type']='teacher'
            st.rerun()
    with col2: 
        st.header("I'm Student")
        st.image("https://png.pngtree.com/png-vector/20250308/ourmid/pngtree-excited-school-kids-multicultural-group-of-happy-students-png-image_15745898.png", width=130)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'): 
            st.session_state['login_type']='student'
            st.rerun()

    footer_home()