import streamlit as st

# Sidebar navigation items
sidebar_items = {
    "Level 1 Item 1": ["Level 2 Item 1", "Level 2 Item 2"],
    "Level 1 Item 2": [],  # Empty list for level 2
}

# Sidebar title
st.sidebar.title("Sidebar Navigation")

# Level 1 selection
level1 = st.sidebar.selectbox("Select Level 1", list(sidebar_items.keys()))

# Level 2 selection (if level 1 item has sub-items)
level2 = st.sidebar.selectbox("Select Level 2", sidebar_items.get(level1, []))

# Content based on selections
st.write(f"Selected Level 1: {level1}")
st.write(f"Selected Level 2: {level2}")
