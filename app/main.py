# -*- coding: utf-8 -*-

try:
    import streamlit as st
    st.set_page_config(page_title="cassava-vit-doctor", layout="centered")
    st.title("cassava-vit-doctor")
    st.write("Estructura base generada (Streamlit).")
    st.caption("Para ejecutar: streamlit run app/main.py")
except Exception:
    print("Streamlit no está instalado. Instalá: pip install streamlit")
    print("Luego ejecutá: streamlit run app/main.py")


