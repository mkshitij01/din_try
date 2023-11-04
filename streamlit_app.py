import streamlit as st
import streamlit_antd_components as sac
import Home

with st.sidebar:
    
    Item_menu = sac.menu([
        sac.MenuItem('Home', icon='house-fill'),
        sac.MenuItem('link1', icon='send'),
        sac.MenuItem('link2', icon='send',),
        sac.MenuItem('Admin', icon='box-fill', children=[
            sac.MenuItem('Mappings', icon='apple', children=[
                sac.MenuItem('Create', icon='git'),
                sac.MenuItem('Edit', icon='git'),
            ]),
        ]),
        '''
        sac.MenuItem(type='divider'),
        sac.MenuItem('reference', type='group', children=[
            sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
            sac.MenuItem('bootstrap-icon', icon='bootstrap', href='https://icons.getbootstrap.com/'),'''
        ]),
    ], format_func='title', open_all=True)

if Item_menu == 'home':
    Home.app()
elif Item_menu == 'apple':
    st.write('yayaya')
