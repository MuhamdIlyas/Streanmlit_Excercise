import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Cointainer dan Expander")
st.header("Container")
st.write("Untuk membuat container, kita bisa menggunakan notasi with dan diikuti function container()")

with st.container():
    st.write("Inside the container")

    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig)

st.write("Menggunakan notasi with dan diikuti dengan function expander(). bisa menggunakan expander untuk menampung penjelasan atau keterangan lanjutan dari sebuah visualisasi data yang ditampilkan dalam sebuah dashboard")
with st.expander("See explanation"):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    )
