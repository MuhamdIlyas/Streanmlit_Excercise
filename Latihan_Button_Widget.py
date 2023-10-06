# Button Widgets
import streamlit as st
st.title("Button Widget")

# Button
st.header('Button Widget')
st.write('Button merupakan widget untuk menampilkan tombol interaktif. Tombol tersebut dapat digunakan pengguna untuk melakukan aksi tertentu. Untuk membuat widget ini, kita bisa menggunakan function button()')
if st.button('Say Hello'):
    st.write('Hello There')

# Checkbox
st.header('Checkbox')
st.write('Checkbox merupakan widget yang digunakan untuk menampilkan sebuah checklist untuk pengguna. Kita bisa menggunakan function checkbox() untuk membuat dan menampilkan checklist dalam streamlit app.')
agree = st.checkbox('I Agree')

if agree:
    st.write('Welcome to MyApp')

# Radiobutton
st.header('Radio Button')
st.write('Radio button merupakan widget yang memungkinkan pengguna untuk memilih satu dari beberapa pilihan yang ada. Untuk membuat widget bisa menggunakan function radio()')
st.text('Erorr Belum Solve')
# genre = st.radio(
#     label="What's your favorite movie genre",
#     options=('Comedy', 'Drama', 'Documentary'),
#     horizontal=False
# )

# SelectBox
st.header('Select Box')
st.write('Select box merupakan widget yang memungkinkan pengguna untuk memilih salah satu dari beberapa pilihan yang ada. Ia merupakan opsi alternatif dari radio button. Streamlit telah menyediakan function selectbox() untuk membuat select box widget')
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Multiselect
st.header('Multiselecct')
st.write('ultiselect merupakan widget yang digunakan agar user dapat memilih lebih dari satu pilihan dari sekumpulan pilihan yang ada. Streamlit telah menyediakan function bernama multiselect().')
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Slidebar
st.header('Slider')
st.write('Slider merupakan widget yang memungkinkan pengguna untuk untuk memilih nilai (atau range nilai) dari sebuah range nilai yang telah ditentukan. Streamlit telah menyediakan function slider()')
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)
