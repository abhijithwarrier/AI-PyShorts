from .nlp import summarizer, sentiment

class AIShorts:
    def summary(self, text, **kwargs):
        """Summarize input text."""
        return summarizer.summarize(text, **kwargs)

    def sentiment(self, text, **kwargs):
        """Analyze sentiment of input text."""
        return sentiment.analyze_sentiment(text, **kwargs)

ai = AIShorts()
