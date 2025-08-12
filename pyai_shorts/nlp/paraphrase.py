from pyai_shorts.utils.model_loader import load_pipeline

def generate_paraphrase(text, num_return_sequences: int = 1, max_length: int = 60):
    """
    Return 1..N paraphrases of the input text.
    """
    paraphrase_pipeline = load_pipeline("text2text-generation", "tuner007/pegasus_paraphrase")
    results = paraphrase_pipeline(
        text,
        num_return_sequences=num_return_sequences,
        max_length=max_length,
        do_sample=True,
        top_k=60,
        top_p=0.95,
        clean_up_tokenization_spaces=True,
    )
    # returns the list of plain strings
    return [r["generated_text"].strip() for r in results]
