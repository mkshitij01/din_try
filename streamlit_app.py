import streamlit as st

st.sidebar.title("Sidebar")

# Create a list of sidebar options
options = [
    "Home",
    "Setting",
    "Rename",
    "Edit",
]

# Create a dictionary to specify which options have sub-options
sub_options = {
    "Setting": ["Rename", "Edit"],
}

# Create a dictionary to specify the parent option for each sub-option
parent_option = {
    "Rename": "Setting",
    "Edit": "Setting",
}

selected_option = st.sidebar.selectbox("Select an option", options)

# If the selected option has sub-options, display them as a nested list
if selected_option in sub_options:
    st.sidebar.markdown("Options:")
    for option in options:
        if parent_option.get(option) == selected_option:
            st.sidebar.write(f"{option}")
