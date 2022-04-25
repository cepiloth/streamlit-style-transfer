# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py
import streamlit as st
from PIL import Image

import style

def get_image_download_link(img,filename,text):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href
    
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
        result = Image.fromarray(output_image)
        st.markdown(get_image_download_link(result, img_file.name,'Download '+img_file.name), unsafe_allow_html=True)

