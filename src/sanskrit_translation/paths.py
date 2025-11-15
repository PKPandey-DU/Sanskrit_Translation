from .config import DATA_DIR, MODELS_DIR, RESULTS_DIR

CORPUS_RAW = DATA_DIR / "corpus_sample.csv"
EXAMPLE_INPUT = DATA_DIR / "example_input.txt"
EXAMPLE_OUTPUT = DATA_DIR / "example_output.txt"

CORPUS_CLEANED = DATA_DIR / "corpus_cleaned.csv"
CORPUS_PREPROCESSED = DATA_DIR / "corpus_preprocessed.csv"
CORPUS_FEATURES = DATA_DIR / "corpus_features.csv"

TFIDF_VECTORIZER = MODELS_DIR / "tfidf_vectorizer.pkl"
ML_BASELINE_MODEL = MODELS_DIR / "ml_baseline.pkl"
SEQ2SEQ_MODEL = MODELS_DIR / "seq2seq_model.h5"
TOKENIZER = MODELS_DIR / "tokenizer.pkl"
TRANSFORMER_DIR = MODELS_DIR / "transformer_model"
