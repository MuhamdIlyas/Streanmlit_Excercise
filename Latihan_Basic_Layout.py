import streamlit as st

# Sidebar
st.title('Belajar Analisis Data')
st.write('Sidebar + Untuk menambahkan sebuah elemen atau widget ke dalam sidebar, kita bisa menggunakan notasi with yang diikuti sebuah object bernama sidebar yang telah disediakan oleh streamlit')

st.header('Coloumn')
col1, col2, col3 = st.columns(3)

st.write('Untuk membuat column dalam streamlit app, membuat object dari setiap kolom terlebih dahulu. Hal ini dapat dilakukan dengan memanfaatkan function columns(). Selanjutnya, menambahkan sebuah elemen atau widget ke dalam column tersebut menggunakan notasi with')

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with st.sidebar:

    st.text('Ini merupakan sidebar')

    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)

st.header("Setting Ukuran Coloumn")
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")


st.header("Tabs")
st.subheader("Erorr Belum Solve")
st.write(" columns yang sebelumnya kita bahas, untuk membuat tabs, kita harus membuat object dari setiap tab menggunakan function tabs() yang diikuti dengan list dari nama dari setiap tab")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")
