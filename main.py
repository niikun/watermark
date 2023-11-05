import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import io
import base64

st.title("WaterMark")
st.write("ドラッグしてね")
uploaded_file=st.file_uploader("ファイルアップロード", type='png')

def add_text(image,text):
    base_img = image.copy()
    
    # 名前を描画するためのフォントとサイズを設定
    font = ImageFont.truetype("arial.ttf", 50)  # 'arial.ttf'はシステムにインストールされたフォントに置き換えてください
    draw = ImageDraw.Draw(base_img)
    
    # 名前を画像上に配置する位置を設定（x, y座標）
    text_positions = [(100, 100),(200, 200),(300, 300),(400, 400),(500, 500)]
    
    # 黒色でテキストを描画
    for text_position in text_positions:
        draw.text(text_position, text, font=font, fill="black")

    return base_img

def get_image_download_link(img, filename="output.png", text="ダウンロード"):
    buffered = io.BytesIO()
    img.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f'<a target="_blank" href="data:image/png;base64,{img_str}" download="{filename}">{text}</a>'


if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    st.image(img_array, caption='アップした画像', use_column_width=True)
    text = st.text_input(label="透かしで入れる文字を教えてください")
    
    if text:
        result = add_text(image, text)
        st.image(result, caption="透かしを入れた画像", use_column_width=True)
        st.markdown(get_image_download_link(result), unsafe_allow_html=True)