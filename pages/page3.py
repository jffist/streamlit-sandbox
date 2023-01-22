import numpy as np
import pandas as pd
import streamlit as st

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

@st.cache
def generate_rand_data():
    x = np.arange(0,10)
    df = pd.DataFrame({"x":x, 
                    "y2": [i*i for i in x], 
                    "y3": [i**2.5 for i in x],
                    "word": np.random.choice(['a','bb','ccc'], size=len(x))})
    return df

df = generate_rand_data()
st.line_chart(df, x='x', y=['y2','y3'])
