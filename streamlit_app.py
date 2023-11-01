import streamlit as st

# Create a sidebar navigation bar
st.sidebar.title("Sidebar Navigation")

# Define the CSS for styling the buttons
button_css = "
<style>
.stButton {
    width: 100%;
    text-align: left;
    padding-left: 30px;
    margin-bottom: 10px;
}

.stButton.subsection {
    margin-left: 20px;
}
</style>
"

st.sidebar.markdown(button_css, unsafe_allow_html=True)

# First-level buttons
if st.sidebar.button("Section 1"):
    st.write("You are in Section 1")
if st.sidebar.button("Section 2"):
    st.write("You are in Section 2")

# Second-level buttons with increased margin for indentation
with st.sidebar:
    if st.button("Subsection 1", key="subsection1", class="subsection"):
        st.write("You are in Subsection 1")

with st.sidebar:
    if st.button("Subsection 2", key="subsection2", class="subsection"):
        st.write("You are in Subsection 2")
