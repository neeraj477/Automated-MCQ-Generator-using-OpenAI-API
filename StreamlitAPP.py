import json
import streamlit as st
import matplotlib.pyplot as plt

from src.mcqgenerator.pdf_generator import create_result_pdf
from src.mcqgenerator.utils import read_file
from src.mcqgenerator.gemini_generator import generate_mcqs

# ---------------------- Session State ----------------------

if "mcqs" not in st.session_state:
    st.session_state.mcqs = None

if "text" not in st.session_state:
    st.session_state.text = None

# ---------------------- Page Config ----------------------

st.set_page_config(
    page_title="AI MCQ Generator",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Automated MCQ Generator")
st.write("Generate Multiple Choice Questions from PDF or Text files using AI.")

# ---------------------- Inputs ----------------------

uploaded_file = st.file_uploader(
    "Upload PDF or TXT",
    type=["pdf", "txt"]
)

col1, col2 = st.columns(2)

with col1:
    number = st.number_input(
        "Number of Questions",
        min_value=1,
        max_value=50,
        value=10
    )

with col2:
    subject = st.text_input(
        "Subject",
        placeholder="Machine Learning"
    )

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

# ---------------------- Generate ----------------------

if st.button("🚀 Generate MCQs"):

    if uploaded_file is None:
        st.error("Please upload a file.")
        st.stop()

    if not subject.strip():
        st.error("Please enter a subject.")
        st.stop()

    try:

        with st.spinner("Reading file..."):
            text = read_file(uploaded_file)

        st.session_state.text = text

        st.success("File uploaded successfully!")

        st.subheader("Extracted Text Preview")

        st.text_area(
            "Content",
            text[:2000],
            height=300
        )

        with st.spinner("Generating MCQs..."):

            response = generate_mcqs(
                text=text,
                subject=subject,
                difficulty=difficulty,
                num_questions=number
            )

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        with st.expander("Raw AI Response"):
            st.code(response, language="json")

        st.session_state.mcqs = json.loads(response)

    except json.JSONDecodeError:
        st.error("Gemini returned invalid JSON.")
        st.code(response)

    except Exception as e:
        st.error(str(e))

# ---------------------- Display Quiz ----------------------

if st.session_state.mcqs:

    st.header("Generated MCQs")

    for idx, mcq in enumerate(st.session_state.mcqs, start=1):

        st.subheader(f"Question {idx}")

        st.write(mcq["question"])

        options = list(mcq["options"].keys())

        st.radio(
            "Choose your answer",
            options,
            format_func=lambda x, m=mcq: f"{x}. {m['options'][x]}",
            key=f"q{idx}"
        )

        st.divider()

    if st.button("✅ Submit Quiz"):

        score = 0

        st.header("📊 Results")

        for idx, mcq in enumerate(st.session_state.mcqs, start=1):

            selected = st.session_state.get(f"q{idx}")

            correct = mcq["correct_answer"]

            if selected == correct:
                score += 1
                st.success(f"✅ Question {idx}: Correct")
            else:
                st.error(f"❌ Question {idx}: Incorrect")

            st.write(f"**Your Answer:** {selected}")
            st.write(f"**Correct Answer:** {correct}")

            if "explanation" in mcq:
                st.info(mcq["explanation"])

            st.divider()

        percentage = (score / len(st.session_state.mcqs)) * 100

        st.success(
            f"🎯 Final Score: {score}/{len(st.session_state.mcqs)} ({percentage:.1f}%)"
        )

        correct = score
        wrong = len(st.session_state.mcqs) - score

        st.subheader("📊 Quiz Performance")

        fig, ax = plt.subplots(figsize=(5, 5))

        ax.pie(
            [correct, wrong],
            labels=["Correct", "Wrong"],
            autopct="%1.1f%%",
            startangle=90
        )

        ax.axis("equal")

        st.pyplot(fig)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("✅ Correct", correct)

        with col2:
            st.metric("❌ Wrong", wrong)

        with col3:
            st.metric("🎯 Accuracy", f"{percentage:.1f}%")

        if percentage >= 80:
            st.balloons()

        # Generate Result PDF
        pdf_path = create_result_pdf(
            mcqs=st.session_state.mcqs,
            user_answers=st.session_state,
            score=score,
            percentage=percentage
        )

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Download Result PDF",
                data=pdf_file,
                file_name="Quiz_Result.pdf",
                mime="application/pdf"
            )