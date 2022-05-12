import streamlit as st
from dotenv import load_dotenv
import os


PROJECT = os.getenv("PROJECT")

st.write("Hello this is the project {PROJECT} project".format(PROJECT=PROJECT))
