import os
import sys

# --- Make sure Python can see the project root and `src` package ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from src.sanskrit_translation.preprocessing import tokenize_sentence, transliterate_to_roman
from src.sanskrit_translation.rule_based import translate_tokens


def main():
    st.title("Sanskrit → English Translation Demo (Rule-based Prototype)")

    st.sidebar.header("Options")
    st.sidebar.markdown(
        "Currently using **rule-based translation only**.\n\n"
        "Transformer / neural models will be added after PyTorch is configured."
    )

    text = st.text_area("Enter Sanskrit text (Devanagari):", height=150)

    if st.button("Translate") and text.strip():
        st.subheader("Preprocessing")
        tokens = tokenize_sentence(text)
        st.write("**Tokens:**", tokens)
        st.write("**Roman transliteration:**", transliterate_to_roman(text))

        st.subheader("Translation (Rule-based)")
        translation = translate_tokens(tokens)
        st.write(translation)

    st.markdown("---")
    st.markdown(
        "This is a research/teaching demo; translations are approximate and rules are incomplete."
    )


if __name__ == "__main__":
    main()
