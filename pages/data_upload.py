import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.markdown("## Upload Data")

    st.markdown("#### Upload a csv file for analysis.") 
    st.write("\n")

    uploaded_file = st.file_uploader("Choose a file", type = ['csv', 'xlsx'])
    global data
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            st.write("File uploaded.")
            st.session_state.file = data
        except Exception as e:
            print(e)
            data = pd.read_excel(uploaded_file)
            st.session_state.file = data

    if st.session_state.file is not None:
        st.markdown('### Preview')
        st.dataframe(data)
