def score_resume(text):
    """
    Simple keyword-based AI scoring (replace with ML/NLP model in future)
    """
    score = 0
    text_lower = text.lower()

    if "python" in text_lower:
        score += 20
    if "machine learning" in text_lower or "ml" in text_lower:
        score += 25
    if "bachelor" in text_lower or "b.tech" in text_lower:
        score += 15
    if "experience" in text_lower:
        score += 10
    if "remote" in text_lower or "hybrid" in text_lower:
        score += 5

    return score
