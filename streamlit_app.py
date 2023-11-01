import streamlit as st

# Define a custom component for the sidebar with dropdown
def sidebar_with_dropdown():
    st.sidebar.markdown("[Home](#)")
    st.sidebar.markdown("[Link1](#)")
    st.sidebar.markdown("[Link2](#)")

    with st.sidebar.beta_expander("Drop1"):
        st.sidebar.markdown("[Link3](#)")
        st.sidebar.markdown("[Link4](#)")

    st.sidebar.markdown("[Link4](#)")

    with st.sidebar.beta_expander("Drop2"):
        st.sidebar.markdown("[Link5](#)")
        st.sidebar.markdown("[Link6](#)")

# Use the custom component
sidebar_with_dropdown()
