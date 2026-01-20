import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import subprocess

OLLAMA_PATH = r"C:\Users\PC\AppData\Local\Programs\Ollama\ollama.exe"

def chunk_text(text, chunk_size=800, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

st.title("📄 AI Research Assistant")

files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

if files:
    docs = []
    for f in files:
        docs.append({"text": load_pdf(f), "source": f.name})

    chunks = []
    for d in docs:
        for c in chunk_text(d["text"]):
            chunks.append({"text": c, "source": d["source"]})

    texts = [c["text"] for c in chunks]
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    X = vectorizer.fit_transform(texts).toarray()

    question = st.text_input("Ask a question")

    if question:
        q_vec = vectorizer.transform([question]).toarray()
        scores = cosine_similarity(q_vec, X)[0]
        top_idx = np.argsort(scores)[-5:][::-1]

        context = "\n".join(chunks[i]["text"][:400] for i in top_idx)

        prompt = f"""
Answer academically using ONLY the context below.
Do not copy text.

Question: {question}

Context:
{context}

Answer:
"""

        result = subprocess.run(
            [OLLAMA_PATH, "run", "llama3"],
            input=prompt,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )

        st.subheader("🧠 Answer")
        st.write(result.stdout)
