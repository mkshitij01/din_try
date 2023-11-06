import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('Home')
    st.write('This is the `home page` of this multi-page app.')
    st.write('In this app, we will be building a simple classification model using the Iris dataset.')
    
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
