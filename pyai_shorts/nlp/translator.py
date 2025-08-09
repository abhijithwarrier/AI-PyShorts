from pyai_shorts.utils.model_loader import load_pipeline

def translate(text, src_lang: str = "en", tgt_lang = "fr", **kwargs):
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    translator = load_pipeline("translation", model_name=model_name)
    result = translator(text, max_length=512)
    return result[0]["translation_text"]
