import requests
import json
import random

# Fetch trivia questions from Open Trivia Database API
url = 'https://opentdb.com/api.php?amount=10&type=multiple'
response = requests.get(url)
data = json.loads(response.text)
questions = data['results']

# Function to ask question


def ask_question(question):
    options = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(options)

    print(question['question'])
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = input("Enter your answer (1-4): ")

    # Determine correct answer
    correct_answer = options.index(question['correct_answer']) + 1

    if int(user_answer) == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Incorrect. Correct answer was: {question['correct_answer']}\n")
        return 0

# Run the quiz


def run_quiz():
    score = 0
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}:")
        score += ask_question(question)

    print(f"\nYour score: {score}/{len(questions)}")


# Run
run_quiz()
3
