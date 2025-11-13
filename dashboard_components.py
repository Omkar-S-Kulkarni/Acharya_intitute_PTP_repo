# modules/dashboard_components.py
import streamlit as st

def render_header():
    st.markdown("""
        <div style="display:flex; align-items:center;">
            <img src="assets/logo.png" width="50" style="margin-right:10px;">
            <h1 style="color:green;">Renewable Energy & Carbon Dashboard</h1>
        </div>
        """, unsafe_allow_html=True)

def render_tabs():
    return st.tabs(["Chat / Q&A", "Upload & Summarize", "Insights"])

def render_file_upload(upload_label="Upload CSV/TXT file"):
    uploaded_file = st.file_uploader(upload_label, type=["csv","txt"])
    return uploaded_file

def render_spinner(msg="Processing..."):
    return st.spinner(msg)
