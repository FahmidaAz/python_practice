import streamlit as st
st.title("Input your files ",anchor=False)
st.divider();
image = st.file_uploader("Enter your image",
                 type=["jpeg","png","gif","jpg"],
                 accept_multiple_files= True)
print(type(image))
if image:
    image_col = st.column(len(image))

    for img in enumerate(image):
        
