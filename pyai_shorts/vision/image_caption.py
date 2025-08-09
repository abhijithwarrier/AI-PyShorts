from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from pyai_shorts.utils.model_loader import load_custom_model
from PIL import Image

def caption_image(image_path, max_length=16, num_beams=4, **kwargs):
    model, feature_extractor, tokenizer = load_custom_model(
        VisionEncoderDecoderModel,
        ViTImageProcessor,
        AutoTokenizer,
        model_name="nlpconnect/vit-gpt2-image-captioning",
        key="caption_model"
    )
    image = Image.open(image_path).convert("RGB")
    pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values
    output_ids = model.generate(pixel_values, max_length=max_length, num_beams=num_beams)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return caption
