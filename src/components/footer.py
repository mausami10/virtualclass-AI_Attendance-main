import streamlit as st
import base64
from pathlib import Path

# footer.py is in src/components/, so parents[2] is the repo root
ROOT = Path(__file__).resolve().parents[2]
LOGO_PATH = ROOT / "assets" / "mausami.png"


def _get_logo_base64():
    """Return the logo as a base64 string, or None if the file is missing."""
    if LOGO_PATH.exists():
        with open(LOGO_PATH, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    return None


def _render_footer(text_color):
    encoded_image = _get_logo_base64()

    if encoded_image:
        logo_html = (
            f"<img src='data:image/png;base64,{encoded_image}' "
            f"style='max-height:25px; border-radius:20px;'/>"
        )
    else:
        # Fallback so the app doesn't crash if the logo is missing
        logo_html = f"<span style='font-weight:bold; color:{text_color};'>Mausami</span>"

    st.markdown(
        f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:{text_color}; margin:0;">Created with ❤️ by</p>
            {logo_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_home():
    _render_footer("white")


def footer_dashboard():
    _render_footer("black")