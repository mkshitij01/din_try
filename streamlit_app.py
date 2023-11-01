import streamlit as st

# Create a sidebar
st.sidebar.title("Sidebar")

# Dropdown menu for Section 1
section_1 = st.sidebar.selectbox("Section 1", ["Option 1", "Option 2", "Option 3"])

# Dropdown menu for Section 2
section_2 = st.sidebar.selectbox("Section 2", ["Option A", "Option B", "Option C"])

# Display content based on the selected dropdown options
st.write("Selected Section 1 option:", section_1)
st.write("Selected Section 2 option:", section_2)
