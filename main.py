
import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in Secrets (Replit) or use st.secrets

st.set_page_config(page_title="Explain My Job", layout="centered")
st.title("🧠 Explain My Job")
st.caption("Simplify your job role for different audiences")

job_desc = st.text_area("📝 Paste your job description or role summary", height=200)

audience = st.selectbox(
    "🎯 Who should this be explained to?",
    ["A 10-year-old", "A non-tech recruiter", "A peer in another team", "A new joiner", "A CXO"]
)

if st.button("Explain"):
    with st.spinner("Generating explanation..."):
        prompt = f"Explain this job to {audience}:\n{job_desc}"
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert job explainer who simplifies roles."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        output = response.choices[0].message.content
        st.success("Here's the explanation:")
        st.write(output)
