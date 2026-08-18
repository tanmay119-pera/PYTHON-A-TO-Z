<div align="center">

# ⚙️ Python Functions & Modularity — Chapter 6

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A comprehensive masterclass on Python Functions: modular programming, DRY (Don't Repeat Yourself) principle, parameters vs arguments, default values, return statements, built-in vs user-defined functions, variable scope, and practical problem-solving algorithms.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [🧩 1. What is a Function?](#-1-what-is-a-function)
  - [Core Concept & The DRY Principle](#core-concept--the-dry-principle)
  - [Anatomy of a Function](#anatomy-of-a-function)
  - [Defining vs Calling a Function](#defining-vs-calling-a-function)
- [📥 2. Parameters vs Arguments](#-2-parameters-vs-arguments)
  - [Positional Arguments](#positional-arguments)
  - [Keyword Arguments](#keyword-arguments)
  - [Default Parameter Values](#default-parameter-values)
- [📤 3. The `return` Statement](#-3-the-return-statement)
  - [Printing vs Returning](#printing-vs-returning)
  - [Returning Multiple Values](#returning-multiple-values)
  - [Default Return Value (`None`)](#default-return-value-none)
- [🧰 4. Built-in vs User-Defined Functions](#-4-built-in-vs-user-defined-functions)
  - [Common Built-in Functions (`print`, `len`, `range`, `type`)](#common-built-in-functions)
  - [User-Defined Functions (Custom Logic)](#user-defined-functions)
- [🌐 5. Variable Scope (Local vs Global)](#-5-variable-scope-local-vs-global)
  - [Local Scope](#local-scope)
  - [Global Scope & The `global` Keyword](#global-scope--the-global-keyword)
- [💻 6. Practice Problems & Solutions (WAF)](#-6-practice-problems--solutions-waf)
  - [Problem 1: Sum and Average of Numbers](#problem-1-sum-and-average-of-numbers)
  - [Problem 2: Product of Two Numbers](#problem-2-product-of-two-numbers)
  - [Problem 3: Find Length of a List](#problem-3-find-length-of-a-list)
  - [Problem 4: Print Elements of a List on a Single Line](#problem-4-print-elements-of-a-list-on-a-single-line)
  - [Problem 5: Factorial of $n$ ($n!$)](#problem-5-factorial-of-n-n)
  - [Problem 6: USD to INR Currency Converter](#problem-6-usd-to-inr-currency-converter)
  - [Problem 7: Check Even or Odd](#problem-7-check-even-or-odd)
- [💡 7. Best Practices for Writing Clean Functions](#-7-best-practices-for-writing-clean-functions)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Overview

A **function** is a self-contained, reusable block of organized code designed to execute a specific task. Functions execute only when explicitly invoked (called).

```
   ┌───────────────────────────────────────────────────────────┐
   │                     Function Lifecycle                    │
   └─────────────────────────────┬─────────────────────────────┘
                                 ▼
   1. Define Function    ──>   def calculate_tax(income): ...
                                 ▼
   2. Pass Arguments     ──>   tax = calculate_tax(50000)
                                 ▼
   3. Execute Logic      ──>   rate * income
                                 ▼
   4. Return Output      ──>   return total_tax
```

---

## 🧩 1. What is a Function?

### Core Concept & The DRY Principle

- **DRY (Don't Repeat Yourself)**: Instead of copy-pasting code across multiple locations, write the logic once inside a function and call it whenever needed.
- **Modularity**: Decomposes large, complex systems into smaller, testable, and maintainable units.
- **Redundancy Reduction**: Fix bugs or update logic in one central place rather than hunting down duplicates throughout the codebase.

---

### Anatomy of a Function

```python
def function_name(parameter_1, parameter_2):
    """Optional docstring explaining what the function does."""
    # Function Body (Indented 4 spaces)
    result = parameter_1 + parameter_2
    return result  # Optional return value
```

| Component | Description |
| :--- | :--- |
| **`def` Keyword** | Informs Python that a function definition begins here. |
| **Function Name** | Descriptive identifier following `snake_case` naming conventions (e.g., `calc_sum`). |
| **Parentheses `()`** | Encloses input parameters (empty `()` if no inputs are required). |
| **Colon `:`** | Concludes the header line and initiates the indented block. |
| **Indentation** | Standard 4 spaces representing the body of the function. |
| **`return`** | Sends calculated values back to the caller and terminates execution of the function. |

---

### Defining vs Calling a Function

```python
# 1. FUNCTION DEFINITION (Blueprint - does not execute immediately)
def greet_user(username):
    print(f"Hello, {username}! Welcome to Python Chapter 6.")

# 2. FUNCTION CALL (Execution trigger)
greet_user("Alex")
greet_user("Sarah")
```

---

## 📥 2. Parameters vs Arguments

```
      def calculate( x , y ):  <─── Parameters (Placeholders / Inputs defined in header)
          ...
      
      calculate( 10 , 20 )     <─── Arguments (Actual concrete values passed during call)
```

### Positional Arguments

Arguments are mapped to parameters in order of their position:

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("dog", "Buddy")   # Output: I have a dog named Buddy.
describe_pet("Buddy", "dog")   # Output: I have a Buddy named dog. (Order matters!)
```

### Keyword Arguments

Pass values explicitly by referencing parameter names. Order does not matter when using keyword arguments:

```python
describe_pet(pet_name="Milo", animal_type="cat")
# Output: I have a cat named Milo.
```

### Default Parameter Values

You can assign default values to parameters. If the caller does not pass an argument, the default is used:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Tanmay")            # Output: Hello, Tanmay! (Uses default greeting)
greet("Tanmay", "Namaste") # Output: Namaste, Tanmay! (Overrides default)
```

> [!IMPORTANT]
> Non-default parameters must always appear **before** default parameters:
> ```python
> # ✅ Correct:
> def func(a, b=10): pass
>
> # ❌ SyntaxError: non-default argument follows default argument:
> # def func(a=10, b): pass
> ```

---

## 📤 3. The `return` Statement

### Printing vs Returning

- **`print()`**: Displays information to the screen/console. It cannot be used in further arithmetic operations.
- **`return`**: Passes data back to the calling statement so it can be stored in a variable, passed to another function, or used in expressions.

```python
# 1. Using print only (No return value)
def add_print(a, b):
    print(a + b)

res1 = add_print(5, 10)  # Prints: 15
print("res1 is:", res1)  # Output: res1 is: None

# 2. Using return (Productive function)
def add_return(a, b):
    return a + b

res2 = add_return(5, 10)
print("res2 * 2 =", res2 * 2)  # Output: res2 * 2 = 30
```

### Returning Multiple Values

Python functions can return multiple values packed as a tuple:

```python
def arithmetic_ops(a, b):
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    return sum_val, diff_val, prod_val

# Unpacking returned tuple
s, d, p = arithmetic_ops(10, 5)
print(f"Sum: {s}, Diff: {d}, Product: {p}")
# Output: Sum: 15, Diff: 5, Product: 50
```

### Default Return Value (`None`)

If a function does not include an explicit `return` statement, Python automatically returns `None` upon completion.

---

## 🧰 4. Built-in vs User-Defined Functions

### Common Built-in Functions

Python comes with numerous pre-installed functions ready to use:

```python
# 1. print() with custom separator and end characters
print("Python", "Java", "C++", sep=" | ", end="\n---\n")

# 2. len() - returns collection length
print("Length of list:", len([10, 20, 30, 40]))

# 3. type() - returns data type
print("Type of 42:", type(42))

# 4. range() - generates arithmetic sequence
print("Range list:", list(range(1, 6)))

# 5. sum(), max(), min()
numbers = [12, 45, 2, 99, 34]
print(f"Sum: {sum(numbers)}, Max: {max(numbers)}, Min: {min(numbers)}")
```

### User-Defined Functions

Functions created by developers to handle custom business logic:

```python
def calculate_simple_interest(principal, rate, time):
    """Calculates SI = (P * R * T) / 100"""
    si = (principal * rate * time) / 100
    return si

si_val = calculate_simple_interest(10000, 5, 2)
print("Simple Interest:", si_val)  # Output: 1000.0
```

---

## 🌐 5. Variable Scope (Local vs Global)

Scope determines where a variable can be accessed or modified in your code.

```
┌─────────────────────────────────────────────────────────────┐
│                        Global Scope                         │
│   global_x = 100                                            │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                    Local Scope                      │   │
│   │   def my_func():                                    │   │
│   │       local_y = 50  # Accessible ONLY inside        │   │
│   └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Local Scope
Variables created inside a function belong to the local scope of that function and cannot be accessed outside it.

```python
def my_func():
    x = 10  # Local variable
    print("Inside function:", x)

my_func()
# print(x)  # ❌ NameError: name 'x' is not defined
```

### Global Scope & The `global` Keyword

Variables declared outside all functions are global. To modify a global variable inside a function, use the `global` keyword:

```python
total_score = 0

def add_points(pts):
    global total_score
    total_score += pts

add_points(50)
add_points(25)
print("Total Score:", total_score)  # Output: 75
```

---

## 💻 6. Practice Problems & Solutions (WAF)

*(WAF: Write a Function / WAP: Write a Program)*

---

### Problem 1: Sum and Average of Numbers

**Task**: 
1. Create a function `calc_sum(a, b)` that returns the sum of two numbers.
2. Create a function `calc_avg(a, b, c)` that returns the average of three numbers.

```python
# 1. Sum Function
def calc_sum(a, b):
    return a + b

print("Sum (5 + 6):", calc_sum(5, 6))
print("Sum (7889 + 7923):", calc_sum(7889, 7923))

# 2. Average Function
def calc_avg(a, b, c):
    return (a + b + c) / 3

print("Average (1, 2, 6):", round(calc_avg(1, 2, 6), 2))
print("Average (88, 90, 45):", round(calc_avg(88, 90, 45), 2))
```

---

### Problem 2: Product of Two Numbers

**Task**: Write a function `calc_prod(a, b)` that multiplies two numbers and returns the result.

```python
def calc_prod(a, b):
    return a * b

print("Product (3 * 35):", calc_prod(3, 35))
print("Product (12 * 12):", calc_prod(12, 12))
```

---

### Problem 3: Find Length of a List

**Task**: Write a function `print_len(lst)` that takes a list as a parameter and returns its length.

```python
cities = ["delhi", "noida", "gurgaon", "pune", "mumbai", "chennai"]
heroes = ["thor", "iron man", "hulk", "captain america"]

def print_len(lst):
    length = len(lst)
    print(f"The list has {length} elements.")
    return length

print_len(cities)  # Output: The list has 6 elements.
print_len(heroes)  # Output: The list has 4 elements.
```

---

### Problem 4: Print Elements of a List on a Single Line

**Task**: Write a function `print_list(lst)` that prints all elements of a list on a single line separated by spaces.

```python
cities = ["delhi", "noida", "gurgaon", "pune", "mumbai", "chennai"]
heroes = ["thor", "iron man", "hulk", "tanmay"]

def print_list(lst):
    for item in lst:
        print(item, end=" ")
    print()  # New line after printing all items

print_list(heroes)  # Output: thor iron man hulk tanmay 
print_list(cities)  # Output: delhi noida gurgaon pune mumbai chennai 
```

---

### Problem 5: Factorial of $n$ ($n!$)

**Task**: Write a function `calc_fact(n)` that calculates and returns $n! = 1 \times 2 \times \dots \times n$. (By definition, $0! = 1$).

```python
def calc_fact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial of 5! =", calc_fact(5))  # Output: 120
print("Factorial of 6! =", calc_fact(6))  # Output: 720
print("Factorial of 7! =", calc_fact(7))  # Output: 5040
```

---

### Problem 6: USD to INR Currency Converter

**Task**: Write a function `converter(usd_value, conversion_rate=96)` that converts USD to INR and displays the formatted result.

```python
def converter(usd_value, conversion_rate=96):
    inr_val = usd_value * conversion_rate
    print(f"${usd_value} USD = ₹{inr_val:,} INR (Rate: 1 USD = {conversion_rate} INR)")
    return inr_val

converter(73)
converter(4567)
```

**Output:**
```text
$73 USD = ₹7,008 INR (Rate: 1 USD = 96 INR)
$4567 USD = ₹438,432 INR (Rate: 1 USD = 96 INR)
```

---

### Problem 7: Check Even or Odd

**Task**: Write a function `check_even_odd(num)` that determines whether a number is EVEN or ODD.

```python
def check_even_odd(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

print("14 is:", check_even_odd(14))  # Output: EVEN
print("27 is:", check_even_odd(27))  # Output: ODD
```

---

## 💡 7. Best Practices for Writing Clean Functions

1. **Single Responsibility Principle (SRP)**: Each function should do **one thing** and do it well.
2. **Use Descriptive Names**: Use verb-noun pairings like `calculate_tax()`, `get_user_by_id()`, `validate_email()`.
3. **Prefer `return` over `print()`**: Returning values keeps functions testable, reusable, and pure.
4. **Keep Functions Small**: A function should ideally fit on a single screen without needing endless scrolling.
5. **Document with Docstrings**: Use triple-quote docstrings `"""Docstring"""` to explain parameters, return types, and exceptions.

---

## 🚀 How to Run

1. **Verify Python Installation**:
   ```bash
   python3 --version
   ```
2. **Execute Functions File**:
   ```bash
   python3 chapter6_functions.py
   ```

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!
<div align="center">

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA!

</div>
