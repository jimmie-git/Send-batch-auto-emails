import os
import pandas as pd
import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Bulk Email Sender")

st.title("Bulk Email Sender")

st.write(
    """
Upload a CSV or Excel file with at least an `email` column. Optionally include
`subject` and `message` columns for personalized content.
    """
)

uploaded_file = st.file_uploader("Choose CSV or Excel file", type=["csv", "xlsx"])

email_user = os.getenv("EMAIL_USER")
email_pass = os.getenv("EMAIL_PASS")

if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Preview of uploaded data:")
    st.dataframe(df.head())

    if st.button("Send Emails"):
        if not email_user or not email_pass:
            st.error("EMAIL_USER and EMAIL_PASS environment variables must be set")
        else:
            successes = 0
            failures = 0
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                try:
                    server.login(email_user, email_pass)
                except Exception as e:
                    st.error(f"Failed to login: {e}")
                    st.stop()
                for _, row in df.iterrows():
                    msg = EmailMessage()
                    msg["From"] = email_user
                    msg["To"] = row.get("email")
                    msg["Subject"] = row.get("subject", "Hello from Streamlit")
                    body = row.get("message", "")
                    msg.set_content(body)
                    try:
                        server.send_message(msg)
                        successes += 1
                    except Exception as e:
                        failures += 1
                        st.write(f"Failed to send to {row.get('email')}: {e}")
            st.success(f"Sent {successes} emails with {failures} failures")
