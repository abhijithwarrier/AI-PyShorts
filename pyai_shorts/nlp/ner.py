from pyai_shorts.utils.model_loader import load_pipeline
from tabulate import tabulate

def recognize_entity(text, **kwargs):
    ner_pipeline = load_pipeline("ner", "dslim/bert-base-NER")
    results = ner_pipeline(text, aggregation_strategy=kwargs.get("aggregation_strategy", "simple"))

    # Formatting result into a table
    table_data = [
        [ent["word"], ent["entity_group"], f"{ent['score']:.3f}"]
        for ent in results
    ]
    return tabulate(table_data, headers=["Entity", "Label", "Confidence"])