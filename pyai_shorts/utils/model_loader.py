
import torch

_loaded_models = {}

def load_pipeline(task, model_name, key=None):
    from transformers import pipeline
    key = key or model_name
    if key in _loaded_models:
        return _loaded_models[key]

    device = 0 if torch.cuda.is_available() else -1
    if device == -1:
        print(f"[INFO] No GPU found, using CPU for {task}. This may be slower.")

    model = pipeline(task, model=model_name, device=device)
    _loaded_models[key] = model
    return model


def load_custom_model(model_class, feature_extractor_class=None, tokenizer_class=None, model_name=None, key=None):
    if key and key in _loaded_models:
        return _loaded_models[key]

    device = 0 if torch.cuda.is_available() else -1
    if device == -1:
        print(f"[INFO] No GPU found, using CPU for {model_name}. This may be slower.")

    model = model_class.from_pretrained(model_name)
    feature_extractor = feature_extractor_class.from_pretrained(model_name) if feature_extractor_class else None
    tokenizer = tokenizer_class.from_pretrained(model_name) if tokenizer_class else None

    if key:
        _loaded_models[key] = (model, feature_extractor, tokenizer)
    return model, feature_extractor, tokenizer
