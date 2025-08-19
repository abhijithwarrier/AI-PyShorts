# AI-PyShorts

⚡ One-liner AI utilities for text, images, and data.

This repository contains short, practical AI scripts built on **Hugging Face Transformers 🤗** and **PyTorch 🔥**.  
The goal is simple: provide **ready-to-use AI commands** that require minimal setup and deliver instant results.

---

## 🧩 Table of Contents

- ✨ [Features](#features)
  - 📝 **[Text Summarization](#-text-summarization)** — Quickly condense long text into concise summaries.
  - 😊 **[Sentiment Analysis](#-sentiment-analysis)** — Detect positive, negative, or neutral sentiment in text.
  - 🖼️ **[Image Captioning](#-image-caption-generator)** — Generate captions for images automatically.
  - 🌐 **[Translator](#-translator)** — Translate text from one language to another.
  - 🔍 **[Named Entity Recognition](#-named-entity-recognition)** — Extracts real-world entities like names, places, and organizations from text.
  - 🔄 **[Paraphraser](#-paraphraser)** — Rewrites text with the same meaning in different words.
  - 🌍 **[Language Detection](#-language-detection)** — Detects the language of the given text instantly.
  - 🔑 **[Keyword Extraction](#-keyword-extraction)** – Find Key Terms in Text
- 🛠 [Requirements](#-requirements)
- 📥 [Installation](#-installation)
- ▶️ [Running the Project](#-running-the-project)

---

## ✨ Features


### 📝 Text Summarization

Condenses long text into a shorter version while preserving the key meaning and context.

Example:

```bash
pyai summary "Artificial Intelligence is transforming industries..."
```

Output:

```bash
Artificial Intelligence is transforming industries. Here are some of the ways it's changing the way we work. Read more at CNN.com/AI.
```

---

### 😊 Sentiment Analysis

Identifies the emotional tone of text, classifying it as POSITIVE, NEGATIVE, or NEUTRAL.

Example:

```bash
pyai sentiment "I like this new AI Tool"
```

Output:

```bash
{'label': 'POSITIVE', 'score': 0.9992}
```

Example:

```bash
pyai sentiment "Oh.. This looks so terrible.."
```

Output:

```bash
{'label': 'NEGATIVE', 'score': 0.9997}
```

---

### 🖼 Image Caption Generator

Generates a concise, descriptive caption for an image — ideal for accessibility, tagging, and creative applications.

Example:

```bash
pyai caption "<path_to_the_image>"
```

Output:

```bash
Automatically generates a relevant caption for the provided image.
```

---

### 🌐 Translator

Effortlessly translates text from a source language to a target language — fast, accurate, and natural-sounding.

Example:

```bash
pyai translate "Hello. This is an example of AI translator command" --src en --tgt sp
```

Output:

```bash
Bonjour. C'est un exemple de commande de traducteur AI
```

---

### 🔍 Named Entity Recognition

Identifies and classifies entities in text such as people, organizations, locations, dates, and more, using a pre-trained Transformer model.

Example:

```bash
pyai ner "Python was created by Guido van Rossum in 1991 and is maintained by the Python Software Foundation in the U
nited States." --aggregation-strategy simple
```

Output:

| Entity | Label | Confidence |
| ------ | ---- | ----- |
| Python | MISC | 0.933 |
| Guido van Rossum | PER | 0.997 |
| Python Software Foundation | ORG | 0.999 |
| United States | LOC | 0.999 |

---

### 🔄 Paraphraser

Generates alternative versions of your text while preserving its original meaning — ideal for improving clarity, variety, or tone.

Example:

```bash
pyai paraphrase "Artificial Intelligence is transforming industries." --num 3
```

Output:

```bash
['Artificial Intelligence is changing industries.', 'Artificial Intelligence is changing the world.', 'Artificial intelligence is helping industries.']
```

---

### 🌍 Language Detection

The Language Detector tool analyzes your input text and identifies its language with high accuracy. 
It’s useful for routing multilingual content, preprocessing text for translation, or simply detecting what language a piece of text is written in.

Example:

```bash
 pyai detectlang "La inteligencia artificial está revolucionando la forma en que trabajamos y vivimos."
```

Output:

```bash
{'language': 'es', 'score': 0.984924852848053}
```

---

### 🔑 Keyword Extraction

Automatically extract the most important words and phrases from any text using transformer-based NLP models.
This helps in summarization, topic discovery, and quick content insights without reading the entire text.

Example:

```bash
pyai keywords "Artificial Intelligence is transforming industries through automation and data-driven decision making." \
  --topk 8 --ngmin 1 --ngmax 2 --method mmr --diversity 0.6
```

Output:

| Keyword | Score |
| ------ |-------|
| industries automation | 0.701 |
| automation data | 0.588 |
| artificial intelligence | 0.548 |
| transforming industries | 0.453 |
| driven decision | 0.438 |
| intelligence transforming | 0.388 |
| data | 0.289 |
| making | 0.128 |

---

## 🛠 Requirements
* Python 3.11 
* See requirements.txt for all dependencies.

---

## 📥 Installation

1. Clone the repository
```bash
git clone <repo-url>

cd AI-PyShorts
```

2. Create & activate a virtual environment
```bash
python3.11 -m venv venv

source venv/bin/activate   # On Windows: venv\Scripts\activate 
```

3. Install dependencies
```bash
pip install -r requirements.txt 
```

4. Install the package in editable mode
```bash
pip install -e . 
```

---

## ▶️ Running the Project

Once installed, you can run the CLI directly:
```bash
pyai summary "Your text here..."
```

Or run through Python:
```bash
python -m pyai_shorts.cli summary "Your text here..."
```

---
