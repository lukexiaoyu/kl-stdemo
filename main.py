import streamlit as st
import pandas as pd
import numpy as np

with open('./hello.js', 'r') as file:
    hello_content = file.read()



site_title="klpalace"
st.header(site_title,divider='rainbow')

st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

st.code(hello_content,language='javascript')


