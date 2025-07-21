# 📘 MCQ Generator with Gemini AI

**MCQ Generator** is an AI-powered web app that lets users upload educational content (PDF or TXT) and generate structured multiple-choice quizzes using Google’s Gemini API.

Designed for students, educators, and content creators, this tool simplifies the process of quiz creation and helps assess understanding efficiently.

---

## ✨ Features

- Upload .pdf or .txt educational files
- Auto-generate multiple-choice questions with correct answers
- Gemini AI ensures relevant and high-quality questions
- Evaluate quiz complexity and tone with expert-level feedback
- Download the quiz as a .csv file
- Built using Streamlit for a fast and interactive UI
- API key securely handled with .env configuration

---

## 📸 Screenshots

**1. Upload Form:**  The user-friendly interface lets you upload a .pdf or .txt file, choose subject, tone, and number of questions.

<img width="985" height="1039" alt="image" src="https://github.com/user-attachments/assets/9b25e241-8e7b-4b1c-9ddb-df1e629d8865" />


**2. Generated Output:** The app displays multiple-choice questions along with a complexity review powered by Gemini AI.

<img width="985" height="1039" alt="image" src="https://github.com/user-attachments/assets/cea0ac5c-fbb9-475b-baa1-563cfe3947e0" />


**3. Export Feature:** Instantly download the quiz as a .csv file to use in assessments, learning apps, or reports.
   
<img width="1359" height="728" alt="image" src="https://github.com/user-attachments/assets/e68dc92b-df33-4581-a5e6-0c793a50ee17" />

---

## 🗂️ Project Structure

mcq-generator\
- app.py ( Flask app setup and routes )
- mcqgen.py ( Handles text extraction and Gemini summarization )
- .env (API key )
- .gitignore ( Files/folders to ignore in Git )
- requirements.txt 
- README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

- git clone https://github.com/your-username/mcq-generator.git
- cd mcq-generator

### 2. Create Virtual Environment (optional but recommended)

This or use anaconda prompt
- python -m venv venv
- source venv/bin/activate

Or use Anaconda:
- conda create -n mcqgen python=3.10 -y
- conda activate mcqgen

### 3. Install Requirements

pip install -r requirements.txt

### 4. Setup Gemini API Key

Create a .env file in the root directory:
- GEMINI_API_KEY=your_google_gemini_api_key

### 5. Running the App

streamlit run app.py

Then open your browser at:
- http://localhost:8501

---

## 🧠 How to Use

1. Upload a .pdf or .txt file with educational content
2. Select number of questions, subject, and desired tone
3. Click “Generate MCQs”
4. View quiz in a table and download it as CSV
5. Check the expert-written review and complexity feedback

---

**“Create quizzes in seconds — and spend more time learning.”**
🧠💡📘
