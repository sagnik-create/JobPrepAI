import pdfplumber
from models.resume_model import Resume
from services.resume_storage import add_resume
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def simple_parse(text):
    lines = text.splitlines()
    name = lines[0] if lines else ""
    email = ""
    phone = ""
    skills = []
    experience = []
    education = []
    
    for line in lines:
        if "@" in line:
            email = line.strip()
        elif any(char.isdigit() for char in line):
            phone = line.strip()
        elif "skill" in line.lower():
            skills.append(line.strip())
        elif "experience" in line.lower():
            experience.append(line.strip())
        elif "education" in line.lower():
            education.append(line.strip())
    
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": ", ".join(skills),
        "experience": "\n".join(experience),
        "education": "\n".join(education)
    }

def parse_resume(file_path):
    parsed_data = simple_parse(file_path)
    resume = Resume(file_name=file_path.split("/")[-1],parsed_data=parsed_data)
    add_resume(resume.to_dict())
    return resume.to_dict()