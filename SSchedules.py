import streamlit_antd_components as sac
import streamlit as st
import pandas as pd

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


    df = pd.DataFrame(
        [
           {"command": st.write("<a href='https://www.google.com/'id='my-link'>Click me</a>", unsafe_allow_html=True), "rating": 4, "is_widget": True},
           {"command": "st.balloons", "rating": 5, "is_widget": False},
           {"command": "st.time_input", "rating": 3, "is_widget": True},
       ]
    )
    edited_df = st.experimental_data_editor(df)
    
    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
