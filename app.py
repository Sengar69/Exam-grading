import streamlit as st
from text_grading import grade_answer

# Page config
st.set_page_config(page_title="Automated Exam Grading", layout="centered")
st.title("📝 Automated Exam Grading System")
st.markdown("Grade student answers using semantic similarity (NLP-powered).")

# Input form
with st.form("grading_form"):
    question = st.text_input("📘 Question")
    model_answer = st.text_area("✅ Model Answer", height=150)
    student_answer = st.text_area("🧑‍🎓 Student's Answer", height=150)
    submitted = st.form_submit_button("Grade Answer")

if submitted:
    if not model_answer.strip() or not student_answer.strip():
        st.warning("Please fill in both the model and student answers.")
    else:
        with st.spinner("Grading in progress..."):
            similarity, grade = grade_answer(model_answer, student_answer)

        st.success(f"Semantic Similarity Score: *{similarity:.2f}*")
        st.info(f"Predicted Grade: *{grade}/10*")

        # Optional color indicator
        if grade >= 8:
            st.markdown("🟢 *Excellent*")
        elif grade >= 5:
            st.markdown("🟡 *Average*")
        else:
            st.markdown("🔴 *Needs Improvement*")