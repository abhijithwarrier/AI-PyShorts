from .nlp import (
    summarizer, sentiment, translator,
    ner, paraphrase, language_detection,
    keywords, qa
)
from .audio import tts
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

    def ner(self, text, **kwargs):
            """Recognize named entities in input text."""
            return ner.recognize_entity(text, **kwargs)

    def paraphrase(self, text, num=1, **kwargs):
        """Generate paraphrases of input text."""
        return paraphrase.generate_paraphrase(text, num_return_sequences=num, **kwargs)

    def detect_lang(self, text, **kwargs):
        """Generate paraphrases of input text."""
        return language_detection.detect_language(text, **kwargs)

    def keywords(self, text, top_k=10, ngram_min=1, ngram_max=2, method="mmr", diversity=0.5):
        """Extract keywords from input text."""
        return keywords.extract_keywords_table(text, top_k=top_k, ngram_min=ngram_min, ngram_max=ngram_max,
                                         method=method, diversity=diversity)

    def tts(self, text, out_path="speech.wav", lang="en"):
        """Convert text -> speech WAV using MMS-TTS."""
        return tts.text_to_speech(text, out_path=out_path, lang=lang)

    def qa(self, context, question, **kwargs):
        """Ask a question about input text."""
        return qa.answer_question(context, question)

ai = AIShorts()
