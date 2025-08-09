from pyai_shorts.utils.model_loader import load_pipeline

def summarize(text, max_length=130, min_length=30, **kwargs):
    summarizer = load_pipeline("summarization", "facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
