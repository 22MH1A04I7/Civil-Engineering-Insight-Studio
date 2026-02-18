# 🏗 Civil Engineering Insight Studio

AI-Powered Structural Analysis System  
Internship Project – 2026  

---

## 🔍 Overview

Civil Engineering Insight Studio is an AI-driven web application designed to automate structural image analysis in civil engineering projects.

The system leverages Google Gemini Multimodal Models to analyze uploaded images of construction sites, buildings, and infrastructure, and generates structured engineering insights in JSON format.

This project demonstrates the integration of Generative AI with civil engineering workflows to improve documentation efficiency and technical reporting.

---

## 🎯 Project Objective

To develop an intelligent system that:

- Analyzes civil engineering structural images
- Identifies visible materials and components
- Detects construction stages
- Generates structured engineering reports
- Reduces manual documentation effort

---

## 🚀 Key Features

✔ Image Upload Support (JPG, JPEG, PNG)  
✔ Strict Engineering Mode (No assumptions allowed)  
✔ Estimation Mode (Professional inference permitted)  
✔ Structured JSON Output  
✔ Interactive Web Interface (Streamlit)  
✔ Multimodal AI Processing (Image + Prompt)  

---

## 🧠 AI Model Used

Gemini 2.5 Flash (Multimodal Model)

Capabilities:
- Image understanding
- Text reasoning
- Structured output generation
- Engineering-focused prompt handling

---

## 🛠 Technology Stack

- Python 3.13
- Streamlit 1.54.0
- Google GenAI SDK 1.63.0
- Pillow 12.1.1
- JSON

---

## 🏗 System Architecture

User Uploads Image  
        ↓  
Streamlit Frontend  
        ↓  
Prompt Engineering Layer  
        ↓  
Gemini Multimodal API  
        ↓  
Structured JSON Response  
        ↓  
Engineering Report Display  

---

## 📂 Project Structure

CE_Insight_V2/
│
├── app.py
├── requirements.txt
└── README.md

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
git clone <your-repository-link>
cd CE_Insight_V2

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Add Gemini API Key

Inside `app.py`, replace:
client = genai.Client(api_key="YOUR_API_KEY")


With your actual Gemini API key.

You can generate API key from:
https://aistudio.google.com/app/apikey


### 4️⃣ Run the Application

streamlit run app.py

Open in browser:http://localhost:8501



## 📊 Output Format

The system generates structured JSON output:
{
"structure_type": "",
"construction_stage": "",
"visible_materials": [],
"structural_components": [],
"construction_methods": "",
"dimensions": "",
"engineering_observations": "",
"confidence_note": ""
}



## 🔐 Security Note

Never share your API key publicly.  
If exposed, immediately revoke and regenerate it.


## 📌 Internship Information

Project Title: Civil Engineering Insight Studio  
Domain: Civil Engineering + Generative AI  
Type: AI-based Web Application  
Year: 2026  


## 📈 Future Enhancements

- BIM Integration
- Structural defect detection
- PDF report export
- Cloud deployment
- Mobile compatibility
- Multi-image comparative analysis


## 👨‍💻 Developed As Part of Internship Program – 2026

Civil Engineering & AI Integration Project

