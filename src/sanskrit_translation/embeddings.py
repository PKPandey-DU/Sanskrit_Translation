from typing import Tuple
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from .paths import CORPUS_CLEANED, TFIDF_VECTORIZER
from .io_utils import read_csv

def build_tfidf_model(input_path=CORPUS_CLEANED, max_features=5000) -> Tuple[TfidfVectorizer, any]:
    df = read_csv(input_path)
    text_col = "cleaned"
    vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=(1, 2))
    X = vectorizer.fit_transform(df[text_col])
    TFIDF_VECTORIZER.parent.mkdir(parents=True, exist_ok=True)
    with open(TFIDF_VECTORIZER, "wb") as f:
        pickle.dump(vectorizer, f)
    return vectorizer, X

def load_tfidf_vectorizer(path=TFIDF_VECTORIZER) -> TfidfVectorizer:
    with open(path, "rb") as f:
        return pickle.load(f)

# Sentence-transformer embeddings will be done in notebooks using transformers.
