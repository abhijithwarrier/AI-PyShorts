import argparse
from pyai_shorts import ai

def main():
    parser = argparse.ArgumentParser(description="AI-Shorts CLI")
    parser.add_argument("task", choices=["summary", "sentiment", "caption", "translate", "ner"], help="Task to perform")
    parser.add_argument("input", help="Input text or image path")
    parser.add_argument("--src-lang", default="en", help="Source language for translation")
    parser.add_argument("--tgt-lang", default="fr", help="Target language for translation")
    parser.add_argument("--aggregation-strategy", default="simple", help="Aggregation strategy for NER")
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

if __name__ == "__main__":
    main()
