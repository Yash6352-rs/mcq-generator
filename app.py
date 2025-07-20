import streamlit as st
import pandas as pd
import json
import re
import PyPDF2
from mcqgen import generate_evaluate_chain, RESPONSE_JSON

# Function to read file (PDF or TXT)
def read_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        try:
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception:
            st.error("Failed to read PDF file.")
            return None
    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    else:
        st.error("Unsupported file format. Only PDF and TXT allowed.")
        return None

# Streamlit UI

st.title("MCQ Generator")
st.write("Upload some educational content and generate multiple choice quizzes.")

uploaded_file = st.file_uploader("Upload a `.pdf` or `.txt` file", type=["pdf", "txt"])
number = st.number_input("Number of Questions", min_value=1, max_value=20, value=5)
subject = st.text_input("Subject", value="GenAI")
tone = st.selectbox("Tone", ["simple", "moderate", "formal", "engaging"], index=0)

if st.button("Generate MCQs") and uploaded_file:
    text = read_file(uploaded_file)
    
    if not text:
        st.stop()

    with st.spinner("Generating quiz..."):
        try:
            result = generate_evaluate_chain({
                "text": text,
                "number": number,
                "subject": subject,
                "tone": tone,
                "response_json": json.dumps(RESPONSE_JSON),
            })

            # Raw output
            quiz_raw = result["quiz"]
            review = result["review"]

            # Clean any formatting like markdown
            cleaned_quiz = re.sub(r"```json|```", "", quiz_raw).strip()

            # Parse JSON
            quiz_dict = json.loads(cleaned_quiz)

            quiz_table_data = []
            for key, value in quiz_dict.items():
                mcq = value["mcq"]
                options = " | ".join(
                    [f"{opt}: {val}" for opt, val in value["options"].items()]
                )
                correct = value["correct"]
                quiz_table_data.append({
                    "MCQ": mcq,
                    "Choices": options,
                    "Correct": correct
                })

            quiz_df = pd.DataFrame(quiz_table_data)

            st.subheader("Generated Quiz")
            st.dataframe(quiz_df)

            st.download_button(
                "Download as CSV", 
                data=quiz_df.to_csv(index=False).encode("utf-8"),
                file_name="quiz.csv",
                mime="text/csv"
            )

            st.subheader("Complexity Review")
            st.write(review)

        except Exception as e:
            st.error("Failed to parse quiz output. Please check the format or try again.")
            st.exception(e)
