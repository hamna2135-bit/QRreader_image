import streamlit as st
import cv2

qcd = cv2.QRCodeDetector()

st.title("Web QRコードリーダー")
st.write(
    "ここに文章を入力"
)

qrcode = st.file_uploader("QRコード",type="image/*")

if qrcode is not None:
    st.image(qrcode)
    item = cv2.imread(qrcode.name)
    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(item)
    st.write(decoded_info)