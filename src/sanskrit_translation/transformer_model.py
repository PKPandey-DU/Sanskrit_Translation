from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from .paths import TRANSFORMER_DIR

MODEL_NAME = "Helsinki-NLP/opus-mt-mul-en"  # example; adjust to Sanskrit-friendly

def load_transformer_model(model_dir=TRANSFORMER_DIR):
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    return tokenizer, model

def translate_with_transformer(text: str, tokenizer, model, max_length=64):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs, max_length=max_length)
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
