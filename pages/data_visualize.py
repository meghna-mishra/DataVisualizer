import pandas as pd
import streamlit as st
import lux
import streamlit.components.v1 as components
import os

def app():
    st.markdown("## Visualize Data")
    if st.session_state.file is None:
        st.markdown("### Please upload data through `Upload Data` page.")
    else:
        #df = pd.read_csv('data/main_data.csv')
        df = st.session_state.file
        df.clear_intent()
        st.session_state.colselected = False
        export_file = 'visualizations.html'
        html_content = df.save_as_html(output=True)

        components.html(html_content, width=1300, height=450)

        st.markdown('1. Correlation displays relationships between two quantitative variables, ranked by the most to least correlated scatterplots.')
        st.markdown('2. Distribution displays histogram distributions of different quantitative attributes in the dataframe, ranked by the most to least skewed distributions.')
        st.markdown('3. Occurrence displays bar chart distributions of different categorical attributes in the dataframe, ranked by the most to least uneven bar charts.')
        st.markdown('4. Geographical displays chloropleth maps of how different measures vary geographically.')
        st.markdown('4. Temporal displays how different measures vary across time.')