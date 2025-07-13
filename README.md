# Developed by REYANSH KAUSHIK


# Smart AI Assistant for Summarization and Interaction

An AI-powered assistant that can:

- Summarize uploaded PDF or TXT research documents.
- Answer comprehension and logic-based questions.
- Generate reasoning-based quiz questions.
- Evaluate user answers with document-based justification.

## Features
- Streamlit Web App
- Gemini Powered LLM Reasoning
- Auto Summary 
- Ask Anything Mode (Based on Documents)
- Challenge Me Mode (Quiz + Evaluation)
- :Sleek Modern UI

## Setup Instructions
```bash
git clone <repo-url>
cd genai-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Add your Gemini API Key in `.env`:
```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the app:
```bash
streamlit run app.py
```

## Architecture
- Streamlit for UI
- Gemini for Summarization, Q&A, Reasoning
- PyMuPDF for Document Parsing
- Dotenv for Secure Keys

