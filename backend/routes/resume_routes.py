from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil

from services.resume_parser import process_resume
from services.resume_storage import (
    get_all_resumes,
    set_active_resume,
    get_active_resume
)

router = APIRouter()

UPLOAD_FOLDER = "backend/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# 🚀 Upload Resume
@router.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        result = process_resume(file_path)

        return {
            "message": "Resume uploaded and processed successfully!",
            "data": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 📄 Get all resumes
@router.get("/")
def get_resumes():
    resumes = get_all_resumes()
    return {
        "count": len(resumes),
        "resumes": resumes
    }


# ⭐ Set active resume
@router.post("/set_active_resume/{resume_id}")
def activate_resume(resume_id: str):
    success = set_active_resume(resume_id)

    if not success:
        raise HTTPException(status_code=404, detail="Resume not found")

    return {"message": f"Resume with ID {resume_id} is now active."}


# 🔍 Get active resume
@router.get("/active")
def fetch_active_resume():
    active_resume = get_active_resume()

    if not active_resume:
        raise HTTPException(status_code=404, detail="No active resume found")

    return {"active_resume": active_resume}