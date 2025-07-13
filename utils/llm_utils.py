import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")






genai.configure(api_key=api_key, transport="rest")




model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def generate_summary(text):
    prompt = f"Summarize the following document in under 150 words:\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def answer_question(text, question):
    prompt = (
        "Based only on the document below, answer the question. Include paragraph/page justification.\n\n"
        f"Document:\n{text}\n\nQuestion:\n{question}"
    )
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating answer: {str(e)}"

def generate_logic_questions(text):
    prompt = (
        "Generate 3 logical reasoning or comprehension questions from the following document:\n\n"
        f"{text}"
    )
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating logic questions: {str(e)}"




