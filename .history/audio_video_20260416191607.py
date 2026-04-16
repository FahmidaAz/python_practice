import streamlit as st
st.title("Input your audio/video")
st.divider();
st.subheader("From directory")
st.audio("audio/hello.mp3")
st.divider();
st.subheader("Upload a audio file")
audio_file = st.file_uploader(type=['mp3','ogg','flac'], accept_multiple_files=True)

if audio_file:
    st.audio(audio_file)
