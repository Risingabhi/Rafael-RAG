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

import streamlit as st
import PyPDF2

# Create a title for the app
st.title("File Upload Example")

# Add a file uploader widget with a label
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Display the filename and size
    st.write("File Uploaded Successfully!")
    st.write("File Details:")
    st.write("File Name:", uploaded_file.name)
    st.write("File Type:", uploaded_file.type)
    st.write("File Size:", uploaded_file.size, "bytes")

    # Read and display the content of the uploaded file
    st.write("Content:")
    if uploaded_file.type == "application/pdf":
        # For PDF files, read and display the text content
        pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
        num_pages = pdf_reader.getNumPages()
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            st.write(page.extract_text())
    elif uploaded_file.type == "text/plain":
        # For TXT files, read and display the text content
        text_content = uploaded_file.read().decode("utf-8")
        st.write(text_content)

    # Optionally, you can save the file to a temporary location or perform further processing.
    # For example, to save the file with the original filename:
    # with open(uploaded_file.name, "wb") as f:
    #     f.write(uploaded_file.getbuffer())

