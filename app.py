import streamlit as st
import qrcode
from datetime import datetime, timedelta
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="QR코드 생성기", layout="centered")

st.title("📱 인적사항 기반 QR코드 생성기")
st.write("아래 항목을 입력하면 자동으로 QR코드를 생성합니다. (만료기한: 1개월)")

# 사용자 입력 받기
name = st.text_input("이름")
birth = st.text_input("생년월일 (예: 1990-01-01)")
phone = st.text_input("전화번호")
address = st.text_input("주소")

if st.button("✅ QR코드 생성"):
    if not (name and birth and phone and address):
        st.warning("모든 항목을 입력해주세요.")
    else:
        today = datetime.today()
        expiry = today + timedelta(days=30)

        qr_data = (
            f"이름: {name}\n"
            f"생년월일: {birth}\n"
            f"전화번호: {phone}\n"
            f"주소: {address}\n"
            f"생성일: {today.strftime('%Y-%m-%d')}\n"
            f"만료일: {expiry.strftime('%Y-%m-%d')}"
        )

        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer)
        buffer.seek(0)
        qr_image = Image.open(buffer)

        st.image(qr_image, caption="생성된 QR코드", use_column_width=True)

        # 다운로드 버튼
        st.download_button(
            label="📥 QR코드 다운로드",
            data=buffer,
            file_name=f"{name}_qr.png",
            mime="image/png"
        )