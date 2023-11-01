'''
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected
'''
import streamlit as st
from streamlit_option_menu import option_menu

def home_button():
    st.write("Home button pressed")
    # Add your code for the Home button action here

def settings_button():
    st.write("Settings button pressed")
    # Add your code for the Settings button action here

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
                           icons=['house', 'gear'], menu_icon="cast", default_index=1)

    if st.button("Home"):
        home_button()

    if st.button("Settings"):
        settings_button()
