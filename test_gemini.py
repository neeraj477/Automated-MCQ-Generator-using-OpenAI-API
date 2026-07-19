from src.mcqgenerator.gemini_generator import generate_mcqs

text = """
Artificial Intelligence is the simulation of human intelligence in machines.
Machine Learning is a subset of AI.
"""

result = generate_mcqs(
    text=text,
    subject="AI",
    difficulty="Easy",
    num_questions=2
)

print(result)