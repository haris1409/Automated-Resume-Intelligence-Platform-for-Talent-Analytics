# 📄 Automated Resume Intelligence Platform for Talent Analytics

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![NLP](https://img.shields.io/badge/NLP-spaCy%20%7C%20NLTK-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🔍 Overview

The **Automated Resume Intelligence Platform** is an NLP-powered system that automates the process of resume screening. It extracts structured information from unstructured resumes and ranks candidates based on job role relevance, making recruitment faster and more efficient.

---

## 🎯 Key Features

* 📄 Automated resume parsing (PDF support)
* 🧠 NLP-based skill and entity extraction
* 📊 Candidate ranking based on job role
* 📁 Batch processing of resumes
* 📈 CSV export for analytics
* ⚙️ Command-line based customization

---

## 🛠️ Tech Stack

* **Programming Language**: Python
* **Libraries**: spaCy, NLTK, pyresparser, pandas
* **Concepts Used**: NLP, Text Processing, Data Analysis

---

## 📂 Project Structure

```bash
resume_intelligence_platform/
│
├── export_to_csv.py
├── rank_candidate.py
├── pre_requisite.py
├── resumes/
└── output/
```

---

## ⚙️ Installation

```bash
pip install pyresparser spacy nltk pandas
python -m spacy download en_core_web_sm
```

---

## ▶️ Usage

```bash
python export_to_csv.py <folder_path> "<job_role>"
```

### Example:

```bash
python export_to_csv.py . "data scientist"
```

---

## 📊 Output

✔ Generates CSV file:

```bash
Extracted-Resumes-DD-MM-YY.csv
```

✔ Contains:

* Candidate details
* Skills
* Experience
* Ranking score

---

## 🧠 How It Works

1. Reads resumes from a folder
2. Extracts data using NLP (pyresparser)
3. Converts data into structured format
4. Ranks candidates based on job role
5. Exports results into CSV

---

## 🎯 Use Cases

* Resume screening automation
* HR analytics
* Candidate shortlisting
* Talent acquisition systems

---

## ⚠️ Requirements

* Python 3.10 / 3.11 recommended
* Works best with PDF resumes

---

## 🚀 Future Enhancements

* Web-based dashboard
* AI-based ranking model
* Support for DOCX resumes
* Integration with job portals

---

## 👨‍💻 Author

Developed as part of an academic project on
**Automated Resume Intelligence & Talent Analytics**

---

⭐ If you found this useful, give it a star!
