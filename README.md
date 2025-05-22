# 📄 Resume Keyword Scanner

This is a simple and interactive Streamlit-based web app that analyzes your resume against a given job description and calculates a match score based on extracted keywords using NLP.

---

## 🚀 Features

- Upload your resume in PDF format
- Paste the job description
- Automatically extracts relevant keywords using NLTK
- Compares and calculates:
  - ✅ Matched keywords
  - ❌ Missing keywords
  - 🔢 Match score (%)
- Clean, user-friendly UI powered by Streamlit

---

## 🧠 Tech Stack

- Python 🐍
- Streamlit 🌐
- PyMuPDF (for PDF reading)
- NLTK (for natural language processing)

---

## 📦 Requirements

All dependencies are listed in the `requirements.txt` file.
streamlit
nltk
pymupdf




---

## 🛠️ Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/resume-keyword-scanner.git
cd resume-keyword-scanner

# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run resume_app.py


🌍 Deploy on Streamlit Cloud
Push your code to a public GitHub repository

Go to Streamlit Cloud

Click New App

Select your GitHub repo

Set the main file as resume_app.py

Deploy and done 🎉

📧 Contact
Created by Lohith Kukkadapu
Feel free to connect via LinkedIn or email: kukkadapulohith@gmail.com