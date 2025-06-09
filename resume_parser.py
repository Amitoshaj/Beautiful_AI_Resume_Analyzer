import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_resume_text(file):
    text = ""
    if file.filename.endswith(".pdf"):
        import PyPDF2
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    elif file.filename.endswith(".docx"):
        import docx
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
    return text

def extract_skills(text):
    skills = []
    skill_keywords = ["python", "java", "sql", "machine learning", "flask", "html", "css", "nlp", "data analysis"]
    text = text.lower()
    for skill in skill_keywords:
        if skill in text:
            skills.append(skill)
    return list(set(skills))

def match_resume_with_job(resume_text, job_desc):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)
    matched = set(resume_skills).intersection(set(job_skills))
    total_required = len(set(job_skills))
    score = int((len(matched) / total_required) * 100) if total_required > 0 else 0
    missing = list(set(job_skills) - matched)
    return score, missing
