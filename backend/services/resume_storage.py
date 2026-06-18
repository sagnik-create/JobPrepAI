import json
import os
import uuid

RESUME_DB_PATH = "backend/data/resumes.json"


def ensure_db():
    os.makedirs(os.path.dirname(RESUME_DB_PATH), exist_ok=True)

    if not os.path.exists(RESUME_DB_PATH):
        with open(RESUME_DB_PATH, "w") as f:
            json.dump([], f)


def load_resumes():
    ensure_db()
    try:
        with open(RESUME_DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_resumes(resumes):
    ensure_db()
    with open(RESUME_DB_PATH, "w") as f:
        json.dump(resumes, f, indent=4)


def add_resume(resume_dict):
    resumes = load_resumes()

    # ✅ Ensure ID exists
    if "id" not in resume_dict:
        resume_dict["id"] = str(uuid.uuid4())

    resumes.append(resume_dict)
    save_resumes(resumes)


def get_all_resumes():
    return load_resumes()


def set_active_resume(resume_id):
    resumes = load_resumes()
    found = False

    for resume in resumes:
        if resume.get("id") == resume_id:
            resume["is_active"] = True
            found = True
        else:
            resume["is_active"] = False

    if found:
        save_resumes(resumes)

    return found


def get_active_resume():
    resumes = load_resumes()
    for resume in resumes:
        if resume.get("is_active"):
            return resume
    return None