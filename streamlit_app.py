import streamlit as st

st.title("Web QRコードリーダー")
st.write(
    "ここに文章を入力"
)

qrcode = st.file_uploader("QRコード",type="image/*")

if qrcode is not None:
    st.image(qrcode,width=50)