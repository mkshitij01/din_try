import streamlit as st

# Create a sidebar navigation bar
st.sidebar.title("Sidebar Navigation")

# First-level buttons
if st.sidebar.button("Section 1"):
    st.write("You are in Section 1")
if st.sidebar.button("Section 2"):
    st.write("You are in Section 2")

# Second-level buttons with indentation
with st.sidebar:
    st.write("   ")  # Add some padding for indentation
    if st.button("Subsection 1"):
        st.write("You are in Subsection 1")

with st.sidebar:
    st.write("   ")  # Add some padding for indentation
    if st.button("Subsection 2"):
        st.write("You are in Subsection 2")
