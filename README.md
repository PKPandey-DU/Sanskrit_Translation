# Sanskrit Translation Project

## Overview
This project explores rule-based and machine-learning-based methods
for translating Sanskrit text to English, and exposes the models
through a Streamlit web application.

## Repository Structure
- `data/` – corpora and intermediate processed files  
- `notebooks/` – Colab-friendly experiment notebooks  
- `src/sanskrit_translation/` – reusable Python package  
- `models/` – saved models and tokenizers  
- `app/` – Streamlit application  

## Setup (Colab)
1. Mount Google Drive.
2. `cd` into the project folder.
3. Install the package:
   ```bash
   !pip install -e .
