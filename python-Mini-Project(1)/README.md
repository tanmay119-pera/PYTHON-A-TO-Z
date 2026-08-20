<div align="center">

# 🎮 PROJECT 1: "GUESS THE NUMBER GAME"

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A classic interactive terminal game built with Python: demonstrates random number generation, while loops, conditional branching, input parsing, error handling, and score tracking.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🎯 Game Rules & Mechanics](#-game-rules--mechanics)
- [🧠 Core Concepts Applied](#-core-concepts-applied)
  - [1. Random Number Generation (`random.randint`)](#1-random-number-generation-randomrandint)
  - [2. Game Loop Architecture (`while True`)](#2-game-loop-architecture-while-true)
  - [3. Conditional Hint Logic](#3-conditional-hint-logic)
  - [4. Robust Input Validation (`try...except`)](#4-robust-input-validation-tryexcept)
- [🔄 Game Flowchart](#-game-flowchart)
- [🐛 Bug Breakdown & Fixes from Raw Notes](#-bug-breakdown--fixes-from-raw-notes)
- [💻 Complete Implementation](#-complete-implementation)
  - [Version 1: Standard Procedural Game](#version-1-standard-procedural-game)
  - [Version 2: Enhanced OOP Game with Difficulty Levels](#version-2-enhanced-oop-game-with-difficulty-levels)
- [🚀 How to Run & Play](#-how-to-run--play)
- [📄 License](#-license)

---

## 📌 Project Overview

**"Guess The Number"** is an interactive console game where the computer secretly generates a random integer within a specified range (e.g., $1$ to $100$), and the player attempts to guess it. After each guess, the game provides real-time feedback:
- **Too High / Big**: Suggests guessing a smaller number.
- **Too Low / Small**: Suggests guessing a larger number.
- **Correct**: Congratulates the user and reports the total attempts taken.
- **Quit ('Q' / 'q')**: Allows the user to exit anytime.

---

## 🎯 Game Rules & Mechanics

1. The target is an integer $T \in [1, 100]$.
2. The user has unlimited guesses (or limited in hard mode).
3. Feedback narrows down the search space following **binary search** intuition ($O(\log N)$ optimal strategy).
4. Entering `'Q'` or `'q'` aborts the game immediately.

---

## 🧠 Core Concepts Applied

### 1. Random Number Generation (`random.randint`)
The `random` module provides pseudo-random number generation:

```python
import random

# Generates an integer N such that 1 <= N <= 100 (inclusive)
target = random.randint(1, 100)
```

### 2. Game Loop Architecture (`while True`)
An infinite loop keeps the game running until a termination condition (`break`) is met:

```python
while True:
    # User interaction
    if user_wins or user_quits:
        break
```

### 3. Conditional Hint Logic
Evaluating the guess against the hidden target:

```python
if user_guess == target:
    print("🎉 Correct!")
    break
elif user_guess < target:
    print("📈 Too small! Guess a bigger number.")
else:
    print("📉 Too big! Guess a smaller number.")
```

### 4. Robust Input Validation (`try...except`)
Prevents runtime crashes if the user inputs non-numeric characters like `"hello"`:

```python
try:
    guess = int(user_input)
except ValueError:
    print("⚠️ Please enter a valid number or 'Q' to quit.")
```

---

## 🔄 Game Flowchart

```
           ┌────────────────────────┐
           │ Start: Generate Target │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ Prompt Player for Input│ ◄──────────┐
           └───────────┬────────────┘            │
                       │                         │
            Is Input == 'Q'/'q'?                 │
            ┌──────────┴──────────┐              │
       Yes  ▼                No   ▼              │
    ┌──────────────┐     Is Valid Integer?       │
    │  Exit Game   │     ┌────────┴────────┐     │
    └──────────────┘ No  ▼            Yes  ▼     │
                   ┌───────────┐    Compare Guess│
                   │ Error Msg │    ┌──────┴──────┐
                   └─────┬─────┘    │             │
                         │          ▼             ▼
                         └────► Target == Guess?  Target != Guess?
                                ┌───┴───┐         ┌───┴───┐
                           Yes  ▼       ▼ No  Low ▼       ▼ High
                           ┌─────────┐       ┌─────────┐ ┌─────────┐
                           │ You Win!│       │Hint: High│ │Hint: Low│
                           └─────────┘       └────┬────┘ └────┬────┘
                                                  └───────────┘
```

---

## 🐛 Bug Breakdown & Fixes from Raw Notes

In the initial draft:
```python
# ❌ ORIGINAL BUGGY SNIPPET:
while True:
    userChoice = input("Guess the target or quit(Q):")
    if (userChoice =="Q"):
        break 
    userChoice = int(input("guess the number : ")) # ⚠️ Double input required every round!
```

### Key Issues Fixed:
1. **Double `input()` Call**: The user was prompted twice per round (once for quit check, once for the actual number). 
   - *Fix*: Read input **once** as a string, check for `'Q'` / `'q'`, and convert to `int`.
2. **Case Sensitivity**: If the user typed `'q'` (lowercase), it was not caught.
   - *Fix*: Use `userChoice.upper() == "Q"`.
3. **No Attempt Counter**: The original version did not track how many guesses the player used.
   - *Fix*: Added `attempts += 1` to report score upon victory.

---

## 💻 Complete Implementation

### Version 1: Standard Procedural Game

```python
import random

def guess_the_number():
    target = random.randint(1, 100)
    attempts = 0

    print("=" * 45)
    print("🎯 WELCOME TO THE 'GUESS THE NUMBER' GAME! 🎯")
    print("Rules: Guess the number between 1 and 100.")
    print("Enter 'Q' anytime to quit.")
    print("=" * 45)

    while True:
        user_input = input("\n👉 Enter your guess (1-100) or 'Q' to quit: ").strip()

        # Check for quit command
        if user_input.upper() == "Q":
            print(f"\n👋 You gave up! The secret target was: {target}")
            break

        # Validate numeric input
        try:
            user_choice = int(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a whole number or 'Q'.")
            continue

        # Check range
        if user_choice < 1 or user_choice > 100:
            print("⚠️ Out of range! Please choose a number between 1 and 100.")
            continue

        attempts += 1

        # Check guess
        if user_choice == target:
            print(f"\n🎉 SUCCESS! You guessed the correct number ({target}) in {attempts} attempts! 🏆")
            break
        elif user_choice < target:
            print("📈 Your guess is TOO SMALL. Try a bigger number!")
        else:
            print("📉 Your guess is TOO BIG. Try a smaller number!")

    print("\n" + "=" * 20 + " GAME OVER " + "=" * 20)

if __name__ == "__main__":
    guess_the_number()
```

---

### Version 2: Enhanced OOP Game with Difficulty Levels

```python
import random

class NumberGuessingGame:
    DIFFICULTIES = {
        "1": ("Easy (1 - 50, 10 attempts)", 50, 10),
        "2": ("Medium (1 - 100, 7 attempts)", 100, 7),
        "3": ("Hard (1 - 200, 5 attempts)", 200, 5)
    }

    def __init__(self, max_range=100, max_attempts=7):
        self.max_range = max_range
        self.max_attempts = max_attempts
        self.target = random.randint(1, self.max_range)
        self.attempts_used = 0

    def play(self):
        print(f"\n🎮 Secret number generated between 1 and {self.max_range}!")
        print(f"You have {self.max_attempts} attempts. Enter 'Q' to exit.")

        while self.attempts_used < self.max_attempts:
            remaining = self.max_attempts - self.attempts_used
            user_input = input(f"\n[Attempts left: {remaining}] Enter guess: ").strip()

            if user_input.upper() == "Q":
                print(f"🚪 Game aborted. The secret number was {self.target}.")
                return

            try:
                guess = int(user_input)
            except ValueError:
                print("❌ Please enter a valid integer.")
                continue

            self.attempts_used += 1

            if guess == self.target:
                print(f"🏆 WINNER! You guessed {self.target} in {self.attempts_used} attempts!")
                return
            elif guess < self.target:
                print("📈 Too LOW!")
            else:
                print("📉 Too HIGH!")

        print(f"\n💀 OUT OF ATTEMPTS! The secret number was {self.target}. Better luck next time!")
```

---

## 🚀 How to Run & Play

1. **Run the Game Script**:
   ```bash
   python3 project1_guess_the_number.py
   ```
2. **Follow On-Screen Prompts**:
   - Enter integer guesses between 1 and 100.
   - Use the feedback to narrow down your next guess.
   - Enter `Q` at any prompt to quit.

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA!

</div>

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA!

</div>