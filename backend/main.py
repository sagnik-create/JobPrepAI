from fastapi import FastAPI, UploadFile, File
import os
from services.resume_parser import process_resume
from services.resume_storage import get_all_resumes

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Resume Parser API is running!"}

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    result = process_resume(file_path)
    return {"message": "Resume uploaded and processed successfully!", "parsed_data": result}

@app.get("/resumes/")
def list_resumes():
    resumes = get_all_resumes()
    return {
        "count": len(resumes),
        "resumes": resumes}

