# Resume ATS Tracker

## Overview
Resume ATS Tracker is a Streamlit application designed to analyze resumes against job descriptions using a Generative AI model (Gemini). The tool evaluates the compatibility of resumes with job descriptions by:
- Assigning a matching percentage.
- Identifying missing keywords.
- Providing a detailed profile summary.

## Features
- Upload PDF resumes for evaluation.
- Generate detailed analysis of resumes using Google Generative AI.
- Offers precise recommendations for resume improvement.

## Requirements Specification

### Libraries to Install
Ensure you have the following Python libraries installed:
- streamlit
- streamlit_extras
- google-generativeai
- python-dotenv
- PyPDF2
- Pillow

### Installation
Install the required libraries using pip install streamlit,streamlit-extras,google-generativeai

###How to Use
Clone the repository and navigate to the project directory.
Create a .env file in the root directory and add your Google API Key:
GOOGLE_API_KEY=your_google_api_key
Run the Streamlit application:
streamlit run app.py
Paste the job description into the text area provided in the UI.
Upload your resume (PDF format only).
Click the "Submit" button to receive the analysis.

###Code Structure

The application performs the following steps:

1. Loads the environment variables using python-dotenv

2. Configures the Gemini Al model with the API key.

3. Extracts text from uploaded PDF resumes using PyPDF2.

4. Sends the resume text and job description as input prompts to the Al model.

5. Displays the Al-generated response, including:

 . Percentage match.

 . Missing keywords.

 . Profile summary
