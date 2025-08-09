from .nlp import summarizer, sentiment, translator
from .vision import image_caption

class AIShorts:
    def summary(self, text, **kwargs):
        """Summarize input text."""
        return summarizer.summarize(text, **kwargs)

    def sentiment(self, text, **kwargs):
        """Analyze sentiment of input text."""
        return sentiment.analyze_sentiment(text, **kwargs)

    def caption(self, image_path, **kwargs):
        """Generate caption for an image."""
        return image_caption.caption_image(image_path, **kwargs)

    def translate(self, text, src_lang: str = "en", tgt_lang = "fr", **kwargs):
        """Translate text from one language to another."""
        return translator.translate(text, src_lang, tgt_lang, **kwargs)

ai = AIShorts()
