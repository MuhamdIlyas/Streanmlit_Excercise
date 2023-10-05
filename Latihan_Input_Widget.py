import pandas as pd
import datetime
import streamlit as st

st.title("Input Widget")

# Text input merupakan widget yang digunakan untuk memperoleh inputan berupa single-line text. Kita bisa menggunakan function text_input()
st.header("Text Input")
name = st.text_input(label='Nama Lengkap', value='')
st.write('Nama :', name)

# Text area merupakan widget yang memungkinkan pengguna untuk menginput multi-line text. Untuk membuat widget ini, streamlit telah menyediakan function bernama text_area()
st.header("Text Area")
text = st.text_area('Feedback')
st.write('Feedback :', text)

# Number Input merupakan widget yang digunakan untuk memperoleh inputan berupa angka dari pengguna. Anda dapat menggunakan contoh kode berikut untuk membuat number input widget menggunakan function number_input()
st.header("Number Input")
number = st.number_input(label='Umur')
st.write('Umur :', int(number), 'Tahun')

# Date input widget. Dapat membuat widget berupa tanggal menggunakan function date_input().
st.header("Date Input")
date = st.date_input(label='Tanggal lahir',
                     min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

# File Uploader memungkinkan untuk meng-upload sebuah berkas tertentu ke dalam web app. Membuat file uploader widget menggunakan function file_uploader()
st.header("File Uploader")

uploaded_file = st.file_uploader('Choose a CSV File')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# Camera input widget dapat digunakan untuk meminta user mengambil gambar melalui webcam sekaligus mengunggahnya.  Hal ini tentunya dilakukan dengan persetujuan pengguna. Camera input widget menggunakan function camera_input().
st.text('Erorr Belum Solve')
st.header("Camera Input")
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)
