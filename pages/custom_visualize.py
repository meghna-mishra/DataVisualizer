import pandas as pd
import streamlit as st
import lux
import streamlit.components.v1 as components
import os


def change():
    st.session_state.colselected = True

def app():
    st.markdown("## Custom Visualization")
    if st.session_state.file is None:
        st.markdown("### Please upload data through `Upload Data` page.")
    else:
        #df = pd.read_csv('data/main_data.csv')
        df = st.session_state.file
        cols = df.columns
        st.markdown("#### Select one or more attributes to analyse.")
        selected_cols = st.multiselect(" ", cols, None, on_change = change)
        if st.session_state.colselected:
            df.intent = selected_cols
            export_file = 'visualizations.html'
            html_content = df.save_as_html(output=True)
            components.html(html_content, width=1350, height=800)