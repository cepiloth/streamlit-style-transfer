# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py
import streamlit as st
from PIL import Image

import style
    
col1, col2, = st.columns(2)

img = st.sidebar.selectbox(
    'Select Image',
    ('amber.jpg', 'cat.png')
)

style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)


model= "/app/streamlit-style-transfer/neural_style/saved_models/" + style_name + ".pth"
input_image = "/app/streamlit-style-transfer/neural_style/images/content-images/" + img
output_image = "/app/streamlit-style-transfer/neural_style/images/output-images/" + style_name + "-" + img

with col1:
    image = Image.open(input_image)
    st.image(image, caption='Source Image', use_column_width=True) # image: numpy array
    clicked = st.button('Stylize')
    
with col2:
    if clicked:
        model = style.load_model(model)
        style.stylize(model, input_image, output_image)

        image = Image.open(output_image)
        st.image(image, caption='Output Image', use_column_width=True)
        btn = st.download_button(
          label="Download image",
          data=img,
          file_name="imagename.png",
          mime="image/png")

