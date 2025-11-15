from typing import List

# toy dictionary; extend later
DICTIONARY = {
    "धर्मक्षेत्रे": "in the field of dharma",
    "कुरुक्षेत्रे": "in Kurukshetra",
    "समवेता": "assembled",
    "युयुत्सवः": "desiring to fight",
}

def translate_tokens(tokens: List[str]) -> str:
    eng_tokens = []
    for token in tokens:
        eng_tokens.append(DICTIONARY.get(token, token))
    return " ".join(eng_tokens)

def translate_sentence(text: str, tokenizer):
    tokens = tokenizer(text)
    return translate_tokens(tokens)
