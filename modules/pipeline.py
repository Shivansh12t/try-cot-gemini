def break_problem_into_steps(model, problem):
    """
    Uses the Gemini model to break a complex problem into logical, ordered reasoning steps.
    """
    prompt = f"Break this problem into logical reasoning steps ( at most do 5 reasoning steps ):\n\nProblem: {problem}"
    print("\n🧩 [Step 1] Asking Gemini to break down the problem...")
    print(f"📤 Prompt:\n{prompt}\n")

    response = model.generate_content(prompt)

    print("📥 Gemini's Response:\n", response.text)

    # Extract and clean steps (split by newlines)
    steps = [line.strip() for line in response.text.strip().split("\n") if line.strip()]
    print(f"✅ Extracted {len(steps)} steps.")
    return steps

def explain_step_with_context(model, step, context):
    """
    For a single reasoning step, enrich it with retrieved knowledge/context and ask Gemini to explain it.
    """
    prompt = f"""Explain this step using the given context:
Step: {step}
Context: {context}
"""
    print(f"\n🔍 [Step Explanation] Explaining: \"{step}\"")
    print(f"📤 Prompt to Gemini:\n{prompt}")

    response = model.generate_content(prompt)

    print("📥 Explanation:\n", response.text.strip())
    return response.text.strip()

def synthesize_final_answer(model, explanations):
    """
    Combines all enriched explanations into one coherent final answer.
    """
    print("\n🧠 [Final Synthesis] Combining explanations into a final answer...")

    # Create the final prompt by feeding all steps and their explanations
    prompt = "Based on the following step-by-step explanations, summarize the complete answer:\n"
    for i, (step, explanation) in enumerate(explanations):
        prompt += f"\nStep {i+1}: {step}\nExplanation: {explanation}"

    print("📤 Prompt to Gemini:\n", prompt[:1000], "\n...truncated if too long")

    response = model.generate_content(prompt)

    print("\n📥 Final Answer:\n", response.text.strip())
    return response.text.strip()

