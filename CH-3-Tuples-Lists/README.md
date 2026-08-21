<div align="center">

# 📦 PYTHON LISTS & TUPLES — CHAPTER 3

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A comprehensive masterclass on Python's core sequence data structures: Lists (mutable) and Tuples (immutable), complete with methods, slicing techniques, and practice problems (WAP).</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [📋 1. Python Lists (Mutable Sequences)](#-1-python-lists-mutable-sequences)
  - [Key Characteristics](#key-characteristics)
  - [Creating & Accessing Elements](#creating--accessing-elements)
  - [Slicing Lists](#slicing-lists)
  - [Modifying Elements (Mutability)](#modifying-elements-mutability)
  - [List Methods Reference](#list-methods-reference)
- [🔒 2. Python Tuples (Immutable Sequences)](#-2-python-tuples-immutable-sequences)
  - [Key Characteristics](#key-characteristics-1)
  - [Creating Tuples & The Single-Element Comma Rule](#creating-tuples--the-single-element-comma-rule)
  - [Slicing Tuples](#slicing-tuples)
  - [Tuple Methods Reference](#tuple-methods-reference)
- [⚖️ 3. List vs Tuple: Quick Comparison](#️-3-list-vs-tuple-quick-comparison)
- [💻 4. Practice Problems & Solutions (WAP)](#-4-practice-problems--solutions-wap)
  - [Problem 1: Favorite Movies Collector](#problem-1-favorite-movies-collector)
  - [Problem 2: Palindrome List Checker](#problem-2-palindrome-list-checker)
  - [Problem 3: Count Grade Occurrences in Tuple](#problem-3-count-grade-occurrences-in-tuple)
  - [Problem 4: Convert Tuple to List & Sort](#problem-4-convert-tuple-to-list--sort)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Overview

Sequences are ordered collections of items in Python. Understanding when to use a **List** (when elements need to change, grow, or shrink) versus a **Tuple** (when elements represent fixed, immutable records) is essential for writing efficient Python code.

---

## 📋 1. Python Lists (Mutable Sequences)

### Key Characteristics
1. **Mutable**: Elements can be modified, appended, or removed after creation.
2. **Ordered**: Elements maintain their insertion order.
3. **Heterogeneous**: Can hold integers, floats, strings, objects, and nested lists.
4. **Indexed & Sliceable**: Supports both positive and negative indexing.

---

### Creating & Accessing Elements
```python
# List with mixed data types
student = ["Tanmay", 18, 92.5, True]

print(student)        # Output: ['Tanmay', 18, 92.5, True]
print(type(student))  # Output: <class 'list'>
print(len(student))   # Output: 4
print(student[0])     # Output: 'Tanmay' (First element)
print(student[-1])    # Output: True (Last element)
```

---

### Slicing Lists
Extract sublists using `list[start : end : step]`:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])   # [3, 4, 5]     (Index 2 to 4)
print(numbers[:4])    # [1, 2, 3, 4]  (Beginning to index 3)
print(numbers[5:])    # [6, 7, 8, 9]  (Index 5 to end)
print(numbers[-3:])   # [7, 8, 9]     (Last 3 elements)
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1] (Reversed)
```

---

### Modifying Elements (Mutability)
Unlike strings, lists allow direct in-place assignment:

```python
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'blueberry'  # Change 'banana' to 'blueberry'
print(fruits)            # Output: ['apple', 'blueberry', 'cherry']
```

---

### List Methods Reference

| Method | Description | Example (`fruits = ['apple', 'banana']`) | Result |
| :--- | :--- | :--- | :--- |
| `.append(x)` | Adds item `x` to the end of the list | `fruits.append('orange')` | `['apple', 'banana', 'orange']` |
| `.insert(i, x)` | Inserts item `x` at specified index `i` | `fruits.insert(1, 'grape')` | `['apple', 'grape', 'banana', ...]` |
| `.remove(x)` | Removes the first occurrence of item `x` | `fruits.remove('banana')` | Removes `'banana'` |
| `.pop(i)` | Removes and returns item at index `i` (default last) | `popped = fruits.pop()` | Returns removed item |
| `.sort()` | Sorts items in ascending order (in-place) | `fruits.sort()` | Alphabetical/numerical sort |
| `.reverse()` | Reverses the list elements in-place | `fruits.reverse()` | Reversed order |
| `.copy()` | Returns a shallow copy of the list | `new_list = fruits.copy()` | Independent list clone |
| `.clear()` | Removes all elements from the list | `fruits.clear()` | `[]` |

```python
# Demonstration of list operations
fruits = ['apple', 'banana', 'cherry']

fruits.append('orange')       # ['apple', 'banana', 'cherry', 'orange']
fruits.insert(1, 'grape')     # ['apple', 'grape', 'banana', 'cherry', 'orange']
fruits.remove('cherry')       # ['apple', 'grape', 'banana', 'orange']
popped_item = fruits.pop()    # Returns 'orange', leaves ['apple', 'grape', 'banana']
fruits.sort()                 # ['apple', 'banana', 'grape']
fruits.reverse()              # ['grape', 'banana', 'apple']
```

---

## 🔒 2. Python Tuples (Immutable Sequences)

### Key Characteristics
1. **Immutable**: Once defined, elements cannot be added, changed, or deleted.
2. **Defined with Parentheses `()`**: Or simply comma-separated values.
3. **Faster & Memory Efficient**: Tuples consume less memory and execute faster than lists.
4. **Hashable / Dictionary Keys**: Because they are immutable, tuples can be used as dictionary keys and set elements.

---

### Creating Tuples & The Single-Element Comma Rule
> [!IMPORTANT]
> A single item enclosed in parentheses without a trailing comma is evaluated as a plain expression, **NOT** a tuple. Always include a trailing comma for single-element tuples.

```python
# Correct single-element tuple
single_tup = (42,)
print(type(single_tup))  # Output: <class 'tuple'>

# Tuple packing without parentheses
another_tup = 42,
print(type(another_tup)) # Output: <class 'tuple'>

# INCORRECT (Evaluates to an integer)
not_a_tuple = (42)
print(type(not_a_tuple)) # Output: <class 'int'>
```

---

### Slicing Tuples
Tuples support the same indexing and slicing syntax as lists:

```python
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(tup[0])     # Output: 1
print(tup[2:5])   # Output: (3, 4, 5)
print(tup[-3:])   # Output: (7, 8, 9)
```

---

### Tuple Methods Reference
Because tuples are immutable, they only feature non-mutating search methods:

| Method | Description | Example (`tup = (1, 2, 2, 3)`) | Output |
| :--- | :--- | :--- | :--- |
| `.count(x)` | Returns total occurrences of `x` | `tup.count(2)` | `2` |
| `.index(x)` | Returns index of the first occurrence of `x` | `tup.index(3)` | `3` |

```python
my_tuple = (1, 2, 3, 2, 4, 2)
print("Count of 2:", my_tuple.count(2))  # Output: 3
print("Index of 3:", my_tuple.index(3))  # Output: 2
```

---

## ⚖️ 3. List vs Tuple: Quick Comparison

| Feature | List (`list`) | Tuple (`tuple`) |
| :--- | :--- | :--- |
| **Syntax** | Square brackets: `[1, 2, 3]` | Parentheses: `(1, 2, 3)` |
| **Mutability** | **Mutable** (Can be changed) | **Immutable** (Read-only) |
| **Methods** | Many (`append`, `pop`, `sort`, `remove`, etc.) | Minimal (`count`, `index`) |
| **Memory & Speed** | Higher memory, slightly slower | Lower memory, faster execution |
| **Dict Key Usability** | ❌ No (Unhashable type) | ✅ Yes (Hashable if items are immutable) |
| **Primary Use Case** | Dynamic collections of homogeneous data | Fixed records / heterogeneous data groups |

---

## 💻 4. Practice Problems & Solutions (WAP)

### Problem 1: Favorite Movies Collector
> **WAP to ask the user to enter 3 of their favorite movies, store them in a list, and display the result.**

```python
movies = []

mov1 = input("Enter 1st favorite movie: ")
mov2 = input("Enter 2nd favorite movie: ")
mov3 = input("Enter 3rd favorite movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print("Your favorite movies list:", movies)
```

---

### Problem 2: Palindrome List Checker
> **WAP to check if a given list is a Palindrome (e.g., `[1, "abc", "abc", 1]`).**

#### Approach 1: Using `.copy()` and `.reverse()`
```python
list_items = [1, "abc", "abc", 1]

# Make a shallow copy to prevent modifying the original list
copied_list = list_items.copy()
copied_list.reverse()

if list_items == copied_list:
    print("The list is a Palindrome! ✅")
else:
    print("The list is NOT a palindrome. ❌")
```

#### Approach 2: Using Slicing `[::-1]` (Pythonic)
```python
numbers = [1, "abc", "abc", 1]

if numbers == numbers[::-1]:
    print("The list is a Palindrome! ✅")
else:
    print("The list is NOT a palindrome. ❌")
```

---

### Problem 3: Count Grade Occurrences in Tuple
> **WAP to count the number of students who received an `"A"` grade in the following tuple:**  
> `("C", "D", "A", "A", "B", "B", "A")`

```python
grades = ("C", "D", "A", "A", "B", "B", "A")

count_a = grades.count("A")
print(f"Number of students with grade 'A': {count_a}") # Output: 3
```

---

### Problem 4: Convert Tuple to List & Sort
> **WAP to convert the tuple `("C", "D", "A", "A", "B", "B", "A")` into a list, sort it alphabetically from "A" to "D", and print the result.**

```python
grades = ("C", "D", "A", "A", "B", "B", "A")

# Convert tuple to list
grade_list = list(grades)

# Sort in-place
grade_list.sort()

print("Sorted grades:", grade_list)
# Output: ['A', 'A', 'A', 'B', 'B', 'C', 'D']
```

---

## 🚀 How to Run

1. Open your terminal in the workspace directory.
2. Run the chapter script:
   ```bash
   python chapter3_lists_tuples.py
   ```

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR- ADESH SRIVASTAVA(TANMAY)!

</div>
