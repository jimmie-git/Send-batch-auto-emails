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

2. **Provide Gmail credentials**
   You can either export environment variables or simply type them directly into
   the web interface. To avoid retyping every time, set environment variables or
   create a `.env` file with your Gmail address and an
   [app password](https://support.google.com/accounts/answer/185833):
   ```bash
   export EMAIL_USER="youraddress@gmail.com"
   export EMAIL_PASS="your_app_password"
   ```
   Copy `.env.example` to `.env` if you want to store them in a file.

3. **Run the app**
   ```bash
   streamlit run app.py --server.port 8080 --server.address 0.0.0.0
   ```
   In Codespaces, open the forwarded port (usually 8080) to view the Streamlit interface in your browser.


4. **Upload your data**
   Prepare a CSV or Excel file with at least an `email` column. Drag and drop
   it onto the uploader. Optional `subject` and `message` columns can override
   the subject and body you provide in the app.

## Using the Application

1. Open the forwarded port in your Codespace and you will see a simple web page.
2. Drag and drop your CSV or Excel sheet onto the uploader (or click **Browse files**).
3. Enter the subject and body of the email you want to send. If your file
   includes `subject` or `message` columns, those values override what you type.
4. Review the preview table to ensure your data looks correct and press
   **Send Emails**.

## Example Usage in Codespaces

Follow these steps in a brand-new Codespace to send your first batch of emails:

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Start the Streamlit app and forward the port when prompted:
   ```bash
   streamlit run app.py --server.port 8080 --server.address 0.0.0.0
   ```
3. In your browser, enter your Gmail address and app password in the fields at the top.
4. Drag and drop the CSV or Excel file containing your recipients.
5. Review the preview table and click **Send Emails** when ready.


## File Format Example

| email | subject | message |
|-------|---------|---------|
| alice@example.com | Hello | Hi Alice,\nthis is a test. |
| bob@example.com | Hi Bob | Dear Bob,\nwelcome! |

## Environment Variables

- `EMAIL_USER` – Gmail address used to send emails.
- `EMAIL_PASS` – Gmail app password for authentication.

You can copy `.env.example` to `.env` and fill in your values. These variables
are loaded automatically with `python-dotenv`, but they are optional because the
web interface also lets you enter them manually.

## Deployment Options

This app runs well in a Codespace. For public hosting you can deploy to services
like Streamlit Community Cloud, PythonAnywhere, or Render. Each platform may have
specific environment variable configuration steps.


## Testing

You can verify that the application starts correctly with:
```bash
python -m py_compile app.py
streamlit run app.py --server.port 8080 --server.address 0.0.0.0
```
Stop the server with `Ctrl+C` when you see the URL message.
