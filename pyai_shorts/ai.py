from .nlp import summarizer, sentiment

class AIShorts:
    def summary(self, text, **kwargs):
        """Summarize input text."""
        return summarizer.summarize(text, **kwargs)

ai = AIShorts()
