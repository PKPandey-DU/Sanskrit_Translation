import re
import pandas as pd
from typing import List
from .paths import CORPUS_RAW, CORPUS_CLEANED
from .io_utils import read_csv, write_csv

def basic_clean(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text

def clean_corpus(input_path=CORPUS_RAW, output_path=CORPUS_CLEANED):
    df = read_csv(input_path)
    text_col = "text" if "text" in df.columns else df.columns[0]
    df["cleaned"] = df[text_col].apply(basic_clean)
    write_csv(df, output_path)
    return df

# ---- tokenization / transliteration using indic-nlp ----

from indicnlp.tokenize import indic_tokenize
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

def tokenize_sentence(text: str) -> List[str]:
    return indic_tokenize.trivial_tokenize(text)

def transliterate_to_roman(text: str, lang_code="sa"):
    # many tools use 'hi' for Devanagari; you can adjust
    return UnicodeIndicTransliterator.transliterate(text, lang_code, "en")

def add_tokens_and_roman(df: pd.DataFrame, col="cleaned"):
    df["tokens"] = df[col].apply(tokenize_sentence)
    df["roman"] = df[col].apply(transliterate_to_roman)
    return df
