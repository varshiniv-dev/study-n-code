# magic8.py
import random


def main():
    print("🎱 Magic 8-Ball - Ask a Yes or No question\n")

    question = input("Your question: ")

    responses = [
        "Yes, definitely.",
        "No, certainly not.",
        "It is decidedly so.",
        "Ask again later.",
        "Cannot predict now.",
        "Very doubtful.",
        "Without a doubt.",
        "Outlook not so good.",
        "Signs point to yes.",
        "My sources say no.",
        "Better not tell you now.",
        "Concentrate and ask again."
    ]

    answer = random.choice(responses)

    print(f"\nMagic 8-Ball says: {answer}")


if __name__ == "__main__":
    main()
