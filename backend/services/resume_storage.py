import json
import os

RESUME_DB_PATH = "backend/data/resumes.json"

def load_resumes():
    if not os.path.exists(RESUME_DB_PATH):
        return []
    with open(RESUME_DB_PATH, "r") as f:
        return json.load(f)

def save_resumes(resumes):
    with open(RESUME_DB_PATH, "w") as f:
        json.dump(resumes,f, indent=4)

def add_resume(resume_dict):
    resumes = load_resumes()
    resumes.append(resume_dict)
    save_resumes(resumes)

def get_all_resumes():
    return load_resumes()