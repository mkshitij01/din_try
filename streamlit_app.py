import streamlit as st
import streamlit_antd_components as sac
import Home

with st.sidebar:
    
    Item_menu = sac.menu([
        sac.MenuItem('Home', icon='house-fill'),
        sac.MenuItem('link1', icon='send'),
        sac.MenuItem('link2', icon='send',),
        sac.MenuItem('Admin', icon='box-fill', children=[
            sac.MenuItem('Mappings', icon='box-fill', children=[
                sac.MenuItem('Create', icon='git'),
                sac.MenuItem('Edit', icon='git'),
            ]),
        ]),
    ], format_func='title', open_all=True)

if Item_menu == 'home':
    Home.app()
elif Item_menu == 'link1':
    st.write('yayaya')
