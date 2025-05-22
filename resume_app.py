import streamlit as st
import fitz  # PyMuPDF
import re
import nltk
from nltk import word_tokenize, pos_tag

# ===== Download required NLTK resources =====
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# ===== Extract text from PDF =====
def extract_text_from_pdf(uploaded_file):
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            return " ".join(page.get_text() for page in doc)
    except Exception as e:
        st.error(f"PDF Extraction Error: {e}")
        return ""

# ===== Clean text =====
def clean_text(text):
    return re.sub(r"[^\w\s]", "", text).lower()

# ===== Extract keywords from job description =====
def extract_keywords_from_text(text):
    try:
        tokens = word_tokenize(text)
        tagged = pos_tag(tokens)
        keywords = [word.lower() for word, pos in tagged if pos.startswith('NN') and len(word) > 2 and word.isalpha()]
        return list(set(keywords))
    except Exception as e:
        st.error(f"Keyword Extraction Error: {e}")
        return []

# ===== Match keywords =====
def match_keywords(resume_text, keywords_list):
    resume_words = set(resume_text.split())
    keywords = set([kw.lower() for kw in keywords_list])

    matched = sorted(list(resume_words & keywords))
    missing = sorted(list(keywords - resume_words))
    score = int((len(matched) / len(keywords)) * 100) if keywords else 0

    return matched, missing, score

# ===== Streamlit UI =====
st.set_page_config(page_title="Resume Keyword Scanner", page_icon="📄")
st.title("📄 Resume Keyword Scanner")
st.markdown("Upload your **resume (PDF)** and paste the **job description** to see how well you match!")

uploaded_file = st.file_uploader("📁 Upload Resume (.pdf)", type=["pdf"])
jd_text = st.text_area("📝 Paste Full Job Description", height=250)

if st.button("🔍 Analyze"):
    if not uploaded_file:
        st.error("Please upload a resume.")
    elif not jd_text.strip():
        st.error("Please enter the job description.")
    else:
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            if not resume_text:
                st.stop()

            cleaned_resume = clean_text(resume_text)
            extracted_keywords = extract_keywords_from_text(jd_text)

            if not extracted_keywords:
                st.warning("No valid keywords found in job description.")
                st.stop()

            matched, missing, score = match_keywords(cleaned_resume, extracted_keywords)

            st.success(f"✅ Match Score: {score}%")
            col1, col2 = st.columns(2)

            with col1:
                st.metric("Matched Keywords", len(matched))
                st.write(", ".join(matched) if matched else "None")

            with col2:
                st.metric("Missing Keywords", len(missing))
                st.write(", ".join(missing) if missing else "None")

            st.divider()
            with st.expander("📋 Extracted Keywords from Job Description"):
                st.write(", ".join(extracted_keywords))
