import streamlit as st
from google import genai
from PIL import Image

API_KEY = "paste here your gemini api key here"

client = genai.Client(api_key=API_KEY)

st.set_page_config(page_title="Civil Engineering Insight Studio", layout="wide")

st.title("🏗 Civil Engineering Insight Studio")
st.markdown("AI-powered structural analysis using Gemini 2.5")
    
uploaded_file = st.file_uploader(
    "Upload Civil Engineering Structure Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=600)

    if st.button("Analyze Structure"):
        with st.spinner("Analyzing structure..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    "You are a professional civil engineer. "
                    "Analyze this structure in detail including "
                    "materials, structural type, components, "
                    "construction stage and observations.",
                    image
                ]
            )

            st.subheader("📋 Structural Report")
            st.write(response.text)
