import faiss
import numpy as np

class SimpleVectorDB:
    def __init__(self):
        self.texts = []
        self.embeddings = []

    def add(self, text, embedding):
        self.texts.append(text)
        self.embeddings.append(np.array(embedding).astype("float32"))

    def build_index(self):
        if not self.embeddings:
            print("⚠️  No embeddings found. Index not built.")
            self.index = None
            return
        self.index = faiss.IndexFlatL2(len(self.embeddings[0]))
        self.index.add(np.array(self.embeddings))

    def search(self, query_embedding, k=1):
        if not self.index:
            print("⚠️  No index found. Returning empty context.")
            return [""]
        D, I = self.index.search(np.array([query_embedding]).reshape(1, -1), k)
        return [self.texts[i] for i in I[0]]
