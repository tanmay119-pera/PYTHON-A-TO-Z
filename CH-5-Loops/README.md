<div align="center">

# 🔄 PYTHON LOOPS & ITERATION — CHAPTER 5

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A comprehensive masterclass on Python's iterative control flow: <code>while</code> loops, <code>for</code> loops, the <code>range()</code> function, loop control statements (<code>break</code>, <code>continue</code>, <code>pass</code>), <code>else</code> clauses in loops, and practical problem-solving algorithms.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [🔄 1. The `while` Loop](#-1-the-while-loop)
  - [Syntax & Working Principle](#syntax--working-principle)
  - [Iterators & Loop Counters](#iterators--loop-counters)
  - [Avoiding Infinite Loops](#avoiding-infinite-loops)
- [🔁 2. The `for` Loop](#-2-the-for-loop)
  - [Sequential Traversal over Iterables](#sequential-traversal-over-iterables)
  - [Traversing Lists, Tuples, and Strings](#traversing-lists-tuples-and-strings)
  - [Using `enumerate()` for Index-Value Pairs](#using-enumerate-for-index-value-pairs)
- [🎯 3. The `range()` Function](#-3-the-range-function)
  - [`range(stop)`](#rangestop)
  - [`range(start, stop)`](#rangestart-stop)
  - [`range(start, stop, step)`](#rangestart-stop-step)
  - [Negative Step & Reverse Counting](#negative-step--reverse-counting)
- [🛑 4. Loop Control Statements](#-4-loop-control-statements)
  - [`break` Statement](#break-statement)
  - [`continue` Statement](#continue-statement)
  - [`pass` Statement](#pass-statement)
- [🧩 5. Loops with `else` Clause](#-5-loops-with-else-clause)
  - [`for...else` Mechanics](#forelse-mechanics)
  - [`while...else` Mechanics](#whileelse-mechanics)
  - [How `break` Affects `else`](#how-break-affects-else)
- [💻 6. Practice Problems & Solutions (WAP)](#-6-practice-problems--solutions-wap)
  - [Problem 1: Print Numbers 1 to 100](#problem-1-print-numbers-1-to-100)
  - [Problem 2: Print Numbers 100 down to 1](#problem-2-print-numbers-100-down-to-1)
  - [Problem 3: Multiplication Table of $n$](#problem-3-multiplication-table-of-n)
  - [Problem 4: Traverse Elements in a List](#problem-4-traverse-elements-in-a-list)
  - [Problem 5: Linear Search in a Tuple/List](#problem-5-linear-search-in-a-tuplelist)
  - [Problem 6: Sum of First $n$ Natural Numbers](#problem-6-sum-of-first-n-natural-numbers)
  - [Problem 7: Factorial of a Number $n!$](#problem-7-factorial-of-a-number-n)
- [⚖️ 7. Comparison: `while` Loop vs `for` Loop](#️-7-comparison-while-loop-vs-for-loop)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Overview

A **loop** is a control flow statement used to execute a block of code repeatedly until a specified condition is satisfied.

Python provides two primary loop constructs:
1. **`while` loop**: Condition-driven loop — repeatedly executes code as long as a boolean condition evaluates to `True`.
2. **`for` loop**: Collection/Sequence-driven loop — traverses items across an iterable (list, tuple, string, dictionary, set, or generator like `range()`).

```
┌─────────────────────────────────────────────────────────────┐
│                       Loop Types                            │
├──────────────────────────────┬──────────────────────────────┤
│         while Loop           │           for Loop           │
│   • Condition-based          │   • Sequence/Iterable-based  │
│   • Used when number of      │   • Used when iterating over │
│     iterations is unknown    │     a known collection/range │
└──────────────────────────────┴──────────────────────────────┘
```

---

## 🔄 1. The `while` Loop

### Syntax & Working Principle

```python
while condition:
    # Code block to execute
    # Update loop counter / state
```

1. The `condition` is evaluated.
2. If `True`, the code block inside the loop executes.
3. Once the block completes, the condition is evaluated again.
4. If `False`, the loop terminates and control jumps to the next statement outside the loop.

### Iterators & Loop Counters

A variable used to control the number of repetitions is called an **iterator** or **loop counter**.

```python
# Print "Hello World" 5 times
count = 1
while count <= 5:
    print(f"[{count}] Hello World")
    count += 1  # Increment counter (CRITICAL: prevents infinite loop)

print("Loop completed. Final count value:", count)
```

**Output:**
```text
[1] Hello World
[2] Hello World
[3] Hello World
[4] Hello World
[5] Hello World
Loop completed. Final count value: 6
```

### Avoiding Infinite Loops

An **infinite loop** occurs when the loop condition never evaluates to `False`.

```python
# ⚠️ CAUTION: Infinite Loop Example
# while 2 == 2:
#     print("This will run forever!")

# ⚠️ Bug Example: Forgetting to increment
# i = 1
# while i <= 5:
#     print(i)
#     # Missing i += 1 -> 'i' remains 1 forever!
```

> [!WARNING]
> Always ensure your `while` loop has a deterministic state update (e.g., `i += 1` or a condition trigger) that guarantees termination.

---

## 🔁 2. The `for` Loop

### Sequential Traversal over Iterables

Python's `for` loop functions like a `for-each` iterator in other languages. It steps through each item in any sequence or iterable object without needing manual index management.

```python
for item in sequence:
    # Statement(s) executed for each item
```

### Traversing Lists, Tuples, and Strings

```python
# 1. Traversing a List
veggies = ["potato", "tomato", "lady finger", "brinjal"]
print("--- Vegetables ---")
for item in veggies:
    print(item)

# 2. Traversing a Tuple
numbers = (10, 20, 30, 40, 50)
print("\n--- Tuple Items ---")
for val in numbers:
    print(val)

# 3. Traversing a String
text = "Python"
print("\n--- String Characters ---")
for char in text:
    print(char)
```

### Using `enumerate()` for Index-Value Pairs

When you need both the index and value during iteration, use Python's built-in `enumerate()`:

```python
fruits = ["Apple", "Banana", "Cherry"]

for idx, fruit in enumerate(fruits):
    print(f"Index {idx} -> {fruit}")
```

---

## 🎯 3. The `range()` Function

The built-in `range()` function generates an immutable sequence of integers. It is memory-efficient because it calculates values on demand rather than storing all integers in memory.

### `range(stop)`
Starts from `0` (default) and ends at `stop - 1` with a step size of `1`.

```python
for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4
```

### `range(start, stop)`
Starts from `start` and ends at `stop - 1` with a default step size of `1`.

```python
for i in range(2, 7):
    print(i, end=" ")
# Output: 2 3 4 5 6
```

### `range(start, stop, step)`
Starts from `start`, increments by `step`, and stops before reaching `stop`.

```python
# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i, end=" ")
# Output: 2 4 6 8 10
```

### Negative Step & Reverse Counting

By providing a negative `step`, you can count backwards:

```python
# Count down from 5 to 1
for i in range(5, 0, -1):
    print(i, end=" ")
# Output: 5 4 3 2 1
```

---

## 🛑 4. Loop Control Statements

Loop control statements alter the standard sequential execution flow.

```
       ┌───────────────────────┐
       │ Loop Control Keywords │
       └───────────┬───────────┘
   ┌───────────────┼───────────────┐
   ▼               ▼               ▼
 break         continue          pass
(Exit loop)   (Skip step)    (Placeholder)
```

### `break` Statement
Terminates the current loop immediately and transfers execution to the statement following the loop.

```python
i = 1
while i <= 10:
    if i == 5:
        print(f"Reached {i}, breaking out of loop!")
        break
    print(i, end=" ")
    i += 1

print("\nCode outside loop resumed.")
# Output:
# 1 2 3 4 Reached 5, breaking out of loop!
# Code outside loop resumed.
```

---

### `continue` Statement
Skips the rest of the current iteration and jumps to the next evaluation/iteration of the loop.

```python
# Print numbers from 1 to 5, skipping 3
for i in range(1, 6):
    if i == 3:
        print("[Skipping 3]")
        continue
    print(f"Number: {i}")

# Output:
# Number: 1
# Number: 2
# [Skipping 3]
# Number: 4
# Number: 5
```

> [!IMPORTANT]
> In `while` loops, ensure the counter increment occurs **before** the `continue` call, or update it inside the `if` branch before skipping; otherwise, you may trigger an infinite loop.

---

### `pass` Statement
The `pass` statement is a null operation (no-op). It serves as a syntactic placeholder where code is required but no action should be performed.

```python
# Placeholder in loop structure
for i in range(5):
    pass  # To be implemented later

# Placeholder in condition
if True:
    pass

print("Executed smoothly without syntax errors.")
```

---

## 🧩 5. Loops with `else` Clause

Python uniquely allows an optional `else` block with both `for` and `while` loops.

### `for...else` Mechanics
The `else` block executes **only when the loop completes all iterations normally** (i.e., without being interrupted by a `break`).

```python
items = [1, 2, 3, 4, 5]

for item in items:
    print(item, end=" ")
else:
    print("\n-> All items traversed successfully!")
```

### `while...else` Mechanics
The `else` block executes when the `while` condition evaluates to `False`.

```python
count = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1
else:
    print("-> While loop completed its condition.")
```

### How `break` Affects `else`

If a loop is terminated via `break`, the `else` block is **skipped completely**. This makes it an ideal construct for search algorithms!

```python
numbers = [10, 20, 30, 40, 50]
target = 99

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was NOT found in the list.")
# Output: 99 was NOT found in the list.
```

---

## 💻 6. Practice Problems & Solutions (WAP)

### Problem 1: Print Numbers 1 to 100

**Task**: Print integers from `1` to `100` using both `while` and `for` loops.

#### Solution using `while` loop:
```python
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1
print()
```

#### Solution using `for` loop:
```python
for i in range(1, 101):
    print(i, end=" ")
print()
```

---

### Problem 2: Print Numbers 100 down to 1

**Task**: Print integers from `100` down to `1` in reverse order.

#### Solution using `while` loop:
```python
i = 100
while i >= 1:
    print(i, end=" ")
    i -= 1
print()
```

#### Solution using `for` loop:
```python
for i in range(100, 0, -1):
    print(i, end=" ")
print()
```

---

### Problem 3: Multiplication Table of $n$

**Task**: Prompt user for an integer $n$ and output its multiplication table up to $n \times 10$.

#### Solution using `while` loop:
```python
n = int(input("Enter number: "))

i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
```

#### Solution using `for` loop:
```python
n = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

---

### Problem 4: Traverse Elements in a List

**Task**: Given a list of square numbers:
`nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`, print all elements using a loop.

#### Method 1: `while` loop with index tracking
```python
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(f"Index [{idx}] = {nums[idx]}")
    idx += 1
```

#### Method 2: `for` loop (Direct element iteration)
```python
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in nums:
    print(val, end=" ")
print()
```

---

### Problem 5: Linear Search in a Tuple/List

**Task**: Search for target value $x$ in a tuple. If found, print its index and stop; if not found, inform the user.

#### Method 1: Using `for...else` with `enumerate()`
```python
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36

for idx, el in enumerate(nums):
    if el == x:
        print(f"Target {x} FOUND at index {idx}")
        break
else:
    print(f"Target {x} NOT found in sequence.")
```

#### Method 2: Using `while` loop
```python
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49

idx = 0
found = False

while idx < len(nums):
    if nums[idx] == x:
        print(f"Target {x} FOUND at index {idx}")
        found = True
        break
    idx += 1

if not found:
    print(f"Target {x} NOT found in sequence.")
```

---

### Problem 6: Sum of First $n$ Natural Numbers

**Task**: Calculate the sum $\sum_{i=1}^{n} i = 1 + 2 + \dots + n$ for a given $n$.

#### Solution using `while` loop:
```python
n = 5
total_sum = 0
i = 1

while i <= n:
    total_sum += i
    i += 1

print(f"Sum of first {n} numbers = {total_sum}")
# Output for n=5: 15
```

#### Solution using `for` loop:
```python
n = 5
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"Sum of first {n} numbers = {total_sum}")
# Output: 15
```

---

### Problem 7: Factorial of a Number $n!$

**Task**: Calculate $n! = 1 \times 2 \times 3 \times \dots \times n$ (with $0! = 1$).

#### Solution using `for` loop:
```python
n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} ({n}!) = {factorial}")
# Output for n=5: 120
```

#### Solution using `while` loop:
```python
n = 5
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"Factorial of {n} ({n}!) = {factorial}")
# Output: 120
```

---

## ⚖️ 7. Comparison: `while` Loop vs `for` Loop

| Feature | `for` Loop | `while` Loop |
| :--- | :--- | :--- |
| **Primary Use Case** | When number of iterations or iterable is known | When loop termination depends on dynamic condition |
| **Iteration Mechanism** | Automatic sequence traversal via iterators | Manual index/counter management |
| **Condition Check** | Handled implicitly per item in collection | Explicitly evaluated before every cycle |
| **Risk of Infinite Loop** | Minimal (finite sequences terminate automatically) | Higher (if loop counter/state update is missing) |
| **Readability** | Cleaner & more Pythonic for sequences and ranges | Better for polling, event loops, or game loops |

---

## 🚀 How to Run

1. **Verify Python Installation**:
   ```bash
   python3 --version
   ```
2. **Execute Any Script**:
   ```bash
   python3 filename.py
   ```

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!
---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA!

</div>