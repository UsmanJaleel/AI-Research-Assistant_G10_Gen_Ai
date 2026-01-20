# AI Research Assistant – Cross-Document Knowledge Synthesis

This project implements a **Generative AI–based research assistant** designed to help **students and researchers** explore, retrieve, and synthesize information from multiple academic PDF documents.

Unlike traditional PDF question-answering tools that focus on a single document, this system supports **cross-document retrieval and knowledge synthesis**, enabling users to understand recurring concepts, shared themes, and connections across multiple sources.

---

## 🎯 Project Goals

* Enable **semantic search** across multiple academic PDFs
* Support **cross-document understanding**, not isolated answers
* Provide **transparent, inspectable steps** for learning and evaluation
* Work **offline and locally** without reliance on paid APIs

---

## 👥 Target Users

* University students
* Researchers
* Academic project groups

These users often work with **lecture slides, research papers, and notes in PDF format** and need help finding, connecting, and summarizing information efficiently.

---

## 🧠 System Overview

The system follows a **retrieval-augmented generation (RAG-inspired)** pipeline:

1. **PDF Upload**
   Users upload one or more academic PDF documents.

2. **Text Extraction & Chunking**
   PDFs are parsed and split into overlapping text chunks for fine-grained retrieval.

3. **Embedding (Offline)**
   TF-IDF vectorization is used to create semantic representations of each chunk.

4. **Cross-Document Retrieval**
   Cosine similarity retrieves relevant chunks across *all* uploaded documents.

5. **Knowledge Synthesis**
   Retrieved passages are combined to highlight shared ideas and concepts.

6. **LLM-Based Answering**
   A **local LLM (LLaMA 3 via Ollama)** generates answers strictly grounded in the retrieved content.

---

## 🖥️ User Interface

### Jupyter Notebook (Primary Interface)

The Jupyter Notebook serves as an **interactive and transparent interface** where users can:

* Inspect retrieved document chunks
* See which PDFs contributed to an answer
* Experiment with queries and retrieval parameters

This interface fits naturally into academic workflows and supports **learning, experimentation, and reproducibility**.

### Demo Web App (Streamlit)

A lightweight **Streamlit demo app** is included to demonstrate:

* PDF upload via browser
* Natural-language question input
* Document-grounded answers

This showcases how the system could be deployed beyond notebooks.

## How to Run the Demo App

```bash
pip install streamlit pypdf scikit-learn
streamlit run app.py


---

## 🛠️ Technologies Used

* **Python 3.11**
* **PyPDF** – PDF parsing
* **scikit-learn** – TF-IDF vectorization and cosine similarity
* **Ollama + LLaMA 3** – Local LLM for answer generation
* **Jupyter Notebook** – Main interface
* **Streamlit** – Demo web application

---

## ⚠️ Design Decisions

* **Offline embeddings (TF-IDF)** were chosen to:

  * Avoid API quotas and costs
  * Ensure reproducibility
  * Keep the system lightweight

* **Local LLM (Ollama)** was used after OpenAI API access proved unreliable due to:

  * API quota limitations
  * Key management issues
  * Network dependency concerns

This makes the system **fully local and self-contained**.

---

## 📊 Evaluation

The system was evaluated using:

* Multiple academic PDFs
* Conceptual questions (e.g., Transformer attention, model taxonomy)
* Cross-document consistency checks

**Results:**

* Relevant passages were retrieved from multiple documents
* Answers were grounded in uploaded PDFs
* The system successfully supported cross-document understanding

---

## 🔍 Limitations

* TF-IDF embeddings are less expressive than neural embeddings
* Quality depends on PDF text extraction
* No ranking feedback loop yet

These limitations are acceptable given the project scope and constraints.

---

## 🔮 Future Work

* Replace TF-IDF with neural embeddings
* Add citation-level grounding
* Improve chunk filtering and summarization
* Expand demo app with persistent document storage

---

## 👨‍👩‍👧‍👦 Group Information

**Course:** Generative AI
**Group:** Group 10

**Members:**

* Rashid Hamza
* Jaleel Usman
* Raja Wajahat Ali
* Maqsood Asim
* Zai Zohaib Sultan Yousuf

---

## 📄 License

This project is developed for **educational purposes** as part of a university course.


