import PyPDF2
import re
from utils.skills_list import skills_list

def extract_skills_from_resume(filepath):
    text = ""
    with open(filepath, "rb") as file:
        pdf = PyPDF2.PdfReader(file)
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    text = text.lower()
    found_skills = [skill for skill in skills_list if skill.lower() in text]
    print("Extracted Text:\n", text)       # Optional for debugging
    print("Found Skills:", found_skills)   # Optional for debugging
    return found_skills
