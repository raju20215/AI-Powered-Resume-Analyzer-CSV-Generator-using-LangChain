import streamlit as st
import pandas as pd
import zipfile
import fitz
import os
import io
from typing import List, TypedDict
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
api_key = os.getenv("gemini")


class ResumeData(TypedDict):
    full_name: str
    email: str
    phone_number: str
    location: str
    total_years_experience: str
    top_skills: List[str]
    education: str
    brief_summary: str


def extract_text(pdf_bytes):
    text = ""
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 AI-Powered Resume Analyzer")
st.write("Upload a ZIP file containing PDF resumes to extract structured data.")

st.divider()

uploaded_file = st.file_uploader("Upload ZIP file containing resumes", type="zip")

if uploaded_file:
    if not api_key:
        st.error("API Key not found. Please check your .env file.")
    else:
        if st.button("Process Resumes", type="primary"):
            extracted_results = []

            with zipfile.ZipFile(uploaded_file, 'r') as z:
                filenames = [f for f in z.namelist() if f.lower().endswith('.pdf') and not f.startswith('__')]

                if not filenames:
                    st.warning("No PDF files found in the archive.")
                else:
                    llm = ChatGoogleGenerativeAI(
                        model="gemini-3-flash-preview",
                        google_api_key=api_key,
                        temperature=0
                    )

                    prompt = ChatPromptTemplate.from_messages([
                        ("system", "Extract structured details from the resume text. Use 'N/A' for missing fields."),
                        ("human", "{text}")
                    ])

                    chain = prompt | llm.with_structured_output(ResumeData)

                    total_files = len(filenames)
                    processed_count = 0
                    counter = st.empty()

                    for name in filenames:
                        processed_count += 1
                        counter.text(f"Processing {processed_count}/{total_files}: {name}")

                        with z.open(name) as f:
                            resume_text = extract_text(f.read())

                        response = chain.invoke({"text": resume_text})
                        data = dict(response)
                        data['filename'] = name
                        extracted_results.append(data)

                    counter.empty()

                    if extracted_results:
                        df = pd.DataFrame(extracted_results)

                        cols = ['filename'] + [c for c in df.columns if c != 'filename']
                        df = df[cols]

                        st.success(f"Successfully processed {len(extracted_results)} resumes!")

                        csv = df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="📥 Download CSV",
                            data=csv,
                            file_name="resume_analysis.csv",
                            mime="text/csv",
                            use_container_width=True
                        )