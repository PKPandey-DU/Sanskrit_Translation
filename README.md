\## Stack

\- \*\*Colab + Google Drive\*\* (model/data cache)

\- \*\*GitHub\*\* (source of truth)

\- Transformers, PyTorch, IndicNLP, SacreBLEU

\- (Optional) Gradio UI in Colab; Streamlit app for deployment



\## Project Layout

\- `src/` core Python code

\- `notebooks/` experiments \& evaluation

\- `app/` optional Streamlit UI

\- `data/` small samples (large corpora kept in Drive)



\## Quick Start (Colab)

1\. Open this repo in Colab: \*Colab → File → Open notebook → GitHub\*.

2\. Run setup cell:

&nbsp;  ```python

&nbsp;  !pip -q install "transformers>=4.39,<5" "torch>=2.3,<2.6" indic-nlp-library sacrebleu pandas numpy gradio

&nbsp;  from google.colab import drive; drive.mount

