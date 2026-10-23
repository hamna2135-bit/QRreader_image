import streamlit as st
import cv2
import numpy as np

qcd = cv2.QRCodeDetector()

st.title("Web QRコードリーダー")
st.write("画像からQRコードを読み取ります。")
st.write("画像内にQRコードが複数あっても読み取りできます。")
st.write("ドット部分がデザインされたものではうまく読み取れない可能性があります。")

qrcode = st.file_uploader("QRコード",type="image/*")

if qrcode is not None:
    st.image(qrcode)
    file_bytes = np.frombuffer(qrcode.read(), np.uint8)
    item = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(item)
    st.write("処理結果")
    for deta in decoded_info:
        if deta == "":
            st.code("内容を読み取れませんでした",language=None)
        else:
            st.code(deta,language=None)