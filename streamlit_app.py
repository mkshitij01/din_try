import streamlit as st
import streamlit_antd_components as sac
import Home
import SSchedules

with st.sidebar:
    
    Item_menu = sac.menu([
        sac.MenuItem('Home', icon='house-fill'),
        sac.MenuItem('Schedules', icon='send'),
        sac.MenuItem('link2', icon='send',),
        sac.MenuItem('Admin', icon='box-fill', children=[
            sac.MenuItem('Mappings', icon='box-fill', children=[
                sac.MenuItem('Create', icon='git'),
                sac.MenuItem('Edit', icon='git'),
            ]),
        ]),
    ], format_func='title', indent=15, open_all=True)

if Item_menu == 'Home':
    Home.app()
elif Item_menu == 'Schedules':
    SSchedules.app()
elif Item_menu == 'link2':
    st.write('Link 2 was clicked!')
