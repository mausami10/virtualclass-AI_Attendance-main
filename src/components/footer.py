import streamlit as st 
import base64

def footer_home():

    logo_url = r"E:\mausami.png"

    with open(logo_url, "rb") as image_file: 
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <div style="margin-top:2rem; display: flex; gap: 6px; justify-content: center; items-align: center;">
            <p style="font-weight:bold; color: white;"> Created with ❤️ by </p>
            <img src='data:image/png;base64, {encoded_image}' style='max-height:25px; border-radius: 20px; border: bl'/>
        </div>
        """, unsafe_allow_html=True)

def footer_dashboard():

    logo_url = r"E:\mausami.png"

    with open(logo_url, "rb") as image_file: 
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <div style="margin-top:2rem; display: flex; gap: 6px; justify-content: center; items-align: center;">
            <p style="font-weight:bold; color: black;"> Created with ❤️ by </p>
            <img src='data:image/png;base64, {encoded_image}' style='max-height:25px; border-radius: 20px; border: bl'/>
        </div>
        """, unsafe_allow_html=True)