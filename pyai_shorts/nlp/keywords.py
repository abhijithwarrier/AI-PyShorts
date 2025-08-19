from typing import List, Tuple
from tabulate import tabulate

# Lazy imports (speedy first import of package)
_KEYBERT = None
_ST_MODEL = None
_CACHE = {}

def _get_keybert():
    global _KEYBERT, _ST_MODEL
    if _KEYBERT is None:
        from keybert import KeyBERT
        from sentence_transformers import SentenceTransformer
        _ST_MODEL = _ST_MODEL or SentenceTransformer("all-MiniLM-L6-v2")
        _KEYBERT = KeyBERT(_ST_MODEL)
    return _KEYBERT

def extract_keywords(
    text: str,
    top_k: int = 10,
    ngram_min: int = 1,
    ngram_max: int = 2,
    method: str = "mmr",   # "mmr" | "maxsum" | "simple"
    diversity: float = 0.5 # only used for mmr
) -> List[Tuple[str, float]]:
    """
    Return a list of (keyword, score), highest score first.
    """
    kw = _get_keybert()
    ngram_range = (ngram_min, ngram_max)

    if method == "maxsum":
        keywords = kw.extract_keywords(
            text, keyphrase_ngram_range=ngram_range, use_mmr=False,
            stop_words="english", top_n=top_k, use_maxsum=True
        )
    elif method == "mmr":
        keywords = kw.extract_keywords(
            text, keyphrase_ngram_range=ngram_range, use_mmr=True,
            diversity=diversity, stop_words="english", top_n=top_k
        )
    else:  # "simple"
        keywords = kw.extract_keywords(
            text, keyphrase_ngram_range=ngram_range, use_mmr=False,
            stop_words="english", top_n=top_k
        )

    # sort high→low
    keywords = sorted(keywords, key=lambda x: x[1], reverse=True)
    return keywords

def extract_keywords_table(*args, **kwargs) -> str:
    pairs = extract_keywords(*args, **kwargs)
    return tabulate([(k, f"{s:.3f}") for k, s in pairs], headers=["Keyword", "Score"], tablefmt="github")
