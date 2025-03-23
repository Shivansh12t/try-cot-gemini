import google.generativeai as genai

def get_gemini_embedding(text):
    try:
        model = genai.embed_content(model="models/embedding-001", content=text)
        return model['embedding']
    except Exception as e:
        print(f"Error during embedding: {e}")
        return None
