import streamlit as st

class Application: 

    def __init__(self) -> None:
        if 'file' not in st.session_state:
            st.session_state.file = None
        if 'colselected' not in st.session_state:
            st.session_state.colselected = False
        self.pages = []
    
    def add_page(self, title, func) -> None: 

        self.pages.append({
          
                "title": title, 
                "function": func
            })

    def run(self):
        st.sidebar.title("Data visualization with Lux")
        page = st.sidebar.selectbox(
            'Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        page['function']()