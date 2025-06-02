# grading.py

from sentence_transformers import SentenceTransformer, util

# Load once at the top (shared model instance)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def grade_answer(model_answer: str, student_answer: str):
    """
    Computes the semantic similarity between the model and student answer.
    Returns a similarity score (0 to 1) and a grade (0 to 10).
    """
    if not model_answer.strip() or not student_answer.strip():
        return 0.0, 0.0

    embeddings = model.encode([model_answer, student_answer], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
    grade = round(similarity * 10, 2)
    return similarity, grade