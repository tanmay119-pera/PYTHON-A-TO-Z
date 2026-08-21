<div align="center">

# 📁 PYTHON FILE INPUT/OUTPUT (I/O) — CHAPTER 8

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A comprehensive masterclass on Python File Handling: reading, writing, appending, binary vs text files, access modes, cursor positioning with <code>seek()</code> & <code>tell()</code>, the <code>with</code> context manager, the <code>os</code> module, and practical data-parsing algorithms.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [🔄 1. The Three Essential Steps of File I/O](#-1-the-three-essential-steps-of-file-io)
- [📄 2. Types of Files](#-2-types-of-files)
  - [Text Files](#text-files)
  - [Binary Files](#binary-files)
- [🔑 3. Complete File Modes Reference](#-3-complete-file-modes-reference)
  - [Text Access Modes Table](#text-access-modes-table)
  - [Binary Access Modes Table](#binary-access-modes-table)
- [📖 4. Reading from Files](#-4-reading-from-files)
  - [`read()` & `read(n)`](#read--readn)
  - [`readline()`](#readline)
  - [`readlines()`](#readlines)
  - [Memory-Efficient Line Iteration](#memory-efficient-line-iteration)
- [✍️ 5. Writing and Appending](#️-5-writing-and-appending)
  - [Write Mode (`'w'`) vs Append Mode (`'a'`)](#write-mode-w-vs-append-mode-a)
  - [`write()` & `writelines()`](#write--writelines)
- [🛡️ 6. The `with` Statement (Context Manager)](#️-6-the-with-statement-context-manager)
- [🧭 7. Cursor Navigation: `tell()` & `seek()`](#-7-cursor-navigation-tell--seek)
- [🗑️ 8. File & OS Operations (`os` module)](#️-8-file--os-operations-os-module)
  - [Deleting Files (`os.remove`)](#deleting-files-osremove)
  - [Checking Existence (`os.path.exists`)](#checking-existence-ospathexists)
  - [Renaming Files (`os.rename`)](#renaming-files-osrename)
- [💻 9. Practice Problems & Solutions (WAF / WAP)](#-9-practice-problems--solutions-waf--wap)
  - [Problem 1: Create and Populate `practice.txt`](#problem-1-create-and-populate-practicetxt)
  - [Problem 2: Search & Replace Text in File](#problem-2-search--replace-text-in-file)
  - [Problem 3: Check If Word Exists in File](#problem-3-check-if-word-exists-in-file)
  - [Problem 4: Find First Line Occurrence of Word](#problem-4-find-first-line-occurrence-of-word)
  - [Problem 5: Count Even Numbers in a Comma-Separated File](#problem-5-count-even-numbers-in-a-comma-separated-file)
- [💡 10. File Handling Best Practices](#-10-file-handling-best-practices)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Overview

Programs execute in volatile Random Access Memory (RAM), meaning data is lost once the program terminates. **File I/O (Input/Output)** enables Python to persist data permanently on disk (SSD/HDD) by reading from and writing to files.

```
┌─────────────────────────────────────────────────────────────┐
│                    File I/O Workflow                        │
├─────────────────────────────────────────────────────────────┤
│   1. OPEN               2. PROCESS             3. CLOSE     │
│   f = open(...)  ───>   read() / write() ───>  f.close()    │
│                                                             │
│   ⭐ PREFERRED: with open(...) as f: (Auto Closes)          │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 1. The Three Essential Steps of File I/O

1. **Open**: Establish a connection/stream between the Python script and the physical file using `open(filename, mode)`.
2. **Process**: Read data from the file into memory or write/append data from memory onto the disk.
3. **Close**: Disconnect from the file using `.close()` to flush unwritten buffers and release system resources.

```python
# Manual Open & Close pattern
f = open("demo.txt", "r")  # 1. Open
data = f.read()            # 2. Process
print(data)
f.close()                  # 3. Close (CRITICAL)
```

---

## 📄 2. Types of Files

### Text Files
- Structured as human-readable characters, strings, and lines.
- Stored using character encodings such as `UTF-8` or `ASCII`.
- Examples: `.txt`, `.csv`, `.log`, `.json`, `.py`, `.md`.

### Binary Files
- Stored as raw bytes (`0s` and `1s`) without character encoding.
- Handled using `bytes` objects (prefixed with `b""`).
- Examples: Images (`.png`, `.jpg`), Audio/Video (`.mp3`, `.mp4`), PDFs, compiled binaries.

---

## 🔑 3. Complete File Modes Reference

### Text Access Modes Table

| Mode | Name | File Must Exist? | Truncates/Overwrites? | Cursor Pointer | Can Read? | Can Write? |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `'r'` | **Read (Default)** | ✅ Yes | ❌ No | Beginning | ✅ Yes | ❌ No |
| `'w'` | **Write** | ❌ Creates new | ⚠️ **Yes (Erases file)** | Beginning | ❌ No | ✅ Yes |
| `'a'` | **Append** | ❌ Creates new | ❌ No | End of file | ❌ No | ✅ Yes |
| `'x'` | **Exclusive Create** | ❌ Fails if exists | ❌ No | Beginning | ❌ No | ✅ Yes |
| `'r+'` | **Read + Write** | ✅ Yes | ❌ No | Beginning | ✅ Yes | ✅ Yes |
| `'w+'` | **Write + Read** | ❌ Creates new | ⚠️ **Yes (Erases file)** | Beginning | ✅ Yes | ✅ Yes |
| `'a+'` | **Append + Read** | ❌ Creates new | ❌ No | End of file | ✅ Yes | ✅ Yes |

---

### Binary Access Modes Table

Append `'b'` to any mode to work with raw bytes:

```python
# Reading binary data (e.g. image or audio)
with open("logo.png", "rb") as file:
    binary_data = file.read()
    print("Read", len(binary_data), "bytes")

# Writing binary bytes
with open("output.bin", "wb") as file:
    file.write(b"\x89PNG\r\n\x1a\n\x00\x00")
```

| Binary Mode | Description |
| :---: | :--- |
| `'rb'` | Read binary file (file must exist). |
| `'wb'` | Write binary file (overwrites or creates new). |
| `'ab'` | Append bytes to end of binary file. |
| `'rb+'` | Read and write binary without truncating. |
| `'wb+'` | Read and write binary (truncates existing). |
| `'ab+'` | Read and append binary data. |

---

## 📖 4. Reading from Files

Assume `demo.txt` contains:
```text
Hello Python!
File handling is easy.
Learning line by line.
```

### `read()` & `read(n)`
- `f.read()`: Reads the entire file content as a single string.
- `f.read(n)`: Reads at most `n` characters (or bytes in binary mode).

```python
with open("demo.txt", "r") as f:
    first_five = f.read(5)   # Reads first 5 chars: 'Hello'
    remaining = f.read()     # Reads the rest of the file
    print("First 5:", first_five)
```

---

### `readline()`
Reads a single line up to the newline character `\n`. Subsequent calls read consecutive lines:

```python
with open("demo.txt", "r") as f:
    line1 = f.readline()  # 'Hello Python!\n'
    line2 = f.readline()  # 'File handling is easy.\n'
    print("Line 1:", line1.strip())
    print("Line 2:", line2.strip())
```

---

### `readlines()`
Reads all lines into a list of strings:

```python
with open("demo.txt", "r") as f:
    all_lines = f.readlines()
    print(all_lines)
    # Output: ['Hello Python!\n', 'File handling is easy.\n', 'Learning line by line.']
```

---

### Memory-Efficient Line Iteration

For large files (gigabytes in size), avoid loading everything into memory. Instead, iterate over the file object directly:

```python
with open("large_log.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        if "ERROR" in line:
            print(f"Error on line {line_number}: {line.strip()}")
```

---

## ✍️ 5. Writing and Appending

### Write Mode (`'w'`) vs Append Mode (`'a'`)

```python
# 1. WRITE MODE ('w') — Overwrites/Truncates existing content!
with open("sample.txt", "w") as f:
    f.write("Line 1: Overwriting previous contents.\n")

# 2. APPEND MODE ('a') — Adds new text to the end
with open("sample.txt", "a") as f:
    f.write("Line 2: Appending this new line at the end.\n")
```

### `write()` & `writelines()`

```python
lines_to_write = [
    "Apple\n",
    "Banana\n",
    "Cherry\n"
]

with open("fruits.txt", "w") as f:
    f.writelines(lines_to_write)
```

> [!NOTE]
> `write()` does not automatically append a newline `\n`. You must explicitly include `\n` if you want subsequent text on a new line.

---

## 🛡️ 6. The `with` Statement (Context Manager)

The `with` statement utilizes Python's **Context Management Protocol** (`__enter__` and `__exit__`).

```python
with open("data.txt", "r") as f:
    content = f.read()
    # File is automatically closed when this indented block finishes!

# f.closed evaluates to True here
print("Is file closed?", f.closed)  # True
```

### Why Always Use `with`?
1. **Guaranteed Cleanup**: The file is automatically closed, even if an uncaught exception or crash occurs inside the block.
2. **Prevents Resource Leaks**: Prevents OS file descriptor exhaustion.
3. **Cleaner Syntax**: Eliminates redundant `f.close()` statements.

---

## 🧭 7. Cursor Navigation: `tell()` & `seek()`

Every open file maintains an internal **file pointer (cursor)** indicating the current byte position.

- `f.tell()`: Returns the cursor's current position (integer offset in bytes).
- `f.seek(offset)`: Repositions the cursor to a specific byte index.

```python
with open("demo.txt", "w+") as f:
    f.write("Python Programming")
    print("Cursor after write:", f.tell())  # 18 bytes
    
    # Reposition pointer to the beginning to read what was written
    f.seek(0)
    print("Cursor after seek(0):", f.tell()) # 0 bytes
    
    content = f.read()
    print("Read content:", content)         # 'Python Programming'
```

---

## 🗑️ 8. File & OS Operations (`os` module)

Python's standard library `os` module handles filesystem-level tasks:

```python
import os

filename = "temp_file.txt"

# 1. Check if a file exists
if os.path.exists(filename):
    print("File exists!")
    
    # 2. Rename a file
    os.rename(filename, "renamed_file.txt")
    print("File renamed.")
    
    # 3. Delete a file
    os.remove("renamed_file.txt")
    print("File deleted.")
else:
    print("File does not exist.")
```

---

## 💻 9. Practice Problems & Solutions (WAF / WAP)

---

### Problem 1: Create and Populate `practice.txt`

**Task**: Create a file named `practice.txt` using Python and insert the following text:
```text
hi everyone
we are learning file I/O
using java.
i like programming in java.
```

#### Solution:
```python
def create_practice_file():
    with open("practice.txt", "w") as f:
        f.write("hi everyone\n")
        f.write("we are learning file I/O\n")
        f.write("using java.\n")
        f.write("i like programming in java.\n")
    print("practice.txt created successfully.")

create_practice_file()
```

---

### Problem 2: Search & Replace Text in File

**Task**: Write a function that replaces all occurrences of `"java"` with `"python"` in `practice.txt`.

#### Solution:
```python
def replace_word(filename="practice.txt", old_word="java", new_word="python"):
    # Step 1: Read entire content
    with open(filename, "r") as f:
        data = f.read()
    
    # Step 2: Perform string replacement
    updated_data = data.replace(old_word, new_word)
    
    # Step 3: Overwrite file with updated content
    with open(filename, "w") as f:
        f.write(updated_data)
    
    print(f"Replaced all '{old_word}' with '{new_word}'.")

replace_word()
```

---

### Problem 3: Check If Word Exists in File

**Task**: Write a function `check_for_word(word)` to verify whether a specific word exists in `practice.txt`.

#### Solution:
```python
def check_for_word(word, filename="practice.txt"):
    with open(filename, "r") as f:
        data = f.read()
        if word in data:
            print(f"Word '{word}' FOUND in {filename}.")
            return True
        else:
            print(f"Word '{word}' NOT found in {filename}.")
            return False

check_for_word("learning")
check_for_word("c++")
```

---

### Problem 4: Find First Line Occurrence of Word

**Task**: Write a function `check_for_line(word)` to identify the exact line number where `word` first occurs. Return `-1` if not found.

#### Solution:
```python
def check_for_line(word, filename="practice.txt"):
    with open(filename, "r") as f:
        for line_no, line in enumerate(f, start=1):
            if word in line:
                print(f"Word '{word}' first found at Line: {line_no}")
                return line_no
                
    print(f"Word '{word}' not found in any line.")
    return -1

line_result = check_for_line("learning")
print("Returned line index:", line_result)
```

---

### Problem 5: Count Even Numbers in a Comma-Separated File

**Task**: Create a file `numbers.txt` containing comma-separated numbers (e.g., `1, 2, 45, 84, 92, 105, 120`). Write a program to parse the numbers and count how many are **EVEN**.

#### Solution:
```python
# 1. Create sample numbers file
with open("numbers.txt", "w") as f:
    f.write("1, 2, 45, 84, 92, 105, 120, 14, 23, 60")

# 2. Function to count even numbers
def count_even_numbers(filename="numbers.txt"):
    with open(filename, "r") as f:
        data = f.read()
    
    # Split by comma and clean whitespace
    raw_numbers = data.split(",")
    even_count = 0
    even_numbers = []
    
    for item in raw_numbers:
        clean_item = item.strip()
        if clean_item:  # Avoid empty strings
            num = int(clean_item)
            if num % 2 == 0:
                even_count += 1
                even_numbers.append(num)
                
    print(f"Found {even_count} even numbers: {even_numbers}")
    return even_count

count_even_numbers()
# Output: Found 6 even numbers: [2, 84, 92, 120, 14, 60]
```

---

## 💡 10. File Handling Best Practices

1. **Always Use `with open(...)`**: Avoid manual `f.close()` calls to guarantee error-safe cleanup.
2. **Choose Correct Modes**: Use `'r'` for inspection, `'a'` for appending logs, and `'w'` only when an intentional reset/overwrite is required.
3. **Handle Missing Files Gracefully**: Use `try...except FileNotFoundError` when accessing external files.
4. **Specify Encodings Explicitly**: In multi-platform environments, write `open("data.txt", "r", encoding="utf-8")`.
5. **Stream Large Files**: Iterate line-by-line (`for line in f:`) rather than calling `.read()` on multi-gigabyte datasets.

---

## 🚀 How to Run

1. **Verify Python Installation**:
   ```bash
   python3 --version
   ```
2. **Execute File I/O Script**:
   ```bash
   python3 chapter8_file_io.py
   ```

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!
---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA(TANMAY)!

</div>