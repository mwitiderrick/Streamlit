import streamlit as st
from PIL import Image

icon = Image.open("icon.png")

st.set_page_config(
    page_title="Data Application",
    page_icon=icon,
    layout="centered",
    initial_sidebar_state="auto",
)

image = Image.open("logo.png")

st.image(image)

video_file = open("video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

audio_file = open("video.wav", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes)