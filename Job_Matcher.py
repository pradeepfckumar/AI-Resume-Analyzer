import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def match_resume_with_job(resume_text, job_description):

    prompt = f"""
You are an expert technical recruiter and ATS analyst.

Compare the candidate's resume with the provided job description.

================ RESUME ================
{resume_text}

================ JOB DESCRIPTION ================
{job_description}

Analyze the match and provide:

## 🎯 Overall Match Score
Give a score from 0 to 100.

## ✅ Matching Skills
List skills present in both the resume and job description.

## ❌ Missing Skills
List important skills required by the job description that are
not clearly present in the resume.

## 💼 Experience Match
Explain how well the candidate's experience matches the role.

## 📂 Project Match
Identify relevant projects from the resume.

## 💪 Candidate Strengths
Explain the strongest areas for this particular job.

## ⚠️ Skill Gaps
Explain the most important gaps.

## 📈 Recommendations
Give specific recommendations to improve the candidate's chances
for this role.

## 🤖 ATS Keywords
List important keywords from the job description that should
naturally appear in the resume if they accurately represent
the candidate's experience.

Important rules:
- Only use information actually present in the resume.
- Do not invent experience or skills.
- Do not claim the candidate has a skill simply because it appears
  in the job description.
- Be objective and concise.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert technical recruiter, "
                    "ATS analyst, and career advisor."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content