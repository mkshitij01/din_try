import streamlit as st

# Define functions for each link action
def home_action():
    st.write("You clicked on Home!")

def edit_action():
    st.write("You clicked on Edit!")

def rename_action():
    st.write("You clicked on Rename!")

def about_action():
    st.write("You clicked on About!")

# Define a CSS style for consistent button size
button_style = "padding: 10px; width: 200px; text-align: left;"

# Create clickable links in the sidebar with consistent size
if st.sidebar.button("Home", key="home", help="Home Button", type="default", on_click=home_action, args=()):
    pass

if st.sidebar.button("Settings", key="settings", help="Settings Button", type="default", on_click=None, args=()):
    if st.sidebar.button("Edit", key="edit", help="Edit Button", type="default", on_click=edit_action, args=()):
        pass

    if st.sidebar.button("Rename", key="rename", help="Rename Button", type="default", on_click=rename_action, args=()):
        pass

if st.sidebar.button("About", key="about", help="About Button", type="default", on_click=about_action, args=()):
    pass
