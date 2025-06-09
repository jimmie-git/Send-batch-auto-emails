import os
import pandas as pd
import streamlit as st
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load variables from a .env file if present
load_dotenv()

st.set_page_config(page_title="Bulk Email Sender")

st.title("Bulk Email Sender")

st.write(
    """
Upload a CSV or Excel file with at least an `email` column. You can also
optionally include `subject` and `message` columns for personalized content.
If these columns are missing you can supply defaults below.
    """
)

# Allow the user to provide Gmail credentials in the UI, prefilled from env vars
email_user = st.text_input("Gmail address", value=os.getenv("EMAIL_USER", ""))
email_pass = st.text_input(
    "Gmail app password", value=os.getenv("EMAIL_PASS", ""), type="password"
)

# Optional defaults if the uploaded file lacks these columns
default_subject = st.text_input("Default subject", "Hello from Streamlit")
default_message = st.text_area("Default message", "")

uploaded_file = st.file_uploader("Choose CSV or Excel file", type=["csv", "xlsx"])

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
            st.error("Please provide your Gmail address and app password.")
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
                    msg["Subject"] = row.get("subject", default_subject)
                    body = row.get("message", default_message)
                    msg.set_content(body)
                    try:
                        server.send_message(msg)
                        successes += 1
                    except Exception as e:
                        failures += 1
                        st.write(f"Failed to send to {row.get('email')}: {e}")
            st.success(f"Sent {successes} emails with {failures} failures")
