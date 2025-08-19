from pyai_shorts.utils.model_loader import load_pipeline

def answer_question(context: str, question:str):
    """
    Extractive Question Answering.
    Provide a context paragraph and a question, get the best possible answer.

    Args:
        context (str): The reference text (paragraph/document).
        question (str): The question to answer.

    Returns:
        str: The extracted answer from the context.
    """
    qa_pipeline = load_pipeline("question-answering", "deepset/roberta-base-squad2")
    result = qa_pipeline(
        question=question,
        context=context
    )
    return result["answer"]
