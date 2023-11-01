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

# Create clickable text links in the sidebar
if st.sidebar.markdown("[Home](#)"):
    home_action()

if st.sidebar.markdown("[Settings](#)"):
    if st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Edit](#)"):
        edit_action()
    if st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Rename](#)"):
        rename_action()

if st.sidebar.markdown("[About](#)"):
    about_action()
