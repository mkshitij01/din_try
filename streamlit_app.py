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

# Create clickable links in the sidebar
if st.sidebar.button("Home"):
    home_action()

if st.sidebar.button("Settings"):
    if st.sidebar.button("Edit"):
        edit_action()
    if st.sidebar.button("Rename"):
        rename_action()

if st.sidebar.button("About"):
    about_action()
