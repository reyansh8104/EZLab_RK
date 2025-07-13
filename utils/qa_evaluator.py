import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-pro")


def evaluate_answer(text, question, user_answer):
    prompt = (
        "Evaluate the user's answer based only on the document provided. "
        "Explain whether the answer is correct, partially correct, or incorrect, and give justification.\n\n"
        f"Document:\n{text}\n\n"
        f"Question:\n{question}\n\n"
        f"User's Answer:\n{user_answer}"
    )

    response = model.generate_content(prompt)
    return response.text.strip()
