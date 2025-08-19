import argparse
from pyai_shorts import ai

def main():
    parser = argparse.ArgumentParser(description="AI-Shorts CLI")
    parser.add_argument("task", choices=[
        "summary", "sentiment", "caption", "translate", "ner", "paraphrase", "detectlang", "keywords", "tts"
    ], help="Task to perform")
    parser.add_argument("input", help="Input text or image path")

    # Arguments for translation
    parser.add_argument("--src-lang", default="en", help="Source language for translation")
    parser.add_argument("--tgt-lang", default="fr", help="Target language for translation")

    # Argument for NER
    parser.add_argument("--aggregation-strategy", default="simple", help="Aggregation strategy for NER")

    # Arguments for paraphraser
    parser.add_argument("--num", type=int, default=1, help="Number of paraphrases (default 1)")
    parser.add_argument("--maxlen", type=int, default=60, help="Max length of each paraphrase")

    # Arguments for keywords
    parser.add_argument("--topk", type=int, default=10, help="Top K keywords (keywords)")
    parser.add_argument("--ngmin", type=int, default=1, help="Min n-gram (keywords)")
    parser.add_argument("--ngmax", type=int, default=2, help="Max n-gram (keywords)")
    parser.add_argument("--method", default="mmr", choices=["mmr", "maxsum", "simple"],
                        help="Selection method (keywords)")
    parser.add_argument("--diversity", type=float, default=0.5, help="MMR diversity 0-1 (keywords)")

    # Arguments for TTS
    parser.add_argument("--lang", default="en", help="TTS language code (e.g., en, es, fr, de, hi)")
    parser.add_argument("--out", default="speech.wav", help="Output WAV file path")

    args = parser.parse_args()

    if args.task == "summary":
        print(ai.summary(args.input))
    elif args.task == "sentiment":
        print(ai.sentiment(args.input))
    elif args.task == "caption":
        print(ai.caption(args.input))
    elif args.task == "translate":
        print(ai.translate(args.input))
    elif args.task == "ner":
        print(ai.ner(args.input))
    elif args.task == "paraphrase":
        print(ai.paraphrase(args.input, num=args.num, max_length=args.maxlen))
    elif args.task == "detectlang":
        print(ai.detect_lang(args.input))
    elif args.task == "keywords":
        print(ai.keywords(args.input, top_k=args.topk, ngram_min=args.ngmin, ngram_max=args.ngmax,
                          method=args.method, diversity=args.diversity))
    elif args.task == "tts":
        print(ai.tts(args.input, out_path=args.out, lang=args.lang))

if __name__ == "__main__":
    main()
