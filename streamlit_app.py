import streamlit as st

# Define the sidebar layout
st.sidebar.header('Navigation')
navigation = st.sidebar.radio("Go to", ["Section 1", "Section 2"])

# Create a dictionary to map the sections to their content
sections = {
    "Section 1": "This is the content of Section 1. You can put any Streamlit elements here.",
    "Section 2": "This is the content of Section 2. You can put different content here.",
}

# Display the content based on the selected section
if navigation in sections:
    st.write(sections[navigation])
else:
    st.write("Welcome to the Streamlit multi-layer side navigation bar. Select a section from the sidebar.")

# Optionally, you can add more sections and content by extending the 'sections' dictionary.
