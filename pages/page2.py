import numpy as np
import pandas as pd
import streamlit as st

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

@st.cache
def get_chart_data():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    return chart_data

st.line_chart(get_chart_data())