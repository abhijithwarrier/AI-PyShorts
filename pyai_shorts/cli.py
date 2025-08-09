import argparse
from pyai_shorts import ai

def main():
    parser = argparse.ArgumentParser(description="AI-Shorts CLI")
    parser.add_argument("task", choices=["summary"], help="Task to perform")
    parser.add_argument("input", help="Input text or image path")
    args = parser.parse_args()

    if args.task == "summary":
        print(ai.summary(args.input))

if __name__ == "__main__":
    main()
