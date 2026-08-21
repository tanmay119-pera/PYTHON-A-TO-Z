<div align="center">

# 📝 PROJECT 4: "INTERACTIVE TO-DO LIST" IN PYTHON

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A full-featured, interactive terminal-based task management application in Python: demonstrates CRUD operations, nested data structures (lists of dictionaries), cross-platform terminal UI clearing, 1-based indexing, defensive bounds checking, and optional JSON file persistence.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [✨ Key Features](#-key-features)
- [🧠 Core Concepts Applied](#-core-concepts-applied)
  - [1. Nested Data Modeling (List of Dicts)](#1-nested-data-modeling-list-of-dicts)
  - [2. Cross-Platform Terminal Clearing (`os.system`)](#2-cross-platform-terminal-clearing-ossystem)
  - [3. 1-Based User Indexing with `enumerate()`](#3-1-based-user-indexing-with-enumerate)
  - [4. Defensive Input & Bounds Validation](#4-defensive-input--bounds-validation)
- [🔄 Application Flowchart](#-application-flowchart)
- [💻 Code Implementations](#-code-implementations)
  - [Version 1: Standard In-Memory To-Do List](#version-1-standard-in-memory-to-do-list)
  - [Version 2: Persistent JSON Storage To-Do Application](#version-2-persistent-json-storage-to-do-application)
- [📊 CRUD Operations Breakdown](#-crud-operations-breakdown)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Project Overview

The **Interactive To-Do List** application is a classic software project implementing full **CRUD (Create, Read, Update, Delete)** operations.

It provides a clean, self-refreshing terminal interface where users can organize daily goals, toggle completion status with visual emoji indicators (`⏳` Pending vs `✅` Done), and safely remove completed or abandoned tasks.

---

## ✨ Key Features

- ➕ **Add Tasks**: Insert new tasks into the active task queue.
- 📋 **Visual Task Dashboard**: Displays formatted status indicators (`⏳` for Pending, `✅` for Completed) and strike-through text for finished items.
- ✔️ **Mark as Done**: Toggle task completion status in-place.
- ❌ **Delete Tasks**: Remove items safely with confirmation feedback.
- 🖥️ **Dynamic Screen Clearing**: Refreshes the terminal display after every action for an app-like feel.
- 🛡️ **Defensive Error Handling**: Catches invalid non-numeric inputs and out-of-range task numbers.

---

## 🧠 Core Concepts Applied

### 1. Nested Data Modeling (List of Dicts)

Each task is represented as a dictionary with `task` (name) and `completed` (boolean state) keys, stored inside a master list:

```python
todo_list = [
    {"task": "Buy groceries", "completed": False},
    {"task": "Finish Python project", "completed": True}
]
```

---

### 2. Cross-Platform Terminal Clearing (`os.system`)

The script dynamically detects the underlying operating system (`nt` for Windows, `posix` for macOS / Linux) to issue the correct screen clearing command:

```python
import os

def clear_screen():
    # 'cls' on Windows, 'clear' on macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')
```

---

### 3. 1-Based User Indexing with `enumerate()`

Users naturally count starting from `1`, while Python lists are `0`-indexed. Using `enumerate(..., start=1)` bridges this gap seamlessly:

```python
for index, item in enumerate(todo_list, start=1):
    status = "✅" if item['completed'] else "⏳"
    print(f"{index}. {status} {item['task']}")
```

When users select task number `N`, internal list access is mapped to `todo_list[N - 1]`.

---

### 4. Defensive Input & Bounds Validation

Prevents `IndexError` and `ValueError` when users provide invalid inputs:

```python
try:
    task_num = int(input("Enter task number: "))
    if 1 <= task_num <= len(todo_list):
        todo_list[task_num - 1]['completed'] = True
    else:
        print("⚠️ Task number out of range!")
except ValueError:
    print("❌ Invalid input! Please enter an integer.")
```

---

## 🔄 Application Flowchart

```
           ┌─────────────────────────────┐
           │        Start Program        │
           └──────────────┬──────────────┘
                          │
                          ▼
           ┌─────────────────────────────┐
           │  Clear Screen & Show Tasks  │ ◄──────────┐
           │   (List of tasks or Empty)  │            │
           └──────────────┬──────────────┘            │
                          │                           │
                          ▼                           │
           ┌─────────────────────────────┐            │
           │     Display Action Menu     │            │
           │ 1. Add   2. Done   3. Delete│            │
           │ 4. Exit                     │            │
           └──────────────┬──────────────┘            │
                          │                           │
                   Evaluate Choice                    │
        ┌─────────────┬───┴─────────┬────────────┐    │
        ▼ 1           ▼ 2           ▼ 3          ▼ 4  │
 ┌─────────────┐┌────────────┐┌────────────┐ ┌──────┐ │
 │ Input Task  ││ Validate & ││ Validate & │ │ Exit │ │
 │ Name & Add  ││ Mark Done  ││ Delete Item│ │ App  │ │
 └──────┬──────┘└─────┬──────┘└─────┬──────┘ └──────┘ │
        │             │             │                 │
        └─────────────┴─────────────┴─────────────────┘
```

---

## 💻 Code Implementations

### Version 1: Standard In-Memory To-Do List

```python
"""
Python Mini-Project 4: Interactive To-Do List
"""

import os

todo_list = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_tasks():
    clear_screen()
    print("=" * 40)
    print("       📝 MY AWESOME TO-DO LIST")
    print("=" * 40)

    if not todo_list:
        print("  📭 Your list is completely empty!")
        print("  Time to chill, or add a new task.")
    else:
        for index, item in enumerate(todo_list, start=1):
            status_icon = "✅" if item['completed'] else "⏳"
            task_name = item['task']
            if item['completed']:
                task_name = f"~{task_name}~ (Done)"

            print(f"  {index}. {status_icon}  {task_name}")
    print("=" * 40)

def main():
    while True:
        show_tasks()

        print("\nWhat would you like to do?")
        print("1. ➕ Add a Task")
        print("2. ✔️  Mark Task as Done")
        print("3. ❌ Delete a Task")
        print("4. 🚪 Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            new_task = input("\n✏️  Enter the new task: ").strip()
            if new_task:
                todo_list.append({"task": new_task, "completed": False})

        elif choice == '2':
            if not todo_list:
                input("\n📭 List is empty! Press Enter to continue...")
                continue
            try:
                task_num = int(input("\n✔️  Enter task number to mark as done: "))
                if 1 <= task_num <= len(todo_list):
                    todo_list[task_num - 1]['completed'] = True
                else:
                    input("⚠️ Invalid number! Press Enter to try again...")
            except ValueError:
                input("❌ Please enter a valid number! Press Enter to try again...")

        elif choice == '3':
            if not todo_list:
                input("\n📭 List is empty! Press Enter to continue...")
                continue
            try:
                task_num = int(input("\n❌ Enter task number to delete: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    input(f"🗑️ Deleted '{removed['task']}'. Press Enter to continue...")
                else:
                    input("⚠️ Invalid number! Press Enter to try again...")
            except ValueError:
                input("❌ Please enter a valid number! Press Enter to try again...")

        elif choice == '4':
            print("\n👋 Goodbye! Have a productive and soulful day!")
            break

        else:
            input("⚠️ Invalid choice! Press Enter to try again...")

if __name__ == "__main__":
    main()
```

---

### Version 2: Persistent JSON Storage To-Do Application

To keep tasks saved even after closing the terminal, we can serialize the task list to a `tasks.json` file using Python's `json` module:

```python
"""
Persistent To-Do List with JSON File Storage
"""

import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)
```

---

## 📊 CRUD Operations Breakdown

| Operation | Action | Implementation Method | Code Example |
| :--- | :--- | :--- | :--- |
| **Create** | Add Task | `list.append()` | `todo_list.append({"task": "Learn Python", "completed": False})` |
| **Read** | View Dashboard | `for i, item in enumerate()` | `print(f"{i}. {item['task']}")` |
| **Update** | Mark Completed | Direct dict mutation | `todo_list[idx]['completed'] = True` |
| **Delete** | Remove Task | `list.pop()` | `removed = todo_list.pop(idx)` |

---

## 🚀 How to Run

1. **Verify Python Installation**:
   ```bash
   python3 --version
   ```
2. **Execute To-Do List Application**:
   ```bash
   python3 project4_todo_list.py
   ```

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA(TANMAY)!

</div>