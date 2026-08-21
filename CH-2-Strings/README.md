<div align="center">

# 🧵 PYTHON STRINGS & CONDITIONAL LOGIC — CHAPTER 2

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>An in-depth guide covering Python strings, indexing & slicing, built-in string methods, nested conditionals, and hands-on practice problems (WAPs).</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [🔤 1. String Fundamentals](#-1-string-fundamentals)
  - [Definition & Initialization](#definition--initialization)
  - [Concatenation & Length](#concatenation--length)
  - [Escape Sequences](#escape-sequences)
- [🎯 2. Indexing & Slicing](#-2-indexing--slicing)
  - [Positive & Negative Indexing](#positive--negative-indexing)
  - [String Slicing Syntax & Examples](#string-slicing-syntax--examples)
- [🛠️ 3. Built-in String Functions & Methods](#️-3-built-in-string-functions--methods)
- [🔀 4. Conditional Logic & Nested Ifs](#-4-conditional-logic--nested-ifs)
- [💻 5. Practice Problems & Solutions (WAP)](#-5-practice-problems--solutions-wap)
  - [Problem 1: Name Length Counter](#problem-1-name-length-counter)
  - [Problem 2: Count Character Occurrences](#problem-2-count-character-occurrences)
  - [Problem 3: Grading System](#problem-3-grading-system)
  - [Problem 4: Even or Odd Checker](#problem-4-even-or-odd-checker)
  - [Problem 5: Largest of Three Numbers](#problem-5-largest-of-three-numbers)
  - [Problem 6: Leap Year Checker](#problem-6-leap-year-checker)
  - [Problem 7: Palindrome String Checker](#problem-7-palindrome-string-checker)
  - [Problem 8: Multiple of 7 Checker](#problem-8-multiple-of-7-checker)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Overview

Strings are one of the most widely used data types in Python. This guide covers string manipulation from the ground up: indexing systems, slicing mechanics, essential string methods, and algorithmic practice questions with clean solutions.

---

## 🔤 1. String Fundamentals

### Definition & Initialization
A **string** in Python is an immutable sequence of Unicode characters enclosed in quotes:
```python
str1 = 'Single quoted string'
str2 = "Double quoted string"
str3 = '''Triple quoted multi-line string'''
```

### Concatenation & Length
Join strings using the `+` operator and calculate character count using `len()`:
```python
str1 = "Hello"
str2 = "World"
full_str = str1 + " " + str2
print(full_str)        # Output: Hello World
print(len(full_str))   # Output: 11 (includes space)
```

### Escape Sequences
Escape characters allow inserting special formatting within strings:

| Escape Sequence | Description | Example |
| :--- | :--- | :--- |
| `\n` | Newline (line break) | `"Line 1\nLine 2"` |
| `\t` | Tab space | `"Name:\tTanmay"` |
| `\\` | Backslash | `"C:\\Users\\Path"` |
| `\'` / `\"` | Single / Double Quote | `"God\'s plan"` |

```python
str1 = "This is a string.\nWe are learning Python programming."
print(str1)
```

---

## 🎯 2. Indexing & Slicing

### Positive & Negative Indexing
Every character in a Python string is assigned a forward (0-based) and reverse (-1-based) index:

```text
 String:   P   y   t   h   o   n
----------------------------------
Positive:  0   1   2   3   4   5
Negative: -6  -5  -4  -3  -2  -1
```

#### Code Example:
```python
word = "Python"

# Positive indexing
print(word[0])   # 'P' (First character)
print(word[3])   # 'h'

# Negative indexing
print(word[-1])  # 'n' (Last character)
print(word[-3])  # 'h' (3rd from end)
```

### String Slicing Syntax & Examples
Slicing extracts a substring using `string[start : end : step]` (where `end` index is excluded):

```python
text = "Royal Challenger Bangalore"

print(text[0:5])    # 'Royal'        (index 0 to 4)
print(text[6:17])   # 'Challenger'   (index 6 to 16)
print(text[:5])     # 'Royal'        (from start to index 4)
print(text[6:])     # 'Challenger Bangalore' (from index 6 to end)
print(text[::-1])   # 'erolagnaB regnellahC layoR' (reversed string)
```

---

## 🛠️ 3. Built-in String Functions & Methods

| Method | Description | Example (`text = "I am a coding enthusiast."`) | Output |
| :--- | :--- | :--- | :--- |
| `.endswith(suffix)` | Checks if string ends with specified suffix | `text.endswith("enthusiast.")` | `True` |
| `.startswith(prefix)` | Checks if string starts with specified prefix | `text.startswith("I am")` | `True` |
| `.upper()` | Converts string to uppercase | `text.upper()` | `"I AM A CODING ENTHUSIAST."` |
| `.lower()` | Converts string to lowercase | `text.lower()` | `"i am a coding enthusiast."` |
| `.capitalize()` | Capitalizes 1st character, lowercases rest | `text.capitalize()` | `"I am a coding enthusiast."` |
| `.replace(old, new)` | Replaces occurrences of substring | `text.replace("coding", "AI")` | `"I am a AI enthusiast."` |
| `.find(sub)` | Returns lowest index of substring (`-1` if not found) | `text.find("coding")` | `7` |
| `.count(sub)` | Counts non-overlapping occurrences of substring | `text.count("a")` | `2` |
| `.split(sep)` | Splits string into a list of words | `text.split()` | `['I', 'am', 'a', 'coding', 'enthusiast.']` |

---

## 🔀 4. Conditional Logic & Nested Ifs

Nested conditionals allow testing layered logic:

```python
age = int(input("Enter your age: "))

if age >= 18:
    if age < 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
else:
    print("You are a minor.")
```

---

## 💻 5. Practice Problems & Solutions (WAP)

### Problem 1: Name Length Counter
> **WAP to input user's name and print its length.**

```python
name = input("Enter your name: ")
name_length = len(name)
print(f"The length of your name is: {name_length}")
```

---

### Problem 2: Count Character Occurrences
> **WAP to find the occurrence of '$' in a given string.**

```python
sample_text = "$100 is equal to $100 dollars in $$ accounts $"
count_dollar = sample_text.count('$')
print("The occurrence of '$' is:", count_dollar)
```

---

### Problem 3: Grading System
> **WAP to assign student grades based on marks:**
> - $\ge 90 \rightarrow \text{Grade A}$
> - $80 - 89 \rightarrow \text{Grade B}$
> - $70 - 79 \rightarrow \text{Grade C}$
> - $60 - 69 \rightarrow \text{Grade D}$
> - $< 60 \rightarrow \text{Grade F}$

```python
marks = int(input("Enter student marks (0-100): "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Student Grade: {grade}")
```

---

### Problem 4: Even or Odd Checker
> **WAP to check if a given number is even or odd.**

```python
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")
```

---

### Problem 5: Largest of Three Numbers
> **WAP to find the largest among three numbers provided by the user.**

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")
```

---

### Problem 6: Leap Year Checker
> **WAP to check if a given year is a leap year.**
> *Rule: Divisible by 4 and not divisible by 100, OR divisible by 400.*

```python
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year! 🎉")
else:
    print(f"{year} is NOT a leap year.")
```

---

### Problem 7: Palindrome String Checker
> **WAP to check if a string is a palindrome (reads the same forward and backward).**

```python
text = input("Enter a string: ")

# Clean case sensitivity and check reverse
if text.lower() == text.lower()[::-1]:
    print(f"'{text}' is a Palindrome! ✅")
else:
    print(f"'{text}' is NOT a palindrome. ❌")
```

---

### Problem 8: Multiple of 7 Checker
> **WAP to check if a number is a multiple of 7.**

```python
num = int(input("Enter a number: "))

if num % 7 == 0:
    print(f"{num} is a multiple of 7.")
else:
    print(f"{num} is NOT a multiple of 7.")
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Open terminal in the project directory:
   ```bash
   python chapter2_strings.py
   ```

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it useful. Author - ADESH SRIVASTAVA(TANMAY)!

</div>
