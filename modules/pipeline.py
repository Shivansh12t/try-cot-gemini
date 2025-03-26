from modules.utils import log_to_markdown

def break_problem_into_steps(model, problem):
    prompt = f'''You are a step-by-step reasoning assistant.
Break down the following problem into exactly 5 logical reasoning steps for a undergraduate level student.  
- Return the output **only** in Markdown format using `1.` to `5.`  
- Do not include subpoints, introductions, explanations, or conclusions.  
- Do not add anything outside the 5 main steps.
Problem: {problem}
'''
    print("\n🧩 [Step 1] Asking Gemini to break down the problem...")
    print(f"📤 Prompt:\n{prompt}\n")
    
    log_to_markdown(f"## 🔍 Problem:\n{problem}")
    # log_to_markdown(f"### 🔧 Prompt to Gemini:\n```\n{prompt}\n```")

    response = model.generate_content(prompt)

    print("📥 Gemini's Response:\n", response.text)
    log_to_markdown(f"### 🧠 Initial Response:\n\n{response.text.strip()}\n")

    steps = [line.strip() for line in response.text.strip().split("\n") if line.strip()]
    log_to_markdown(f"### ✅ Research Plan {len(steps)} Steps:\n" + "\n".join([f"- {step}" for step in steps]))

    return steps

def explain_step_with_context(model, step, context):
    prompt = f"""You are a helpful reasoning assistant.

Explain the following reasoning step using the provided context.  
- Return the answer **only** in valid Markdown format (use simple paragraphs or bullet points if needed).  
- Include Latex or Code if required in Proper Markdown Format
- Answer the question in Detail.
- Don't Answer things outside the context or the question

Step: {step}  
Context: {context}
    """
    print(f"\n🔍 [Step Explanation] Explaining: \"{step}\"")
    print(f"📤 Prompt to Gemini:\n{prompt}")
    # log_to_markdown(f"## 🔄 Step: {step}\n### 📄 Context:\n> {context}")
    log_to_markdown(f"### 🔄 Step: {step}\n📄 Context:\n> {context}")
    # log_to_markdown(f"### 📤 Prompt:\n```\n{prompt}\n```")

    response = model.generate_content(prompt)

    explanation = response.text.strip()
    print("📥 Explanation:\n", explanation)
    log_to_markdown(f"### 📥 Explanation:\n\n{explanation}\n\n")

    return explanation

def synthesize_final_answer(model, explanations):
    print("\n🧠 [Final Synthesis] Combining explanations into a final answer...")

    prompt = "Based on the following step-by-step explanations, summarize the complete answer return the answer in markdown without fail, the answer must be elaborate and answer all the questions, you can use pointers to curate the answer:\n"
    for i, (step, explanation) in enumerate(explanations):
        prompt += f"\nStep {i+1}: {step}\nExplanation: {explanation}"

    # log_to_markdown("## 🧩 Final Synthesis Prompt\n```" + prompt[:1000] + "\n...```")

    response = model.generate_content(prompt)
    final = response.text.strip()

    print("\n📥 Final Answer:\n", final)
    log_to_markdown("## ✅ Final Answer\n" + final)

    return final

