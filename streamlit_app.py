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

def settings_button(selected_sub_option):
    st.write(f"Settings button pressed with sub-option: {selected_sub_option}")
    # Add your code for the selected sub-option action here

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
                           icons=['house', 'gear'], menu_icon="cast", default_index=1)

    if selected == 'Settings':
        sub_option = st.selectbox("Sub-options", ["Rename", "Save"])
        settings_button(sub_option)

    if st.button("Home"):
        home_button()
