
import streamlit as st
from utils.doc_parser import extract_text_from_pdf, extract_text_from_txt
from utils.llm_utils import generate_summary, answer_question, generate_logic_questions
from utils.qa_evaluator import evaluate_answer
import tempfile
st.set_page_config(page_title="Smart AI Assistant", page_icon="", layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #6C63FF;'>Smart AI Assistant by Reyansh Kaushik</h1>
    <p style='text-align: center; color: #555;'>Your personal assistant for summarization and interaction. </p>
    <hr>
""", unsafe_allow_html=True)



uploaded_file = st.file_uploader("Upload a PDF or TXT Document:", type=["pdf", "txt"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    if uploaded_file.type == 'application/pdf':
        doc_text = extract_text_from_pdf(tmp_path)
    else:
        doc_text = extract_text_from_txt(tmp_path)

    st.success("Document uploaded successfully!")

    st.markdown("""
        <div style='background-color: #F0F2F6; padding: 15px; border-radius: 10px; border-left: 5px solid #6C63FF;'>
            <h3>Auto Summary</h3>
        </div>
    """, unsafe_allow_html=True)

    with st.spinner("Generating summary..."):
        summary = generate_summary(doc_text)
    st.info(summary)

    st.subheader("Select Interaction Mode:")
    mode = st.radio("Choose Mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        question = st.text_input("Ask your question about the document:")
        if question:
            with st.spinner("Fetching answer..."):
                answer = answer_question(doc_text, question)
            st.markdown(f"<div style='background-color:#FFF3E0;padding:15px;border-radius:10px;border-left:5px solid #FF9800;'>"
                        f"<strong>Answer:</strong><br>{answer}</div>", unsafe_allow_html=True)

    elif mode == "Challenge Me":
        with st.spinner("Creating challenge questions..."):
            questions = generate_logic_questions(doc_text).split('\n')

        st.markdown("### Check your brain:")
        user_answers = []
        for idx, q in enumerate(questions, start=1):
            st.markdown(f"**Q{idx}:** {q}")
            ans = st.text_area(f"Your Answer to Q{idx}", height=80)
            user_answers.append(ans)

        if st.button("Check my brain"):
            for idx, (q, ans) in enumerate(zip(questions, user_answers), start=1):
                with st.spinner(f"Evaluating Ques{idx}..."):
                    feedback = evaluate_answer(doc_text, q, ans)
                st.markdown(f"#### Feedback{idx}:")
                st.markdown(f"<div style='background-color:#E8F5E9;padding:15px;border-radius:10px;border-left:5px solid #4CAF50;'>"
                            f"{feedback}</div>", unsafe_allow_html=True)
