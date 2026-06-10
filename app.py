import streamlit as st
st.set_page_config(page_title="AI Phishing Detector")
st.title("🔒 AI Powered Phishing Email Detector")
email_text = st.text_area(
    "Paste suspicious email content here"
)
if st.button("Analyze Email"):
    suspicious_words = [
        "verify",
        "urgent",
        "login",
        "password",
        "bank",
        "account suspended",
        "click here",
        "limited time",
        "update account",
        "security alert"
    ]
    found_words = []
    for word in suspicious_words:
        if word.lower() in email_text.lower():
            found_words.append(word)
    risk_score = min(len(found_words) * 15, 100)
    if risk_score >= 70:
        threat_level = "High"
        phishing_status = "Likely Phishing"
    elif risk_score >= 40:
        threat_level = "Medium"
        phishing_status = "Suspicious"
    else:
        threat_level = "Low"
        phishing_status = "Likely Safe"
    st.success("Analysis Complete")
    st.write("### Analysis Report")
    st.write(f"**Phishing Status:** {phishing_status}")
    st.write(f"**Risk Score:** {risk_score}/100")
    st.write(f"**Threat Level:** {threat_level}")
    st.write("**Indicators Found:**")
    if found_words:
        for item in found_words:
            st.write(f"- {item}")
    else:
        st.write("No suspicious indicators found.")
    st.write("**Recommendations:**")
    st.write("- Do not click unknown links.")
    st.write("- Verify sender identity.")
    st.write("- Avoid sharing passwords.")
    st.write("- Report suspicious emails.")