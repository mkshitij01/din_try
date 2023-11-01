import streamlit as st

# Create a dictionary to represent the navigation structure
navigation = {
    "Level 1 Link 1": {
        "Sublink 1": "/sublink1",
        "Sublink 2": "/sublink2",
    },
    "Level 1 Link 2": {
        "Sublink 3": "/sublink3",
    },
    "Level 1 Link 3": {
        "Sublink 4": "/sublink4",
        "Sublink 5": "/sublink5",
    },
}

# Create the navigation bar
st.sidebar.title("Navigation")

# Iterate through the Level 1 links and their sublinks
for level1_link, sublinks in navigation.items():
    st.sidebar.subheader(level1_link)

    # Create buttons for sublinks under the Level 1 link
    for sublink, link in sublinks.items():
        if st.sidebar.button(sublink):
            st.experimental_set_query_params(**{"page": link})

# Display content based on the selected link
if "page" in st.experimental_get_query_params():
    selected_page = st.experimental_get_query_params()["page"]
    st.write(f"Content for the selected page: {selected_page}")
