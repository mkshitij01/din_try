import streamlit as st
import streamlit_antd_components as sac
from files import Home

with st.sidebar:
    sac.menu([
        sac.MenuItem('home', icon='house-fill', Home.app()),
        sac.MenuItem('products', icon='box-fill', children=[
            sac.MenuItem('apple', icon='apple', tag=sac.Tag('USA', color='green', bordered=False)),
            sac.MenuItem('other', icon='git')
        ]),
        sac.MenuItem('disabled', icon='send', disabled=True),
        sac.MenuItem(type='divider'),
        sac.MenuItem('reference', type='group', children=[
            sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
            sac.MenuItem('bootstrap-icon', icon='bootstrap', href='https://icons.getbootstrap.com/'),
        ]),
    ], format_func='title', open_all=True)
    
if sac.MenuItem == 'home':
    st.write('yay')
