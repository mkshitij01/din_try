import streamlit as st

# Create a sidebar
st.sidebar.title("Sidebar")

# Define the links and dropdowns
links = {
    "About": "#about",
    "Services": "#services",
    "Clients": "#clients",
    "Contact": "#contact",
}

# Dropdown for "Dropdown"
dropdown_links = {
    "Link 1": "#link1",
    "Link 2": "#link2",
    "Link 3": "#link3",
}

# Display the links
for text, link in links.items():
    st.sidebar.markdown(f"[{text}]({link})")

# Display the dropdown
with st.sidebar.expander("Dropdown"):
    for text, link in dropdown_links.items():
        st.sidebar.markdown(f"[{text}]({link})")

# Main content
st.title("Main Content")
st.write("This is the main content area.")
