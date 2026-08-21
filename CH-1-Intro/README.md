<div align="center">

# 🐍 Introduction to Python — Chapter 1

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A clean, beginner-friendly starter guide and code walkthrough covering core Python fundamentals.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Key Topics Covered](#-key-topics-covered)
  - [1. Hello World & Basic Output](#1-hello-world--basic-output)
  - [2. Variables & Data Types](#2-variables--data-types)
  - [3. Arithmetic Operations & Expressions](#3-arithmetic-operations--expressions)
  - [4. User Input Handling & Type Casting](#4-user-input-handling--type-casting)
  - [5. Conditional Logic & Ternary Operators](#5-conditional-logic--ternary-operators)
- [💡 Best Practices for Clean Code](#-best-practices-for-clean-code)
- [🚀 Getting Started](#-getting-started)
- [📄 License](#-license)

---

## 📌 Overview

This repository contains foundational concepts for learning Python, covering everything from variable declarations, arithmetic expressions, and user input to conditional statements and best practices for writing clean, maintainable Python code.

---

## 🎯 Key Topics Covered

### 1. Hello World & Basic Output
The classic entry point into Python programming.
```python
print("Hello, World!")
```

---

### 2. Variables & Data Types
Python is dynamically typed. Common primitive data types include integers, floats, strings, and booleans:

```python
name = "Tanmay"     # str
age = 18            # int
pi = 3.14           # float
is_active = True    # bool

# Check type of any variable
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
print(type(pi))     # <class 'float'>
print(type(is_active)) # <class 'bool'>
```

---

### 3. Arithmetic Operations & Expressions
Python provides rich arithmetic and floor division operations:

| Operator | Name | Example | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` (float) |
| `//` | Floor Division | `12 // 5` | `2` |
| `%` | Modulus (Remainder) | `5 % 2` | `1` |
| `**` | Exponentiation | `10 ** 5` | `100000` |

#### String Repetition & Concatenation
```python
# String multiplication (repetition)
txt = "@"
print(10 * txt * 5)     # Prints '@' 50 times

# String concatenation & repetition
c, d = "2", 3
print((c + txt) * d)    # Prints '2@2@2@'
```

---

### 4. User Input Handling & Type Casting
`input()` reads user input as a string by default. Type casting functions (`int()`, `float()`) convert string inputs into numerical types:

```python
# String input
name = input("Enter your name: ")

# Integer input
age = int(input("Enter your age: "))

# Float input
height = float(input("Enter your height in meters: "))

print(f"Hello, {name}! You are {age} years old and {height}m tall.")
```

---

### 5. Conditional Logic & Ternary Operators

#### Standard `if-elif-else`
```python
light = input("Enter the traffic light color (red, yellow, green): ")

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Caution")
elif light == "green":
    print("Go")
else:
    print("Traffic light is broken")
```

#### Single-line Ternary (`if-else` expression)
```python
food = input("Enter a food item: ")
result = "Yummy!" if food == "pizza" else "Not my favorite."
print(result)
```

#### Tuple Indexing Conditional Trick
```python
salary = int(input("Enter your salary: "))
# (False_value, True_value)[condition]
tax_rate = (0.2, 0.3)[salary > 50000]
print("Tax rate:", tax_rate)
```

---

## 💡 Best Practices for Clean Code

1. **Meaningful Variable Names**: Choose descriptive names (`user_age`, `total_price`) over single characters.
2. **Comment Purposefully**: Explain *why* something is done, not just *what* the code does.
3. **Consistent Indentation**: Always use 4 spaces per indentation level (PEP 8 standard).
4. **Avoid Global Variables**: Encapsulate logic inside functions or classes.
5. **Modular Functions**: Organize repetitive logic into reusable blocks.
6. **Graceful Error Handling**: Use `try-except` blocks to handle runtime errors cleanly.
7. **Keep It Simple & Readable (KISS)**: Prioritize readable code over overly clever one-liners.
8. **Version Control**: Use Git for versioning, atomic commits, and collaboration.
9. **Unit Testing**: Write tests to verify code reliability.
10. **Continuous Refactoring**: Regularly clean and optimize your codebase.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ installed on your system.
- Recommended IDE: [Visual Studio Code](https://code.visualstudio.com/) or [Google Antigravity](https://deepmind.google/).

### Running the Code
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/python-fundamentals.git
   cd python-fundamentals
   ```
2. Run the script:
   ```bash
   python main.py
   ```

---

<div align="center">

Made with ❤️ for learning Python | ⭐ Star this repo if you found it helpful.Author - ADESH SRIVASTAVA(TANMAY)!!

</div>
