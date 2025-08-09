# AI-PyShorts

⚡ One-liner AI utilities for text, images, and data.

This repository contains short, practical AI scripts built on **Hugging Face Transformers 🤗** and **PyTorch 🔥**.  
The goal is simple: provide **ready-to-use AI commands** that require minimal setup and deliver instant results.

---

## ✨ Features

- 📝 **Text Summarization** — Quickly condense long text into concise summaries.
- 😊 **Sentiment Analysis** — Detect positive, negative, or neutral sentiment in text.
- 🖼️ **Image Captioning** — Generate captions for images automatically.

---

## 📌 Text Summarization

Our summarizer uses a pre-trained Transformer model to shorten long content while keeping the meaning intact.

Example:

```bash
pyai summary "Artificial Intelligence is transforming industries..."
```

Output:

```bash
Artificial Intelligence is transforming industries. Here are some of the ways it's changing the way we work. Read more at CNN.com/AI.
```

---

## 📌 Sentiment Analysis

Classify the sentiment of a given sentence as POSITIVE, NEGATIVE, or NEUTRAL.

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

---

## 📌 Image Caption Generator

Automatically generate a caption for an image.

Example:

```bash
pyai caption "<path_to_the_image>"
```

Output:

```bash
Automatically generates a relevant caption for the provided image.
```

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

## 🛠 Requirements
* Python 3.11 
* See requirements.txt for all dependencies.

---