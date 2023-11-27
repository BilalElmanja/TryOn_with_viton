import streamlit as st
import os
from PIL import Image
import io
import warnings
warnings.filterwarnings('ignore')

# Streamlit page configuration
st.set_page_config(page_title='Virtual TryOn', layout='wide')

# Title for your app
st.title('Virtual TryOn Application')

# Creating main columns for input and output with horizontal spacing
input_col, output_col = st.columns([2, 2], gap='medium')

# Within the input column, creating sections for each image type
with input_col:
    st.header("Upload Person Image")
    person_image = st.file_uploader("Person Image", type=['jpg', 'png', 'jpeg'], key="person")
    if person_image is not None:
        st.image(person_image, caption='Person Image', width=250)

    st.header("Upload Clothing Image")
    clothing_image = st.file_uploader("Clothing Image", type=['jpg', 'png', 'jpeg'], key="clothing")
    if clothing_image is not None:
        st.image(clothing_image, caption='Clothing Image', width=250)

# Output column for the result
with output_col:
    if st.button('Try On'):
        if person_image is not None and clothing_image is not None:
            # Save and resize uploaded person image
            person_image = Image.open(io.BytesIO(person_image.read())).convert('RGB')  # Convert to RGB
            person_image = person_image.resize((768, 1024))
            person_image.save('person_image.jpg', 'JPEG')

            # Save and resize uploaded person image
            clothing_image = Image.open(io.BytesIO(clothing_image.read())).convert('RGB')  # Convert to RGB
            clothing_image = clothing_image.resize((768, 1024))
            clothing_image.save('clothing_image.jpg', 'JPEG')

            # Call your command line script or method
            os.system('python tryon_script.py person_image.jpg clothing_image.jpg output_image.jpg')

            # Display the resized person image
            st.image('person_image.jpg', caption='Resized Person Image')

            # Optionally display the output image
            # st.image('output_image.jpg', caption='Output Image')
    else:
        st.write('Upload images and click on "Try On" to see the results.')
