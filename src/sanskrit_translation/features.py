import pandas as pd
from .paths import CORPUS_PREPROCESSED, CORPUS_FEATURES
from .io_utils import read_csv, write_csv

def dummy_morph_analysis(token: str) -> dict:
    # Placeholder for real morphological analysis
    return {"lemma": token, "pos": "UNK", "case": "NA"}

def add_morph_features(df: pd.DataFrame):
    features = df["tokens"].apply(
        lambda tokens: [dummy_morph_analysis(t) for t in tokens]
    )
    df["morph_features"] = features
    return df

def build_feature_corpus(
    input_path=CORPUS_PREPROCESSED, output_path=CORPUS_FEATURES
):
    df = read_csv(input_path)
    df = add_morph_features(df)
    write_csv(df, output_path)
    return df
