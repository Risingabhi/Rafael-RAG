import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



#choose option at top
#1 Professor's Assistant
#2 Student's Assistant


image = Image.open('infolab.PNG')

st.image(image, caption='Introducing RAG powered by Ai')

st.checkbox("Professor's Assistant")
st.checkbox("Student's Assistant")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.button('Upload Doc')
title = st.text_input('Your Query Here', 'Write your query')
st.write('You asked Ai', title)
st.button('send')
