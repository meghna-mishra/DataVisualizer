import streamlit as st
from application import Application
from pages import data_upload, data_visualize, custom_visualize
st.set_page_config(layout="wide")
app = Application()
app.add_page("Upload Data", data_upload.app)
app.add_page("Visualize Data", data_visualize.app)
app.add_page("Custom Visualization", custom_visualize.app)

app.run()
