<div align="center">

# 🔁 PYTHON RECURSION — CHAPTER 7

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A comprehensive masterclass on Python Recursion: how recursive functions work, base cases vs. recursive steps, the call stack memory model, recursion limits, iteration vs. recursion trade-offs, and step-by-step problem walkthroughs.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [🧠 1. What is Recursion?](#-1-what-is-recursion)
  - [Core Concept](#core-concept)
  - [The Two Pillars of Recursion](#the-two-pillars-of-recursion)
  - [Visualizing the Call Stack](#visualizing-the-call-stack)
- [⚙️ 2. Python's Recursion Architecture](#️-2-pythons-recursion-architecture)
  - [Call Stack & Stack Frames](#call-stack--stack-frames)
  - [Recursion Limit (`RecursionError`)](#recursion-limit-recursionerror)
  - [Why Python Has No Tail-Call Optimization (TCO)](#why-python-has-no-tail-call-optimization-tco)
- [⚖️ 3. Recursion vs Iteration: Trade-offs](#️-3-recursion-vs-iteration-trade-offs)
  - [Pros & Cons](#pros--cons)
  - [Comparison Matrix](#comparison-matrix)
- [💻 4. Core Examples & Step-by-Step Traces](#-4-core-examples--step-by-step-traces)
  - [Example 1: Print Numbers $n$ to 1 (Countdown)](#example-1-print-numbers-n-to-1-countdown)
  - [Example 2: Factorial of $n$ ($n!$)](#example-2-factorial-of-n-n)
- [🎯 5. Practice Problems & Solutions (WAF)](#-5-practice-problems--solutions-waf)
  - [Problem 1: Sum of First $n$ Natural Numbers](#problem-1-sum-of-first-n-natural-numbers)
  - [Problem 2: Print List Elements Recursively](#problem-2-print-list-elements-recursively)
  - [Problem 3: $N^{\text{th}}$ Fibonacci Number](#problem-3-ntextth-fibonacci-number)
  - [Problem 4: Calculate Power ($a^b$) Recursively](#problem-4-calculate-power-ab-recursively)
  - [Problem 5: Reverse a String Recursively](#problem-5-reverse-a-string-recursively)
- [💡 6. Common Pitfalls & Debugging Tips](#-6-common-pitfalls--debugging-tips)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Overview

**Recursion** is a programming technique where a function solves a problem by calling a smaller instance of itself. It breaks complex problems into simpler sub-problems until reaching a trivial scenario that can be solved directly without further calls.

```
       ┌────────────────────────────────────────────────────────┐
       │                 Recursive Function Anatomy             │
       └───────────────────────────┬────────────────────────────┘
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
      1. BASE CASE                              2. RECURSIVE CASE
   (Stopping Condition)                       (Self-Call with smaller input)
   • if n == 0: return                         • return n * fact(n - 1)
   • Prevents Infinite Loops                   • Moves closer to base case
```

---

## 🧠 1. What is Recursion?

### Core Concept

When a function calls itself, Python creates a new execution context (**stack frame**) on top of the call stack. Each invocation works with its own local parameters and variables.

```python
def countdown(n):
    if n == 0:          # 1. Base Case (Stop Condition)
        print("Blast off! 🚀")
        return
    print(n)
    countdown(n - 1)    # 2. Recursive Case (Reduced Input)
```

---

### The Two Pillars of Recursion

Every recursive function must contain two essential components:

1. **The Base Case**: The terminating condition that produces an immediate result without making another recursive call. Without a base case, recursion continues infinitely until memory is exhausted.
2. **The Recursive Case**: The logical step where the function calls itself with modified arguments that progressively move closer toward the base case.

---

### Visualizing the Call Stack

Consider evaluating `fact(4)` ($4! = 24$):

```
PHASE 1: WINDING (Pushing calls to Stack)
┌────────────────────────┐
│ fact(1) -> returns 1   │ [Base Case Reached]
├────────────────────────┤
│ fact(2) -> 2 * fact(1) │
├────────────────────────┤
│ fact(3) -> 3 * fact(2) │
├────────────────────────┤
│ fact(4) -> 4 * fact(3) │
└────────────────────────┘

PHASE 2: UNWINDING (Resolving Return Values)
fact(1) = 1
fact(2) = 2 * 1 = 2
fact(3) = 3 * 2 = 6
fact(4) = 4 * 6 = 24  ===> Final Result
```

---

## ⚙️ 2. Python's Recursion Architecture

### Call Stack & Stack Frames

Every time a function is called, a **stack frame** is allocated in memory containing:
- Function arguments and local variables.
- The return address (where execution should resume once the function finishes).

### Recursion Limit (`RecursionError`)

To prevent stack overflow crashes caused by runaway infinite recursion, Python imposes a default recursion depth limit (typically **1,000** calls).

```python
import sys

# Check current recursion limit
print("Default recursion limit:", sys.getrecursionlimit())  # Usually 1000

# Changing the limit (use with caution!)
# sys.setrecursionlimit(2000)
```

If a function exceeds this threshold without hitting a base case:
```text
RecursionError: maximum recursion depth exceeded in comparison
```

### Why Python Has No Tail-Call Optimization (TCO)

Some languages (e.g., Scheme, Haskell, and certain JavaScript engines) implement **Tail-Call Optimization (TCO)**, reusing the same stack frame for tail-recursive functions.

Guido van Rossum (Python's creator) intentionally chose **not** to include TCO in Python for two main reasons:
1. **Preserving Full Stack Traces**: TCO discards intermediate stack frames, making debugging and stack traces incomplete.
2. **Language Philosophy**: Python emphasizes explicit iterative loops (`for`, `while`) as the preferred, idiomatic way to handle repetition.

---

## ⚖️ 3. Recursion vs Iteration: Trade-offs

### Pros & Cons

| Aspect | Recursion | Iteration |
| :--- | :--- | :--- |
| **Code Clarity** | Elegant for hierarchical structures (trees, graphs, JSON). | Cleaner for simple counting, linear arrays, and ranges. |
| **Memory Footprint** | $O(N)$ memory due to stack frames. | $O(1)$ memory (reuses loop variables). |
| **Execution Speed** | Slightly slower due to function call overhead. | Faster; executed directly by Python's bytecode loop engine. |
| **Risk** | Can trigger `RecursionError` if recursion is too deep. | Can cause infinite loops, but won't crash stack memory. |

---

## 💻 4. Core Examples & Step-by-Step Traces

### Example 1: Print Numbers $n$ to 1 (Countdown)

**Task**: Given integer $n$, print numbers backwards from $n$ down to $1$.

```python
def show(n):
    # Base Case: Stop when n hits 0
    if n == 0:
        return
    print(n, end=" ")
    # Recursive Case: Decrement n
    show(n - 1)

print("Countdown from 5:")
show(5)
print()
```

**Output:**
```text
Countdown from 5:
5 4 3 2 1
```

---

### Example 2: Factorial of $n$ ($n!$)

**Mathematical Definition**:
$$n! = \begin{cases} 1 & \text{if } n = 0 \text{ or } n = 1 \\ n \times (n-1)! & \text{if } n > 1 \end{cases}$$

```python
def fact(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    return n * fact(n - 1)

print("Factorial of 4! =", fact(4))  # Output: 24
print("Factorial of 6! =", fact(6))  # Output: 720
print("Factorial of 7! =", fact(7))  # Output: 5040
```

---

## 🎯 5. Practice Problems & Solutions (WAF)

*(WAF: Write a Function)*

---

### Problem 1: Sum of First $n$ Natural Numbers

**Task**: Write a recursive function `calc_sum(n)` to calculate $\sum_{i=1}^n i = 1 + 2 + \dots + n$.

**Recurrence Relation**:
$$\text{calc\_sum}(n) = n + \text{calc\_sum}(n - 1), \quad \text{with } \text{calc\_sum}(0) = 0$$

```python
def calc_sum(n):
    # Base Case
    if n == 0:
        return 0
    # Recursive Case
    return n + calc_sum(n - 1)

# Testing
n = 5
result = calc_sum(n)
print(f"Sum of first {n} numbers = {result}")  # Output: 15
print("Sum of first 10 numbers =", calc_sum(10)) # Output: 55
```

---

### Problem 2: Print List Elements Recursively

**Task**: Write a recursive function `print_list(lst, idx=0)` that traverses and prints each item in a list using the list and current index as parameters.

```python
def print_list(lst, idx=0):
    # Base Case: Stop when index reaches list length
    if idx == len(lst):
        return
    
    # Action: Print current element
    print(lst[idx], end=" ")
    
    # Recursive Case: Move to the next index
    print_list(lst, idx + 1)

fruits = ["mango", "berry", "apple", "banana"]
print("List elements printed recursively:")
print_list(fruits)
print()
```

**Output:**
```text
List elements printed recursively:
mango berry apple banana
```

> [!TIP]
> Notice the order of operations:
> - Printing **before** `print_list(lst, idx + 1)` prints forward: `mango berry apple banana`.
> - Printing **after** `print_list(lst, idx + 1)` prints in reverse: `banana apple berry mango`!

---

### Problem 3: $N^{\text{th}}$ Fibonacci Number

**Task**: Write a recursive function `fibonacci(n)` to return the $n^{\text{th}}$ Fibonacci number where $F(0) = 0, F(1) = 1$.

```python
def fibonacci(n):
    # Base Cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive Case: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence (first 8 numbers):")
for i in range(8):
    print(fibonacci(i), end=" ")
print()
# Output: 0 1 1 2 3 5 8 13
```

---

### Problem 4: Calculate Power ($a^b$) Recursively

**Task**: Compute $a^b$ recursively using $a^b = a \times a^{b-1}$ (with $a^0 = 1$).

```python
def power(base, exp):
    # Base Case
    if exp == 0:
        return 1
    # Recursive Case
    return base * power(base, exp - 1)

print("2^5 =", power(2, 5))   # Output: 32
print("3^4 =", power(3, 4))   # Output: 81
```

---

### Problem 5: Reverse a String Recursively

**Task**: Write a recursive function `reverse_string(s)` to reverse a given string.

```python
def reverse_string(s):
    # Base Case: Empty string or single character
    if len(s) <= 1:
        return s
    # Recursive Case: Last char + reverse of remaining
    return s[-1] + reverse_string(s[:-1])

print("Reverse of 'python':", reverse_string("python"))  # Output: nohtyp
print("Reverse of 'recursion':", reverse_string("recursion")) # Output: noisrucer
```

---

## 💡 6. Common Pitfalls & Debugging Tips

1. **Missing or Faulty Base Case**:
   - Always verify that your base case is reachable for all possible input domains (including $0$ and negative numbers).
2. **Incorrect Recursive Step**:
   - Ensure the arguments passed in the recursive call make strict progress towards the base case (e.g., `n - 1` or `idx + 1`).
3. **Accidental Type Errors in Recursive Calls**:
   - *Example bug from raw notes*: Calling `print_list(lst[idx])` instead of `print(lst[idx])` would pass a string instead of a list into `len(lst)`.
4. **Stack Overflow on Large Inputs**:
   - If your recursion depth exceeds 1,000, consider switching to an iterative loop with $O(1)$ space or using memoization/dynamic programming.

---

## 🚀 How to Run

1. **Verify Python Installation**:
   ```bash
   python3 --version
   ```
2. **Run Recursion Script**:
   ```bash
   python3 chapter7_recursion.py
   ```

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA!

</div>