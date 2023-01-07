import streamlit as st
import pandas as pd
import numpy as np

#st.write('Hello world!')
st.text('Hello world ++!')
phello = st.sidebar.checkbox('Personalised greetings')

# generating data in cahced funciton ensures that they are the same when users
# interacts with app
@st.cache
def generate_rand_data():
    x = np.arange(0,10)
    df = pd.DataFrame({"x":x, 
                    "y2": [i*i for i in x], 
                    "y3": [i**2.5 for i in x],
                    "word": np.random.choice(['a','bb','ccc'], size=len(x))})
    return df

df = generate_rand_data()
st.line_chart(df,x='x', y=['y2','y3'])

#st.write(df.head(3))
#st.table(df.head(3))
st.dataframe(df.head(5).style.highlight_max(axis=0))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)


@st.cache
def generate_map_data():
    return pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

if st.checkbox('Show me the map'):
    map_data = generate_map_data()
    st.map(map_data)

### widgets
x = st.slider('x',0,20,3)  # 👈 this is a widget
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

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
b = left_column.button('Press me!')
st.write(b)

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")