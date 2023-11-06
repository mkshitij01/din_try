import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('Home')
    st.write('This is the `home page` of this multi-page app.')
    st.write('In this app, we will be building a simple classification model using the Iris dataset.')

    col1, col2 = st.columns(2)

    with col1:
        st.header('Bar Chart')
        chart_data = pd.DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])
        st.bar_chart(chart_data)

    with col2:
        st.header('Line Chart')
        chart_data = pd.DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])
        st.line_chart(chart_data)

    chart_data = pd.DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
