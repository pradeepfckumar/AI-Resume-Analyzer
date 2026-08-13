# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer that analyzes resumes and compares them with job descriptions using **Groq LLMs**.

The application allows users to upload a resume in PDF format, extract the resume content, analyze the candidate's profile, and evaluate how well the resume matches a specific job description.

---

## 🚀 Features

### 📄 Resume Analysis

Upload a PDF resume and get an AI-generated analysis covering:

- Candidate name
- Professional summary
- Technical skills
- Soft skills
- Work experience
- Education
- Projects
- Certifications
- Strengths
- Areas for improvement
- Overall resume quality score

### 🎯 Job Description Matching

Compare a resume against a specific job description and receive:

- Overall job match score
- Matching skills
- Missing skills
- Experience match
- Relevant projects
- Candidate strengths
- Skill gaps
- Improvement recommendations
- Important ATS keywords

### 🧠 AI-Powered Analysis

The application uses **Groq API** with the **Llama 3.3 70B Versatile** model for resume analysis and job matching.

### 🐳 Docker Support

The application can be containerized and run using Docker.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — Frontend/UI
- **PyMuPDF** — PDF text extraction
- **Groq API** — LLM inference
- **Llama 3.3 70B Versatile** — AI model
- **python-dotenv** — Environment variable management
- **Docker** — Containerization

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── App.py
├── analyzer.py
├── job_matcher.py
├── resume_parser.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
