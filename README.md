# Chain-of-Thought + RAG with Gemini API

This project is a simple implementation of a **Chain-of-Thought (CoT) reasoning system** with optional **Retrieval-Augmented Generation (RAG)** using **Google's Gemini API** and **FAISS** for in-memory vector search.

---

## 🚀 How It Works

1. **User inputs a complex question**
2. **Gemini breaks it into logical steps** (Chain of Thought)
3. For each step:
   - Optionally retrieves relevant context from a **vector store (RAG)**
   - Explains each step using the context
4. **Gemini synthesizes a final answer** from all the step-wise explanations

You can toggle between:
- ✅ **CoT + RAG**: with document-based context
- 🧠 **Pure CoT**: no documents, no distractions

---

## 🧱 Tech Stack

| Component              | Description |
|------------------------|-------------|
| 🧠 Gemini API           | Google's GenAI model (via `google-generativeai`) for reasoning and explanation |
| 📦 FAISS               | In-memory vector search for document retrieval |
| 🔐 python-dotenv       | Load Gemini API key from `.env` |
| 🐍 Python              | Core programming language |
| 📂 SimpleVectorDB      | Minimal vector database for storing and retrieving documents |

---

## 📂 Project Structure

```
📦 try-cot-gemini/
├── main.py                # Main script (runs the pipeline)
├── modules/
│   ├── embeddings.py      # Get Gemini Embeddings
│   ├── vectordb.py        # SimpleVectorDB class (FAISS + context handling)
│   ├── pipeline.py        # CoT + RAG logic (break, explain, synthesize)
├── .env                   # API key file
├── requirements.txt
└── README.md
```

---

## 🛠 Setup Instructions

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Set your Gemini API key**
Create a `.env` file as per `template.env`:
```
GOOGLE_API_KEY=your-api-key-here
```

3. **Run the app**
```bash
python main.py
```

4. **Ask anything!**
```
Ask Anything? Why does the moon appear to change shape?
```

---

## 🧪 Example Run

```
Ask Anything? Why does the moon appear to change shape?

🧠 Final Answer:
The moon appears to change shape because different portions of it are illuminated by the Sun as it orbits Earth...
```

---

## 📌 Notes

- If no documents are added to the vector store, it will run in **CoT-only mode**
- You can add relevant knowledge/documents to `SimpleVectorDB` for RAG-style context enrichment

---

## 📧 Contact

Feel free to reach out or fork for improvements!

---

## To-Do
* [ ] Saving Responses in Markdown format
* [ ] Some way to Benchmark the Generations
* [ ] UI/UX for general use
* [ ] Document Splitter and Other Document Handling functions
