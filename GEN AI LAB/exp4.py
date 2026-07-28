from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Sample documents
documents = [
    "Artificial Intelligence is transforming industries.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks.",
    "Python is widely used for AI development.",
    "Natural Language Processing enables computers to understand text."
]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# User query
query = input("Enter your query: ")

# Encode query
query_embedding = model.encode([query])

# Search top 2 similar documents
distances, indices = index.search(np.array(query_embedding), k=2)

print("\nTop Matching Documents:\n")

for i, idx in enumerate(indices[0], 1):
    print(f"{i}. {documents[idx]}")
    print(f"Distance: {distances[0][i-1]:.4f}\n")