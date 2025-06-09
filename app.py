import os
import pandas as pd
import streamlit as st
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Configure the page
st.set_page_config(page_title="Bulk Email Sender")

# Automatically load EMAIL_USER and EMAIL_PASS from a .env file if present
load_dotenv()

st.title("Bulk Email Sender")

st.write(
    """
    Upload a CSV or Excel file with at least an `email` column. Optional
    `subject` and `message` columns let you personalize each email.
    If those columns are missing, you'll be asked for a subject and message
    to use for all recipients.
    """
)

# Input fields for Gmail credentials. If environment variables exist, they are
# pre-filled so the user does not need to type them each time.
email_user = st.text_input("Gmail address", value=os.getenv("EMAIL_USER", ""))
email_pass = st.text_input(
    "Gmail app password", value=os.getenv("EMAIL_PASS", ""), type="password"
)

# Drag-and-drop file uploader for recipient data
uploaded_file = st.file_uploader(
    "Drag and drop or choose a CSV or Excel file",
    type=["csv", "xlsx"],
)

if uploaded_file is not None:
    # Read the uploaded file into a pandas DataFrame
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    if "email" not in df.columns:
        st.error("The uploaded file must contain an `email` column")
        st.stop()

    st.write("Preview of uploaded data:")
    st.dataframe(df.head())

    # Default subject and message when the file lacks these columns
    default_subject = st.text_input("Email subject", "Hello from Streamlit")
    default_message = st.text_area("Email message", "")

    if st.button("Send Emails"):
        if not email_user or not email_pass:
            st.error("Please enter your Gmail address and app password")
        else:
            successes = 0
            failures = 0
            # Connect to Gmail's SMTP server using SSL
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
