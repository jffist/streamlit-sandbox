import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(20):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {(i+1)*5}')
  bar.progress((i+1)*5)
  time.sleep(0.15)

'...and now we\'re done ...almost...'

placeholder = st.empty()
msg = st.empty()
msg.text("wait for 5 sec")
time.sleep(5)

# Replace the placeholder with some text:
placeholder.text("Hello")
msg.text("wait for 5 sec again")
time.sleep(5)

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})
msg.text("wait for 5 sec again and again")
time.sleep(5)

# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")
msg.text("the last time to wait for 5 sec befor cleaning containers")
time.sleep(5)

# Clear all those elements:
placeholder.empty()
msg.empty()