import streamlit as st

from src.sanskrit_translation.preprocessing import tokenize_sentence, transliterate_to_roman
from src.sanskrit_translation.rule_based import translate_tokens
from src.sanskrit_translation.transformer_model import load_transformer_model, translate_with_transformer

@st.cache_resource
def load_models():
    try:
        tokenizer, transformer = load_transformer_model()
    except Exception as e:
        tokenizer, transformer = None, None
    return tokenizer, transformer

def main():
    st.title("Sanskrit → English Translation Demo")

    st.sidebar.header("Options")
    model_choice = st.sidebar.selectbox(
        "Choose translation model",
        ["Rule-based (simple)", "Transformer (fine-tuned)"],
    )

    text = st.text_area("Enter Sanskrit text (Devanagari):", height=150)

    if st.button("Translate") and text.strip():
        st.subheader("Preprocessing")
        tokens = tokenize_sentence(text)
        st.write("Tokens:", tokens)
        st.write("Roman transliteration:", transliterate_to_roman(text))

        st.subheader("Translation")

        if model_choice == "Rule-based (simple)":
            translation = translate_tokens(tokens)
            st.write("**Rule-based translation:**")
            st.write(translation)

        elif model_choice == "Transformer (fine-tuned)":
            tokenizer, transformer = load_models()
            if tokenizer is None:
                st.error("Transformer model not available. Train and save it first.")
            else:
                translation = translate_with_transformer(text, tokenizer, transformer)
                st.write("**Transformer translation:**")
                st.write(translation)

    st.markdown("---")
    st.markdown("This is a research/teaching demo; translations may be approximate.")

if __name__ == "__main__":
    main()
