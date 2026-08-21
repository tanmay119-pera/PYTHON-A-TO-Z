<div align="center">

# 🧮 PROJECTS 3: "SIMPLE CALCULATOR" IN PYTHON

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A modular, interactive command-line calculator in Python: demonstrates arithmetic functions, continuous game/app loops, defensive input validation (<code>try...except</code>), zero-division safeguards, and calculation history tracking.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🧠 Core Concepts Applied](#-core-concepts-applied)
  - [1. Modular Arithmetic Functions](#1-modular-arithmetic-functions)
  - [2. Interactive Control Loop (`while True`)](#2-interactive-control-loop-while-true)
  - [3. Defensive Programming & Zero-Division Safeguards](#3-defensive-programming--zero-division-safeguards)
  - [4. Input Validation with `try...except`](#4-input-validation-with-tryexcept)
- [🔄 Calculator Execution Flowchart](#-calculator-execution-flowchart)
- [💻 Code Implementations](#-code-implementations)
  - [Version 1: Standard Modular CLI Calculator](#version-1-standard-modular-cli-calculator)
  - [Version 2: Advanced OOP Calculator with Memory & History](#version-2-advanced-oop-calculator-with-memory--history)
- [📊 Feature Comparison](#-feature-comparison)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Project Overview

The **Simple Calculator** is a foundational project designed to reinforce clean function separation, user input parsing, and robust error handling.

It provides an intuitive menu-driven interface supporting:
- ➕ **Addition (`+`)**
- ➖ **Subtraction (`-`)**
- ✖️ **Multiplication (`*`)**
- ➗ **Division (`/`)** with automatic $0$-denominator protection
- 🔄 **Continuous Calculations** until the user decides to exit

---

## 🧠 Core Concepts Applied

### 1. Modular Arithmetic Functions

Each mathematical operation is encapsulated inside a pure, single-purpose function:

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
```

---

### 2. Interactive Control Loop (`while True`)

An infinite loop enables the user to perform multiple calculations in a single session without restarting the script:

```python
while True:
    # 1. Display menu
    # 2. Get operation choice
    # 3. Perform calculation
    # 4. Ask to continue or exit
    next_calc = input("Do you want to continue? (y/n): ")
    if next_calc.lower() not in ('yes', 'y'):
        print("Goodbye!")
        break
```

---

### 3. Defensive Programming & Zero-Division Safeguards

In mathematics and computing, dividing by zero is undefined and triggers a `ZeroDivisionError` in Python. Defensive logic intercepts zero denominators before division occurs:

```python
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is undefined."
    return x / y
```

---

### 4. Input Validation with `try...except`

Prevents program crashes when users enter letters or symbols instead of numeric values:

```python
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("❌ Invalid input! Please enter numeric digits.")
    continue
```

---

## 🔄 Calculator Execution Flowchart

```
           ┌────────────────────────────┐
           │        Start Program       │
           └─────────────┬──────────────┘
                         │
                         ▼
           ┌────────────────────────────┐
           │    Display Operation Menu  │ ◄────────────┐
           │  1. Add        2. Subtract │              │
           │  3. Multiply   4. Divide   │              │
           └─────────────┬──────────────┘              │
                         │                             │
                         ▼                             │
           ┌────────────────────────────┐              │
           │     Read User Choice       │              │
           └─────────────┬──────────────┘              │
                         │                             │
             Is choice in ('1','2','3','4')?           │
             ┌───────────┴───────────┐                 │
         Yes ▼                   No  ▼                 │
    ┌──────────────────┐       ┌────────────────────┐  │
    │  Read num1, num2 │       │ Show Error Message │──┘
    └────────┬─────────┘       └────────────────────┘
             │
     Valid Floats?
     ┌───────┴───────┐
 Yes ▼           No  ▼
┌─────────────────┐ ┌────────────────────┐
│ Execute Function│ │ Show "Invalid Num" │
└────────┬────────┘ └─────────┬──────────┘
         │                    │
         ▼                    │
┌─────────────────┐           │
│ Display Result  │           │
└────────┬────────┘           │
         │                    │
         ▼                    │
┌───────────────────────────┐ │
│ Perform another? (yes/no) │◄┘
└────────┬──────────────────┘
         │
     User wants to continue?
     ┌───┴───┐
 Yes ▼   No  ▼
 (Loop)    ┌──────────────┐
           │ Exit Program │
           └──────────────┘
```

---

## 💻 Code Implementations

### Version 1: Standard Modular CLI Calculator

```python
"""
Simple Python Calculator — Standard Implementation
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("=" * 45)
    print("🧮 --- Simple Python Calculator --- 🧮")
    print("=" * 45)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        choice = input("\nEnter choice (1/2/3/4): ").strip()

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input. Please enter valid numeric values.")
                continue

            if choice == '1':
                print(f"👉 Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"👉 Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"👉 Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                res = divide(num1, num2)
                if isinstance(res, str):
                    print(f"⚠️ {res}")
                else:
                    print(f"👉 Result: {num1} / {num2} = {res}")

            # Check for another calculation
            next_calc = input("\nDo you want to perform another calculation? (yes/no): ").strip()
            if next_calc.lower() not in ('yes', 'y'):
                print("\n👋 Thank you for using Simple Calculator. Goodbye!")
                break
        else:
            print("⚠️ Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    calculator()
```

---

### Version 2: Advanced OOP Calculator with Memory & History

```python
"""
Advanced Object-Oriented Calculator with History Tracking
"""

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        res = a + b
        self._record(f"{a} + {b} = {res}")
        return res

    def subtract(self, a, b):
        res = a - b
        self._record(f"{a} - {b} = {res}")
        return res

    def multiply(self, a, b):
        res = a * b
        self._record(f"{a} * {b} = {res}")
        return res

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        res = a / b
        self._record(f"{a} / {b} = {res}")
        return res

    def power(self, a, b):
        res = a ** b
        self._record(f"{a} ^ {b} = {res}")
        return res

    def _record(self, entry):
        self.history.append(entry)

    def show_history(self):
        if not self.history:
            print("No calculations recorded yet.")
        else:
            print("\n📜 --- Calculation History ---")
            for idx, item in enumerate(self.history, start=1):
                print(f"  {idx}. {item}")
```

---

## 📊 Feature Comparison

| Feature | Basic Script | Version 1 (Modular) | Version 2 (OOP + History) |
| :--- | :---: | :---: | :---: |
| **Basic Arithmetic (`+`, `-`, `*`, `/`)** | ✅ | ✅ | ✅ |
| **Division by Zero Protection** | ❌ (Crashes) | ✅ | ✅ |
| **Input Error Validation (`try...except`)** | ❌ (Crashes) | ✅ | ✅ |
| **Continuous Calculation Loop** | ❌ | ✅ | ✅ |
| **Power / Exponentiation (`^`)** | ❌ | ❌ | ✅ |
| **Audit / Calculation History** | ❌ | ❌ | ✅ |

---

## 🚀 How to Run

1. **Verify Python Installation**:
   ```bash
   python3 --version
   ```
2. **Execute Calculator**:
   ```bash
   python3 project3_simple_calculator.py
   ```

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA(TANMAY)!

</div>