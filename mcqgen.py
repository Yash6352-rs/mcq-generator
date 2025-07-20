import os
import json
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.5
)

# JSON structure example
RESPONSE_JSON = {
    "1": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    }
}

# Quiz generation prompt
template1 = """
Text: {text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in a {tone} tone. 
Ensure questions are not repeated and are aligned with the text.
Only return valid JSON with no markdown or extra text.

### RESPONSE_JSON
{response_json}
"""

# Quiz evaluation prompt
template2 = """
You are an expert English grammarian and writer. Given the following quiz for {subject} students, \
evaluate its complexity in under 50 words. If necessary, adjust questions and tone to better suit the students' level.

Quiz:
{quiz}
"""

# Prompt chains
quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=template1,
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=template2,
)

review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

# Sequential chain
generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=["text", "number", "subject", "tone", "response_json"],
    output_variables=["quiz", "review"],
    verbose=True,
)

# Export chain and response format
__all__ = ["generate_evaluate_chain", "RESPONSE_JSON"]
