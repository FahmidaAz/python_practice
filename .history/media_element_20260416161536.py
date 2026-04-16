import streamlit as st
st.title("Input your files ",anchor=False)
st.divider();
st.file_uploader("Enter your image",
                 (type=["jpeg","png","gif"]))