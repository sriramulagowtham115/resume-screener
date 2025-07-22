import re

def extract_email(text):
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return email[0] if email else ''

def extract_phone(text):
    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)
    return phone[0] if phone else ''

def extract_skills(text):
    skill_keywords = ['python', 'java', 'sql', 'html', 'css', 'javascript', 'django']
    text_lower = text.lower()
    skills = [skill for skill in skill_keywords if skill in text_lower]
    return skills

def extract_name(text):
    lines = text.strip().split('\n')
    for line in lines:
        line = line.strip()
        if len(line.split()) >= 2 and line[0].isupper():
            return line
    return 'Not found'

def extract_education(text):
    education_keywords = ['b.tech', 'm.tech', 'bachelor', 'master', 'mba', 'bsc', 'msc', 'degree']
    text_lower = text.lower()
    found = [line.strip() for line in text_lower.split('\n') if any(edu in line for edu in education_keywords)]
    return found[0] if found else 'Not found'

def extract_experience(text):
    experience_keywords = ['experience', 'intern', 'internship', 'worked', 'project', 'developed']
    text_lower = text.lower()
    found = [line.strip() for line in text_lower.split('\n') if any(exp in line for exp in experience_keywords)]
    return found[0] if found else 'Not found'

def score_resume(text, required_skills):
    text_lower = text.lower()
    matched_skills = [skill for skill in required_skills if skill in text_lower]
    score = round((len(matched_skills) / len(required_skills)) * 100, 2) if required_skills else 0
    return score, matched_skills
