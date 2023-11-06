import streamlit_antd_components as sac
import streamlit as st

def app():
    st.title('Schedules')

    sac.tree(items=[
        sac.TreeItem('item1'),
        sac.TreeItem('item2'),
        sac.TreeItem('item3'),
        sac.TreeItem('item4'),
        sac.TreeItem('item5'),
        sac.TreeItem('item6'),
        sac.TreeItem('item7'),
        sac.TreeItem('item8'),
        sac.TreeItem('item9'),
        sac.TreeItem('item10'),
    ], label='label', index=0, format_func='title', checkbox=True, show_line=False, checkbox_strict=True, return_index=True)
