import streamlit as st
from streamlit_embedcode import github_gist

gist_link = st.text_input(
    "Enter Link",
    "https://gist.github.com/mwitiderrick/0486435c53939a2fcee235e2a02a5550",
)
github_gist(gist_link, width=730)