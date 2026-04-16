import streamlit as st
st.title("Input your files ",anchor=False)
st.divider();
image = st.file_uploader("Enter your image",
                 type=["jpeg","png","gif","jpg"],
                 accept_multiple_files= True)
print(type(image))
if image:
    image_col = st.columns(len(image))

    for i, img in enumerate(image):
        with image_col[i]:
            st.image(img)
store_img = st.image("images/G2.jpeg")
url_image = st.image("https://commons.wikimedia.org/wiki/File:Pink_flower.jpg")