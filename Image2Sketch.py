import streamlit as st
import numpy as np
from PIL import Image
import cv2

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)


st.title("SketchLikePro App")
st.write("Photos to realistic Pencil Sketches")

File_image = st.sidebar.file_uploader("Upload your Image", type=['jpeg','jpg','png'])

if File_image is None:
    st.write("You haven't uploaded any Image")

else:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    st.write("**Input Image**")
    st.image(input_img, use_column_width=True)
    st.write("**Here is you awesome Pencil Sketch**")
    st.image(final_sketch, use_column_width=True)