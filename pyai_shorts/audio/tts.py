# pyai_shorts/audio/tts.py
from __future__ import annotations
import os
from typing import Dict
import torch
from transformers import AutoProcessor, AutoModelForTextToWaveform
import scipy.io.wavfile as wav

# Cache so models load once per language
_CACHE: Dict[str, tuple] = {}

# Map common language codes -> MMS-TTS model IDs (ISO 639-3)
_LANG_TO_MODEL = {
    "en": "facebook/mms-tts-eng",
    "es": "facebook/mms-tts-spa",
    "fr": "facebook/mms-tts-fra",
    "de": "facebook/mms-tts-deu",
    "it": "facebook/mms-tts-ita",
    "pt": "facebook/mms-tts-por",
    "hi": "facebook/mms-tts-hin",
    "ta": "facebook/mms-tts-tam",
    "te": "facebook/mms-tts-tel",
    "mr": "facebook/mms-tts-mar",
    "bn": "facebook/mms-tts-ben",
    "gu": "facebook/mms-tts-guj",
    "kn": "facebook/mms-tts-kan",
    "ml": "facebook/mms-tts-mal",
    "ur": "facebook/mms-tts-urd",
    # add more as needed
}

def _pick_device() -> str:
    if torch.cuda.is_available():
        return "cuda"
    if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        return "mps"
    return "cpu"

def _load(lang: str):
    lang = lang.lower()
    model_id = _LANG_TO_MODEL.get(lang)
    if not model_id:
        raise ValueError(f"Unsupported lang '{lang}'. Supported: {', '.join(sorted(_LANG_TO_MODEL))}")
    if model_id in _CACHE:
        return _CACHE[model_id]

    processor = AutoProcessor.from_pretrained(model_id)
    model = AutoModelForTextToWaveform.from_pretrained(model_id)
    model.eval().to(_pick_device())
    _CACHE[model_id] = (processor, model)
    return processor, model

@torch.inference_mode()
def text_to_speech(text: str, out_path: str = "speech.wav", lang: str = "en") -> str:
    """
    Convert text -> speech WAV using MMS-TTS.
    Returns the written file path.
    """
    if not text or not text.strip():
        raise ValueError("Empty text provided to TTS.")

    processor, model = _load(lang)
    inputs = processor(text=text, return_tensors="pt")
    # Move tensors if needed
    device = next(model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}

    outputs = model(**inputs)
    waveform = outputs.waveform[0].detach().cpu().numpy()
    sr = getattr(model.config, "sampling_rate", 16000)

    # Ensure dir exists, write WAV (PCM_16)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    wav.write(out_path, sr, waveform)

    return out_path