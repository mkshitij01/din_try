import streamlit as st

# Create the left-side navigation bar with hyperlinks
st.sidebar.markdown('[Home](#)')
st.sidebar.markdown('[Link1](#)')
st.sidebar.markdown('[Link2](#)')

# Create a dropdown for "Drop1" with hyperlinks
with st.sidebar.beta_expander("Drop1"):
    st.sidebar.markdown('[Link3](#)')
    st.sidebar.markdown('[Link4](#)')

# Create "Link4" outside the dropdown
st.sidebar.markdown('[Link4](#)')

# Create a dropdown for "Drop2" with hyperlinks
with st.sidebar.beta_expander("Drop2"):
    st.sidebar.markdown('[Link5](#)')
    st.sidebar.markdown('[Link6](#)')
