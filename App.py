import streamlit as st
from resume_parser import extract_text_from_pdf
from Analyzer import analyze_resume
from Job_Matcher import match_resume_with_job

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze your resume and compare it with a job description."
)

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "💼 Paste Job Description",
    height=300,
    placeholder="Paste the job description here..."
)


if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.success("Resume uploaded successfully!")

    with st.expander("📋 View Extracted Resume"):
        st.text_area(
            "Resume Text",
            resume_text,
            height=400
        )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🔍 Analyze Resume", use_container_width=True):

            with st.spinner("Analyzing resume..."):

                try:

                    analysis = analyze_resume(resume_text)

                    st.subheader("📊 Resume Analysis")

                    st.markdown(analysis)

                except Exception as e:

                    st.error(f"Analysis failed: {e}")

    with col2:

        if st.button(
            "🎯 Match Resume with Job",
            use_container_width=True
        ):

            if not job_description.strip():

                st.warning(
                    "Please paste a job description first."
                )

            else:

                with st.spinner(
                    "Comparing resume with job description..."
                ):

                    try:

                        result = match_resume_with_job(
                            resume_text,
                            job_description
                        )

                        st.subheader(
                            "🎯 Job Match Analysis"
                        )

                        st.markdown(result)

                    except Exception as e:

                        st.error(
                            f"Job matching failed: {e}"
                        )