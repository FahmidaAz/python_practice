import streamlit as st
st.title("Input your audio/video")
st.divider();
st.subheader("From directory")
st.audio("audio/hello.mp3")
st.divider();
st.subheader("Upload a audio file")
audio_file = st.file_uploader("Enter your audio",
                              type=['mp3','ogg','flac'])
print(type(audio_file))
if audio_file:
    st.audio(audio_file)

#video upload
st.divider();
st.subheader("Upload Video file")
st.divider();
video_file = st.file_uploader("Enter your video",type='mp4')
video_upload_button = st.button("Upload now!", type="secondary")