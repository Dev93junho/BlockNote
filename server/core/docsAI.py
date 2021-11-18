"""
This AI help your for your write
"""
import numpy as np 

# calculate similarity
def cos_sim(v1, v2):
    dot_prod = np.dot(v1, v2)
    norm = (np.sqrt(sum(np.square(v1)))*np.sqrt(sum(np.square(v2))))
    sim = dot_prod / norm
    return sim


# TF-IDF vectorization
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorize = TfidfVectorizer()
tfidf = tfidf_vectorize.fit_transform(corpus).toarray() # corpus is korean dataset. It will be install later