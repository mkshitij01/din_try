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

with st.sidebar:
    selected = option_menu("Menu", ["Home", option_menu('Settings', ['link1', 'link2'])]
        icons=['house', 'gear'], default_index=0)

if selected == "Home":
    st.write("home is where the heart is")
    
else:
    st.write("settings is my bettings")
