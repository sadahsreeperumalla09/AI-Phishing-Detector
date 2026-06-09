import streamlit as st
import google.generativeai as genai
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
st.set_page_config(page_title="AI Phishing Detector")
st.title("🔒 AI Powered Phishing Email Detector")
email_text = st.text_area(
    "Paste suspicious email content here"
)
if st.button("Analyze Email"):
    prompt = f"""
    Analyze the email.
    Return:
    1. Phishing Status
    2. Risk Score out of 100
    3. Threat Level
    4. Indicators Found
    5. Recommendations
    Email:
    {email_text}
    """
    response = model.generate_content(prompt)
    st.success("Analysis Complete")
    st.write(response.text)