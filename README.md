# Bulk Email Sender

This repository contains a simple Streamlit application that lets you send
personalized bulk emails directly from a web browser. The app is intended for
use inside GitHub Codespaces so no additional GUI tools are required.

## Quick Start

1. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Set Gmail credentials**
   You can either export environment variables with your Gmail address and an [app password](https://support.google.com/accounts/answer/185833)
   or simply type them into the Streamlit app when prompted.
   To use environment variables:
   ```bash
   export EMAIL_USER="youraddress@gmail.com"
   export EMAIL_PASS="your_app_password"
   ```

3. **Run the app**
   ```bash
   streamlit run app.py --server.port 8080 --server.address 0.0.0.0
   ```
   In Codespaces, open the forwarded port to view the Streamlit interface.

4. **Upload your data**
   Prepare a CSV or Excel file with at least an `email` column. Optional columns
   `subject` and `message` allow customizing each email. If those columns are not
   present you can provide a default subject and message in the app. Upload the
   file via the Streamlit interface and press **Send Emails**.

## File Format Example

| email | subject | message |
|-------|---------|---------|
| alice@example.com | Hello | Hi Alice,\nthis is a test. |
| bob@example.com | Hi Bob | Dear Bob,\nwelcome! |

## Environment Variables

- `EMAIL_USER` – Gmail address used to send emails.
- `EMAIL_PASS` – Gmail app password for authentication.

You can copy `.env.example` to `.env` and fill in your values if you prefer
using `python-dotenv`. Alternatively you can enter these credentials directly in
the Streamlit interface when prompted.

## Deployment Options

This app runs well in a Codespace. For public hosting you can deploy to services
like Streamlit Community Cloud, PythonAnywhere, or Render. Each platform may have
specific environment variable configuration steps.

