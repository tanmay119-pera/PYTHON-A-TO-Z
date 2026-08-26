"""                                         TEXT-BASED QUIZ GAME

A beginner-friendly Python project built using:

- Lists and Dictionaries (to store quiz data)
- Functions (to organize logic into reusable blocks)
- Loops (to go through each question)
- Conditionals (to check answers and give feedback)
- f-strings (for clean output formatting)

No advanced concepts like classes are used here — everything
is broken down step-by-step so it's easy to follow."""

import time  # used only to add a small pause for better user experience

# STEP 1: Store all quiz questions in a list of dictionaries.

# Each question is a dictionary with:
#   - "question": the question text
#   - "options" : a dictionary of choices (a, b, c, d)
#   - "answer"  : the correct option 

'''Here we are making a list of dictionaries where each dictionary represents a question, its options, and 
the correct answer. This structure allows us to easily loop through the questions and access their data.'''

questions = [
    {
        "question": "What does CPU stand for?",
        "options": {
            "a": "Central Process Unit",
            "b": "Central Processing Unit",
            "c": "Computer Personal Unit",
            "d": "Central Processor Unit"
        },
        "answer": "b"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "a": "function",
            "b": "def",
            "c": "func",
            "d": "define"
        },
        "answer": "b"
    },
    {
        "question": "Which data type stores True/False values in Python?",
        "options": {
            "a": "bool",
            "b": "int",
            "c": "str",
            "d": "float"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of len('Hello')?",
        "options": {
            "a": "4",
            "b": "5",
            "c": "6",
            "d": "Error"
        },
        "answer": "b"
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": {
            "a": "//",
            "b": "<!-- -->",
            "c": "#",
            "d": "/* */"
        },
        "answer": "c"
    },
    {
        "question": "Which of these is NOT a built-in Python data structure?",
        "options": {
            "a": "list",
            "b": "tuple",
            "c": "array",
            "d": "dictionary"
        },
        "answer": "c"
    },
    {
        "question": "What will 10 % 3 return in Python?",
        "options": {
            "a": "3",
            "b": "1",
            "c": "0",
            "d": "3.33"
        },
        "answer": "b"
    },
    {
        "question": "Which loop is best when the number of iterations is known?",
        "options": {
            "a": "while",
            "b": "for",
            "c": "do-while",
            "d": "repeat"
        },
        "answer": "b"
    }
]


def display_welcome():
    """Prints a welcome banner and simple instructions."""
    print("=" * 50)
    print("        WELCOME TO THE PYTHON QUIZ GAME")
    print("=" * 50)
    print("Answer each question by typing a, b, c, or d.")
    print("Let's test your basic Python knowledge!\n")
    time.sleep(1)


def ask_question(question_data, question_number):
    """
    Displays a single question and its options, takes the
    user's input, and returns True if correct, False otherwise.
    """
    print(f"Q{question_number}. {question_data['question']}")

    # .items() lets us loop through key-value pairs of a dictionary
    for key, value in question_data["options"].items():
        print(f"   {key}) {value}")

    # Keep asking until a valid option (a/b/c/d) is entered
    user_answer = input("Your answer: ").strip().lower()
    while user_answer not in question_data["options"]:
        print("Invalid choice. Please enter a, b, c, or d.")
        user_answer = input("Your answer: ").strip().lower()

    # Compare user's answer with the correct answer
    if user_answer == question_data["answer"]:
        print("Correct!\n")
        return True
    else:
        correct_key = question_data["answer"]
        correct_text = question_data["options"][correct_key]
        print(f"Wrong! The correct answer was: {correct_key}) {correct_text}\n")
        return False


def show_result(score, total):
    """Displays the final score, percentage, and a closing message."""
    percentage = (score / total) * 100
    print("=" * 50)
    print("              QUIZ COMPLETED!")
    print("=" * 50)
    print(f"Your Score: {score}/{total} ({percentage:.2f}%)")

    if percentage >= 80:
        print("Excellent! You really know your Python basics.")
    elif percentage >= 50:
        print("Good job! A bit more practice and you'll master it.")
    else:
        print("Keep learning! Review the basics and try again.")


def main():
    """Main function that runs the entire quiz flow."""
    display_welcome()
    score = 0
    total_questions = len(questions)

    # enumerate() gives both the index and the item while looping
    for index, question_data in enumerate(questions, start=1):
        if ask_question(question_data, index):
            score += 1

    show_result(score, total_questions)

    # Ask if the user wants another round
    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if play_again == "y":
        print("\n")
        main()
    else:
        print("Thanks for playing! Goodbye.")


# This ensures main() runs only when this file is executed directly,
# not when it's imported into another script.
if __name__ == "__main__":
    main()