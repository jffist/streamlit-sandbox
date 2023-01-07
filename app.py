import streamlit as st
import pandas as pd
import numpy as np

#st.write('Hello world!')
st.text('Hello world ++!')
phello = st.sidebar.checkbox('Personalised greetings')


x = np.arange(0,10)
df = pd.DataFrame({"x":x, 
                  "y2": [i*i for i in x], 
                  "y3": [i**2.5 for i in x],
                  "word": np.random.choice(['a','bb','ccc'], size=len(x))})
st.line_chart(df,x='x', y=['y2','y3'])

#st.write(df.head(3))
#st.table(df.head(3))
st.dataframe(df.head(5).style.highlight_max(axis=0))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

if st.checkbox('Show me the map'):
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)

### widgets
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


if phello:
    st.text_input("Your name", key="the_cool_name")
    # You can access the value at any point with:
    st.write(f"Hello {st.session_state.the_cool_name}!!!")


option = st.selectbox(
    'Which word do you like best?',
     df['word'].unique())

'You selected: ', option

categories = {
    'cat1': ['sub11','sub12'],
    'cat2': ['sub21','sub22','sub23'],
    'cat3': []
}
tcat = st.selectbox("choose category:", categories.keys())
tsubcat = st.selectbox("choose subcategory:", categories[tcat])
st.write(f"Your tcats: {tcat}/{tsubcat}")

