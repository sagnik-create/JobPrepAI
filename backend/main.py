from fastapi import FastAPI
from routes.resume_routes import router as resume_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Resume Parser API is running!"}


# ✅ Plug in your routes here
app.include_router(resume_router, prefix="/resume", tags=["Resume"])