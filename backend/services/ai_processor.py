import json
import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"


def call_llm(messages, model=os.getenv("OPENROUTER_MODEL")):
    try:
        response = requests.post(
            url=URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": messages
            }
        )

        data = response.json()
        return data["choices"][0]["message"]

    except Exception as e:
        return {"error": str(e)}


# ✅ FIXED
def enhance_resume(resume_text):
    messages = [
        {
            "role": "system",
            "content": "You are an expert resume analyzer. Extract structured data in JSON."
        },
        {
            "role": "user",
            "content": f"""
Extract:
- skills
- experience (role, company, duration)
- projects
- education

Resume:
{resume_text}

Return ONLY valid JSON.
"""
        }
    ]

    response = call_llm(messages)

    try:
        return json.loads(response["content"])
    except:
        return {
            "error": "Invalid JSON",
            "raw_output": response.get("content")
        }


# ✅ FIXED
def generate_insights(resume_text):
    messages = [
        {
            "role": "system",
            "content": "You are a resume coach. Analyze resumes and give insights."
        },
        {
            "role": "user",
            "content": f"""
Analyze this resume and provide:
- strengths
- weaknesses
- suggestions
- overall score (out of 10)

Resume:
{resume_text}

Return ONLY valid JSON.
"""
        }
    ]

    response = call_llm(messages)

    try:
        return json.loads(response["content"])
    except:
        return {
            "error": "Invalid JSON",
            "raw_output": response.get("content")
        }