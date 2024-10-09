import streamlit as st

st.write("""
# Presentasi Wawancara
""")
st.markdown("<span style='color:red;'>**(_Kelompok Satu_)**</span>", unsafe_allow_html=True)
number = st.slider("**Bagaimana penilaian anda?**:blush:✨", 0, 10)

if number == 10:
    st.balloons()

if number == 10:
    st.markdown("<h3 style='text-align: center;'>Terima Kasih🤩</h3>", unsafe_allow_html=True)
elif 1 <= number <= 9: 
    st.markdown("<h3 style='text-align: center;'>Terima Kasih🙏</h3>", unsafe_allow_html=True)
