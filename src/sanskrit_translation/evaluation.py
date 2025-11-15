from typing import List
from sacrebleu import corpus_bleu

def bleu_score(references: List[str], hypotheses: List[str]) -> float:
    refs = [references]  # sacrebleu expects list of ref lists
    bleu = corpus_bleu(hypotheses, refs)
    return bleu.score
