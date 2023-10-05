# Dataframe() merupakan function yang digunakan untuk menampilkan DataFrame sebagai sebuah tabel interaktif.
# Pada function ini, bisa mengatur ukuran dari table yang ingin ditampilkan menggunakan parameter width dan height.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# DataFrame
st.text('DataFrame.')
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.dataframe(data=df, width=500, height=150)

# Tabel
st.text('Tabel.')
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

# Metric
st.text('Metric.')
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# Json
st.text('Json.')
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})


# Latihan Chart
st.text('Latihan Chart.')
x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)
