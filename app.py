from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os 
import PyPDF2
from PIL import Image
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')


#function to get gemini responece
def get_gemini_response(input):
    response=model.generate_content(input)
    return response.text
def input_pdf_text(upload_files):
    reader=PyPDF2.PdfReader(upload_files)
    text=''
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text
input_prompt="""

As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD (Job Description) and meticulously identify any missing keywords with utmost accuracy.

resume: {text}

description:{jd}

I want the response in the following structure:

The first line indicates the percentage match with the job description (JD).

The second line presents a list of missing keywords.

The third section provides a profile summary.

Mention the title for all the three sections.

While generating the response put some space to separate all the three sections."""

st.title("Resume ATS Tracker")
st.text_area("Paste JobDescribtion")
upload_files=st.file_uploader("Upload Your resume",type="pdf",help="Please Upload Your resume")
submit=st.button("submit")
if submit:
    if upload_files is not None:
        text=input_pdf_text(upload_files)
        response=get_gemini_response(input_prompt)
        st.subheader(response)