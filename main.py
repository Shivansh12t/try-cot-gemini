from dotenv import load_dotenv
import os
import google.generativeai as genai
from src import *

# Load .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash-lite")

def run_chain_of_thought_rag(problem, vector_db):
    gemini = model

    steps = break_problem_into_steps(gemini, problem)

    explanations = []
    for step in steps:
        emb = get_gemini_embedding(step)
        context = vector_db.search(emb, k=1)[0]
        explanation = explain_step_with_context(gemini, step, context)
        explanations.append((step, explanation))

    final_answer = synthesize_final_answer(gemini, explanations)
    return final_answer


# small cpu based vector db, can be used to store relevant docs for context
docs = [
    "The moon's phases are caused by its position relative to the Earth and Sun.",
    "As the moon orbits Earth, different parts are illuminated by sunlight.",
    "Half the moon is always lit by the Sun, but we see varying parts from Earth.",
    "The lunar cycle takes about 29.5 days."
]

db = SimpleVectorDB()
for doc in docs:
    emb = get_gemini_embedding(doc)
    db.add(doc, emb)
db.build_index()

problem = input("Ask Anything ?")
answer = run_chain_of_thought_rag(problem, db)
print("🧠 Final Answer:\n", answer)