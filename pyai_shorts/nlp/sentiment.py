from pyai_shorts.utils.model_loader import load_pipeline

def analyze_sentiment(text, **kwargs):
    sentiment_analyzer = load_pipeline("sentiment-analysis", "distilbert-base-uncased-finetuned-sst-2-english")
    result = sentiment_analyzer(text)[0]
    return {"label": result["label"], "score": round(result["score"], 4)}
