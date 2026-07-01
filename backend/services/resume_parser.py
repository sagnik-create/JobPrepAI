import pdfplumber
import os
from models.resume_model import Resume
from services.resume_storage import add_resume
from services.ai_processor import enhance_resume, generate_insights


def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
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
        elif any(char.isdigit() for char in line) and len(line) < 20:
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
        "skills": skills,
        "experience": experience,
        "education": education
    }


# ✅ This should ONLY parse text
def parse_resume(text):
    return simple_parse(text)


# ✅ This is your MAIN pipeline (VERY IMPORTANT)
def process_resume(file_path):
    # Step 1: Extract text
    text = extract_text_from_pdf(file_path)

    # Step 2: Parse
    parsed_data = parse_resume(text)

    # Step 3: AI Enhancement
    ai_data = enhance_resume(parsed_data)

    # Step 4: Generate insights
    insights = generate_insights(ai_data)

    # Step 5: Create Resume Object
    file_name = os.path.basename(file_path)
    resume = Resume(
        file_name=file_name,
        file_path=file_path,
        parsed_data=parsed_data,
        ai_data=ai_data,
        insights=insights,
        is_active=True

    )

    # Step 6: Store in JSON
    add_resume(resume.to_dict())

    return resume.to_dict()
