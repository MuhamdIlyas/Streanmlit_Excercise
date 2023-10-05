# Button Widgets
import streamlit as st
st.title("Button Widget")

# Button merupakan widget untuk menampilkan tombol interaktif. Tombol tersebut dapat digunakan pengguna untuk melakukan aksi tertentu. Untuk membuat widget ini, kita bisa menggunakan function button()
st.header('Button Widget')
if st.button('Say Hello'):
    st.write('Hello There')

# Checkbox merupakan widget yang digunakan untuk menampilkan sebuah checklist untuk pengguna. Kita bisa menggunakan function checkbox() untuk membuat dan menampilkan checklist dalam streamlit app.
st.header('Checkbox')
agree = st.checkbox('I Agree')

if agree:
    st.write('Welcome to MyApp')

# Radio button merupakan widget yang memungkinkan pengguna untuk memilih satu dari beberapa pilihan yang ada. Untuk membuat widget bisa menggunakan function radio()
st.header('Radio Button')
st.text('Erorr Belum Solve')
# genre = st.radio(
#     label="What's your favorite movie genre",
#     options=('Comedy', 'Drama', 'Documentary'),
#     horizontal=False
# )

# Select box merupakan widget yang memungkinkan pengguna untuk memilih salah satu dari beberapa pilihan yang ada. Ia merupakan opsi alternatif dari radio button. Streamlit telah menyediakan function selectbox() untuk membuat select box widget
st.header('Select Box')
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Multiselect merupakan widget yang digunakan agar user dapat memilih lebih dari satu pilihan dari sekumpulan pilihan yang ada. Streamlit telah menyediakan function bernama multiselect().
st.header('Multiselecct')
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Slider merupakan widget yang memungkinkan pengguna untuk untuk memilih nilai (atau range nilai) dari sebuah range nilai yang telah ditentukan. Streamlit telah menyediakan function slider()
st.header('Slider')
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)
