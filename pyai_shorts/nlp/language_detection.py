from pyai_shorts.utils.model_loader import load_pipeline

def detect_language(text, src_lang: str = "en", tgt_lang = "fr", **kwargs):
    model_name = f"papluca/xlm-roberta-base-language-detection"
    detector = load_pipeline("text-classification", model_name=model_name)
    result = detector(text, top_k=None)[0]
    return {
        "language": result["label"],
        "score": float(result["score"])
    }
