# Experiment 6 - Question Answering System

context = """
Artificial Intelligence (AI) is the simulation of human intelligence in machines.
Machine Learning is a branch of AI that enables systems to learn from data.
Deep Learning is a subset of Machine Learning that uses neural networks.
Python is one of the most popular programming languages for AI development.
"""

print("Context:")
print(context)

question = input("\nEnter your question: ")

question = question.lower()

if "artificial intelligence" in question or "ai" in question:
    answer = "Artificial Intelligence (AI) is the simulation of human intelligence in machines."

elif "machine learning" in question:
    answer = "Machine Learning is a branch of AI that enables systems to learn from data."

elif "deep learning" in question:
    answer = "Deep Learning is a subset of Machine Learning that uses neural networks."

elif "python" in question:
    answer = "Python is one of the most popular programming languages for AI development."

else:
    answer = "Sorry! Answer not found in the given context."

print("\nAnswer:")
print(answer)