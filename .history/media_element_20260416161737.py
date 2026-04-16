import streamlit as st
st.title("Input your files ",anchor=False)
st.divider();
image = st.file_uploader("Enter your image",
                 type=["jpeg","png","gif","jpg"])
print(type(image))
if image:
    st.image(image)
