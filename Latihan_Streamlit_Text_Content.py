import streamlit as st
import pandas as pd

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

#  Markdown
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# Title
st.title("Belajar Analisis Data")

# Header
st.header('Pengembangan Dashboard')

# Subheader
st.subheader('Pengembangan Dashboard (Subheader)')

# Caption
st.caption('Copyright (c) 2023')

# Code
code = """def hello(): print("Hello, Streamlit!")"""
st.code(code, language='python')

# Text
st.text('Halo, Calon Praktisi Data Masa Depan.')

# Latex
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")
