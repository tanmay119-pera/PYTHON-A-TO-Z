<div align="center">

# 📖 PYTHON DICTIONARIES & SETS — CHAPTER 4

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A comprehensive masterclass on Python's associative and unique collection types: Dictionaries (key-value mappings) and Sets (unique mathematical collections), complete with built-in methods, set theory operations, and practice problems (WAP).</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [📖 1. Python Dictionaries](#-1-python-dictionaries)
  - [Key Characteristics](#key-characteristics)
  - [Creating & Accessing Elements](#creating--accessing-elements)
  - [Modifying, Adding & Removing Items](#modifying-adding--removing-items)
  - [Nested Dictionaries](#nested-dictionaries)
  - [Dictionary Methods Reference](#dictionary-methods-reference)
- [🎯 2. Python Sets](#-2-python-sets)
  - [Key Characteristics](#key-characteristics-1)
  - [Empty Set vs Empty Dictionary](#empty-set-vs-empty-dictionary)
  - [Set Methods Reference](#set-methods-reference)
  - [Mathematical Set Operations (Union, Intersection, Difference)](#mathematical-set-operations)
- [⚖️ 3. Dictionary vs Set: Quick Comparison](#️-3-dictionary-vs-set-quick-comparison)
- [💻 4. Practice Problems & Solutions (WAP)](#-4-practice-problems--solutions-wap)
  - [Problem 1: Word Meaning Dictionary](#problem-1-word-meaning-dictionary)
  - [Problem 2: Unique Classrooms for Subjects](#problem-2-unique-classrooms-for-subjects)
  - [Problem 3: User Subject Marks Entry (2 Methods)](#problem-3-user-subject-marks-entry-2-methods)
  - [Problem 4: Storing 9 and 9.0 Separately in a Set](#problem-4-storing-9-and-90-separately-in-a-set)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Overview

Python provides two powerful hash-table based data structures:
- **Dictionary (`dict`)**: Stores data in labeled `key: value` pairs with $O(1)$ lookup time.
- **Set (`set`)**: Stores an unordered collection of unique, immutable elements and supports fast membership testing and mathematical set operations.

---

## 📖 1. Python Dictionaries

### Key Characteristics
1. **Key-Value Pairs**: Data is stored as `{key: value}` mappings.
2. **Ordered & Mutable**: Insertion order is preserved (Python 3.7+), and values can be modified in-place.
3. **Unique & Immutable Keys**: Keys must be immutable (strings, numbers, or tuples with immutable items) and cannot be duplicated.
4. **Any Data Type as Values**: Values can be integers, floats, lists, tuples, or even nested dictionaries.

---

### Creating & Accessing Elements

```python
# Creating a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Accessing items
print(car["brand"])         # Output: Ford
print(car.get("model"))     # Output: Mustang (Safe lookup, returns None if not found)
```

---

### Modifying, Adding & Removing Items

```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# 1. Modifying existing value
car["year"] = 2024

# 2. Adding a new key-value pair
car["color"] = "Red"

# 3. Removing an item using 'del'
del car["model"]

# 4. Removing using '.pop()' (returns removed value)
removed_color = car.pop("color")

print(car)  # Output: {'brand': 'Ford', 'year': 2024}
```

---

### Nested Dictionaries
Dictionaries can contain other dictionaries to model complex hierarchical data:

```python
student = {
    "name": "Anushka",
    "subjects": {
        "maths": 98,
        "science": 95,
        "english": 92,
        "history": 90
    }
}

# Accessing nested values
print(student["name"])                    # Output: Anushka
print(student["subjects"]["maths"])       # Output: 98
```

---

### Dictionary Methods Reference

| Method | Description | Example (`d = {"a": 1, "b": 2}`) | Result |
| :--- | :--- | :--- | :--- |
| `.keys()` | Returns a view of all keys | `d.keys()` | `dict_keys(['a', 'b'])` |
| `.values()` | Returns a view of all values | `d.values()` | `dict_values([1, 2])` |
| `.items()` | Returns a view of `(key, value)` tuples | `d.items()` | `dict_items([('a', 1), ('b', 2)])` |
| `.get(key, default)` | Returns value for `key` safely without throwing `KeyError` | `d.get("c", 0)` | `0` |
| `.update(dict2)` | Inserts or updates key-value pairs from another dictionary | `d.update({"c": 3})` | `{'a': 1, 'b': 2, 'c': 3}` |
| `.pop(key)` | Removes `key` and returns its value | `d.pop("a")` | Returns `1` |
| `.clear()` | Empties the entire dictionary | `d.clear()` | `{}` |

---

## 🎯 2. Python Sets

### Key Characteristics
1. **Unordered & Unindexed**: Elements do not have a fixed position, so indexing `set[0]` is **not allowed**.
2. **Unique Elements**: Duplicate items are automatically filtered out.
3. **Mutable Set, Immutable Elements**: The set can grow or shrink, but elements stored within it must be immutable and hashable (`int`, `float`, `str`, `tuple`).

---

### Empty Set vs Empty Dictionary
> [!WARNING]
> Using `{}` creates an empty **Dictionary**, not a set. To initialize an empty set, you **must** use `set()`.

```python
# Empty dictionary
dict_var = {}
print(type(dict_var))  # Output: <class 'dict'>

# Empty set
set_var = set()
print(type(set_var))   # Output: <class 'set'>
```

---

### Set Methods Reference

| Method | Description | Example (`s = {1, 2, 3}`) | Result |
| :--- | :--- | :--- | :--- |
| `.add(elem)` | Adds an element to the set | `s.add(4)` | `{1, 2, 3, 4}` |
| `.remove(elem)` | Removes element (raises `KeyError` if not found) | `s.remove(2)` | `{1, 3}` |
| `.discard(elem)` | Removes element safely (no error if absent) | `s.discard(99)` | `{1, 2, 3}` |
| `.pop()` | Removes and returns an arbitrary element | `s.pop()` | Returns popped item |
| `.clear()` | Removes all elements from the set | `s.clear()` | `set()` |

---

### Mathematical Set Operations

Python provides mathematical operations for set relationships:

```python
setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
```

```text
       Set A               Set B
   ┌───────────┐       ┌───────────┐
   │   a   b   │   c   │   d   e   │
   └───────────┴───────┴───────────┘
```

#### 1. Union (`|` or `.union()`)
Combines all distinct elements from both sets:
```python
print(setA.union(setB))  # {'a', 'b', 'c', 'd', 'e'}
print(setA | setB)        # {'a', 'b', 'c', 'd', 'e'}
```

#### 2. Intersection (`&` or `.intersection()`)
Extracts common elements present in both sets:
```python
print(setA.intersection(setB))  # {'c'}
print(setA & setB)              # {'c'}
```

#### 3. Difference (`-` or `.difference()`)
Returns elements in `setA` that are not in `setB`:
```python
print(setA.difference(setB))    # {'a', 'b'}
print(setA - setB)              # {'a', 'b'}
```

#### 4. Symmetric Difference (`^` or `.symmetric_difference()`)
Returns elements in either set, but not in both:
```python
print(setA ^ setB)              # {'a', 'b', 'd', 'e'}
```

---

## ⚖️ 3. Dictionary vs Set: Quick Comparison

| Feature | Dictionary (`dict`) | Set (`set`) |
| :--- | :--- | :--- |
| **Structure** | Key-Value mappings `{k: v}` | Unique element collection `{v1, v2}` |
| **Indexing** | By key: `d["key"]` | ❌ No indexing or slicing allowed |
| **Duplicates** | Keys: No / Values: Yes | ❌ No duplicates allowed |
| **Empty Init** | `{}` | `set()` |
| **Internal Hashing** | Keys are hashed for fast lookup | All elements are hashed |
| **Primary Use** | Associated data, records, lookups | Deduplication, membership tests, set math |

---

## 💻 4. Practice Problems & Solutions (WAP)

### Problem 1: Word Meaning Dictionary
> **Store the following word meanings in a Python dictionary:**
> - `table`: `"a piece of furniture"`, `"list of facts and figures"`
> - `cat`: `"a small animal"`

```python
word_dict = {
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat": ["a small animal"]
}

print("Dictionary contents:")
for word, meanings in word_dict.items():
    print(f"• {word}: {meanings}")
```

---

### Problem 2: Unique Classrooms for Subjects
> **You are given a list of subjects for students. Assume 1 classroom is required for each unique subject. Find out how many classrooms are needed.**  
> `subjects = ["python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "C"]`

```python
subjects = [
    "python", "java", "c++", "python", 
    "javascript", "java", "python", "java", "c++", "C"
]

# Eliminate duplicate subjects using set()
unique_subjects = set(subjects)
required_classrooms = len(unique_subjects)

print(f"Unique Subjects: {unique_subjects}")
print(f"Total Classrooms Required: {required_classrooms}") # Output: 5
```

---

### Problem 3: User Subject Marks Entry (2 Methods)
> **WAP to enter marks of 3 subjects from the user and store them in an empty dictionary with subject names as keys and marks as values.**

#### Method 1: Using `.update()`
```python
marks_dict = {}

phy = int(input("Enter marks for Physics: "))
marks_dict.update({"Physics": phy})

chem = int(input("Enter marks for Chemistry: "))
marks_dict.update({"Chemistry": chem})

math = int(input("Enter marks for Mathematics: "))
marks_dict.update({"Mathematics": math})

print("Marks Dictionary:", marks_dict)
```

#### Method 2: Direct Key-Assignment (Clean & Pythonic)
```python
marks_dict = {}

marks_dict["Math"] = int(input("Enter marks for Math: "))
marks_dict["Science"] = int(input("Enter marks for Science: "))
marks_dict["English"] = int(input("Enter marks for English: "))

print("Marks Dictionary:", marks_dict)
```

---

### Problem 4: Storing 9 and 9.0 Separately in a Set
> **Figure out a way to store `9` and `9.0` as separate values in a set.**

> [!NOTE]
> In Python, `9 == 9.0` evaluates to `True` and `hash(9) == hash(9.0)`. Therefore, `{9, 9.0}` automatically collapses to `{9}` because sets eliminate duplicates based on value equality and hash.

#### Solutions to Store Both Values:

```python
# Approach 1: Store as String and Float
set_sol1 = {"9", 9.0}
print("Approach 1 (Str + Float):", set_sol1)  # Output: {'9', 9.0}

# Approach 2: Store with type tags as Tuples
set_sol2 = {("int", 9), ("float", 9.0)}
print("Approach 2 (Typed Tuples):", set_sol2) # Output: {('int', 9), ('float', 9.0)}

# Approach 3: Store with built-in type object pairing
set_sol3 = {(9, int), (9.0, float)}
print("Approach 3 (Value, Type):", set_sol3)  # Output: {(9, <class 'int'>), (9.0, <class 'float'>)}
```

---

## 🚀 How to Run

1. Open your terminal in the workspace directory.
2. Run the chapter script:
   ```bash
   python chapter4_dict_sets.py
   ```

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA!

</div>
