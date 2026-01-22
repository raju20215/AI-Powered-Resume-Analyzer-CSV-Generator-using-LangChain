# AI-Powered Resume Analyzer & CSV Generator

## Overview

AI-Powered Resume Analyzer is an intelligent application designed to automate the tedious process of extracting structured information from bulk resumes. Built using LangChain and Google's Gemini AI, this tool transforms unstructured resume data into organized, downloadable CSV files, saving hours of manual work for HR teams and recruiters.

The application accepts a ZIP file containing multiple PDF resumes, processes each document using advanced natural language processing, and extracts key candidate information into a standardized format. This enables efficient candidate screening, comparison, and database management.

## Problem Statement

Recruiters and HR professionals face significant challenges when dealing with large volumes of resumes:

- **Time-Consuming Manual Review** - Reading through hundreds of resumes manually is inefficient and drains valuable time
- **Inconsistent Data Extraction** - Different resume formats, layouts, and styles make manual extraction error-prone
- **Lack of Structured Output** - Resumes come as unstructured documents, making analysis and comparison difficult
- **Scalability Issues** - Manual processing doesn't scale when dealing with bulk applications

## Solution

This AI-powered system solves these problems by:

1. **Automated Text Extraction** - Reads PDF resumes and extracts text content automatically
2. **Intelligent Information Parsing** - Uses Google's Gemini AI to understand and extract structured data
3. **Standardized Schema** - Enforces a consistent output format across all resumes
4. **Bulk Processing** - Handles multiple resumes simultaneously from a single ZIP file
5. **CSV Export** - Generates downloadable CSV files for easy integration with existing HR systems

## Features

### Structured Data Extraction

The application extracts the following information from each resume:

- **Full Name** - Candidate's complete name
- **Email Address** - Primary contact email
- **Phone Number** - Contact number
- **Location** - Current city/state/country
- **Total Years of Experience** - Overall work experience
- **Top Skills** - List of technical and professional skills
- **Education** - Highest degree and institution
- **Brief Summary** - Professional summary or objective

### User-Friendly Interface

- Clean, intuitive Streamlit interface
- Simple file upload for ZIP archives
- Real-time processing counter showing progress
- One-click CSV download
- No technical knowledge required

### Processing Workflow

1. Upload a ZIP file containing PDF resumes
2. Click "Process Resumes" to start extraction
3. Monitor progress as each resume is analyzed
4. Download the generated CSV file with all extracted data

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| AI Model | Google Gemini 2.0 Flash |
| LLM Framework | LangChain |
| PDF Processing | PyMuPDF (fitz) |
| Data Handling | Pandas |
| Environment Management | python-dotenv |

## Installation

### Prerequisites
- Python 3.8 or higher
- Google API Key for Gemini

### Setup Steps

1. Clone the repository
2. Install required packages:
```bash
pip install streamlit langchain-google-genai langchain-core python-dotenv pandas PyMuPDF
```

3. Create a `.env` file:
```
GOOGLE_API_KEY=your_google_api_key_here
```

4. Run the application:
```bash
streamlit run app.py
```

## Use Cases

- **Recruitment Agencies** - Process hundreds of applications quickly
- **Corporate HR Teams** - Screen candidates for job openings efficiently
- **Freelance Recruiters** - Deliver faster results to clients
- **Job Portals** - Automate candidate data entry
- **Career Services** - Help students organize application tracking

## Key Benefits

- **Time Savings** - Reduce hours of manual work to minutes
- **Accuracy** - AI-powered extraction minimizes human error
- **Scalability** - Process unlimited resumes without additional effort
- **Standardization** - Consistent data format across all candidates
- **Integration Ready** - CSV output works with existing tools and databases

## Future Enhancements

- Support for DOCX format resumes
- Multi-language resume processing
- Advanced filtering and search capabilities
- Direct integration with ATS systems
- Batch processing with email notifications
