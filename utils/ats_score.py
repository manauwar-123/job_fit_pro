from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_skills, job_description):
    documents = [" ".join(resume_skills), job_description]
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(documents)
    return round(cosine_similarity(vectors[0], vectors[1])[0][0] * 100, 2)
