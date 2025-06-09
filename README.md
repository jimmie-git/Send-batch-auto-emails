# Bulk Email Sender

A simple Streamlit application for sending personalized bulk emails directly from a browser. It is designed to run entirely inside **GitHub Codespaces** so no desktop GUI is required.

## Step 1: Verify Repository Setup

Your repository should contain these files:

- `app.py` – the Streamlit application.
- `requirements.txt` – Python dependencies.
- `.env.example` – sample environment variable file for Gmail credentials.

Clone the repository or create a Codespace with these files in the project root.

## Step 2: Choose a Web Interface

This project uses **Streamlit** because it provides an easy way to build web apps with drag-and-drop file upload widgets and requires only a single command to start. It runs in the browser and works well inside Codespaces without extra configuration.

## Step 3: Set Up the Python Environment

Create a virtual environment and install the dependencies listed in `requirements.txt`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
streamlit>=1.34.0
pandas
openpyxl
python-dotenv
```

## Step 4: Run the Application

Provide your Gmail credentials either through environment variables or by editing a `.env` file based on `.env.example`:

```bash
export EMAIL_USER="youraddress@gmail.com"
export EMAIL_PASS="your_app_password"
```

Then start the Streamlit server (replace the port if 8080 is already in use):

```bash
streamlit run app.py --server.port 8080 --server.address 0.0.0.0
```

Open the **Ports** tab in Codespaces, expose port `8080`, and click **Open in
Browser** to view the interface.

## Step 5: Upload Data and Send Emails

1. Drag and drop a CSV or Excel file containing an `email` column. Optional `subject` and `message` columns can override the defaults.
2. If prompted, enter your Gmail address and app password.
3. Provide a subject and message if your file does not include them.
4. Click **Send Emails** to send messages via Gmail SMTP. A summary of successes and failures appears when done.

## Step 6: Example Data Format

Your upload should have at minimum an `email` column:

```csv
email,subject,message
person1@example.com,Hello,A personalized message here
person2@example.com,,Another message
```

The `subject` and `message` columns are optional. If omitted, the values you
enter in the app will be used for all recipients.

## Step 7: Deployment Options

The app works out of the box in Codespaces. To share it publicly you can deploy to services such as:

- **Streamlit Community Cloud** – free for small projects.
- **PythonAnywhere** – easy Python hosting with a free tier.
- **Render** – supports deploying Streamlit apps with environment variables.

Each platform requires setting `EMAIL_USER` and `EMAIL_PASS` as environment variables.

## Testing

Verify the code by compiling and launching the server:

```bash
python -m py_compile app.py
streamlit run app.py --server.port 8080 --server.address 0.0.0.0
```

Stop the server with `Ctrl+C` once you see the URL.
