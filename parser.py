import re
import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "c++", "machine learning",
    "deep learning", "html", "css", "javascript",
    "react", "node", "sql", "pandas", "numpy",
    "tensorflow", "powerbi", "excel", "tableau"
]

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Unknown"

def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group(0) if match else "Not Found"

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS_DB:
        if skill in text:
            found.append(skill)

    return list(set(found))

def parse_resume(file_path):
    text = extract_text(file_path)

    name = extract_name(text)
    email = extract_email(text)
    skills = extract_skills(text)

    return {
        "name": name,
        "email": email,
        "skills": skills
    }