import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_resume(resume_text):

    prompt = f"""
You are an expert technical recruiter and resume analyst.

Analyze the following resume and return a clear, structured analysis.

RESUME:
{resume_text}

Provide the following:

1. Candidate Name
2. Professional Summary
3. Technical Skills
4. Soft Skills
5. Work Experience
6. Education
7. Projects
8. Certifications
9. Key Strengths
10. Weaknesses or Areas for Improvement
11. Overall Resume Quality Score out of 100

Keep the analysis factual. Do not invent information that is not present
in the resume.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert resume analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

