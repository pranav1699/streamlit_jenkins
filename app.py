import streamlit as st
import os


PROJECT = os.getenv("PROJECT")

st.write("Hello this is the project {PROJECT} project".format(PROJECT=PROJECT))
