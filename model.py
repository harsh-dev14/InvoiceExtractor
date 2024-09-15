import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def geminiResponse(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_data(image):
    if image is not None:
        img_byte_array = BytesIO()
        image.save(img_byte_array, format=image.format)  # Save image to byte array
        bytes_data = img_byte_array.getvalue()  # Get byte data
        image_parts = [
            {
                "mime_type": f"image/{image.format.lower()}",  # Get image format for mime type
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No image uploaded")

st.set_page_config(page_title="Invoice Extractor")

st.header("Invoice Extracter")
input=st.text_input("Input Prompt: ", key="input")
uploaded_file=st.file_uploader("Choose an invoice to upload!!", type=["jpeg","jpg","png","heic"])

img=""
if uploaded_file is not None:
    img=Image.open(uploaded_file)
    st.image(img,caption="Preview of Uploaded Image", use_column_width=True)

submit=st.button("Tell me about the invoice!!")

input_prompt="You are and invoice extractor expert. We will upload an inovice image and you will anser all the quetions based on the uploaded image."

if submit:
    image_data=input_image_data(img)
    response=geminiResponse(input_prompt,image_data,input)
    st.subheader("Response")
    st.write(response)