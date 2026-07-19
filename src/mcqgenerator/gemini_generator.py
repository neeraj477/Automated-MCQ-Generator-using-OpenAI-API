import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_mcqs(text, subject, difficulty, num_questions):
    prompt = f"""
You are an expert teacher.

Generate exactly {num_questions} multiple-choice questions from the following study material.

Subject: {subject}
Difficulty: {difficulty}

Rules:
- Use only information present in the study material.
- Exactly 4 options: A, B, C, D.
- Exactly one correct answer.
- Include a short explanation.
- Return ONLY valid JSON.
- Do NOT wrap the response in ```json.

Return this format:

[
  {{
    "question": "...",
    "options": {{
      "A": "...",
      "B": "...",
      "C": "...",
      "D": "..."
    }},
    "correct_answer": "A",
    "explanation": "..."
  }}
]

Study Material:

{text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text