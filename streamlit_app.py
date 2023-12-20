import streamlit as st
import os

# Get the current working directory
current_directory = os.getcwd()

# Display the current working directory in the Streamlit app
st.write(f"Current Working Directory: {current_directory}")
