<div align="center">

# 🏛️ OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON — CHAPTER 9

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A comprehensive masterclass on Object-Oriented Programming in Python: Classes & Objects, <code>__init__</code> constructor, <code>self</code> reference, Class vs Instance attributes, the 4 Pillars of OOP (Encapsulation, Abstraction, Inheritance, Polymorphism), <code>@classmethod</code>, <code>@staticmethod</code>, Dunder methods, and Operator Overloading.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview & Evolution of Paradigms](#-overview--evolution-of-paradigms)
- [⚡ Quick Concept Reference (15 Core Concepts)](#-quick-concept-reference-15-core-concepts)
- [🏗️ 1. Classes, Objects & The `__init__` Constructor](#️-1-classes-objects--the-__init__-constructor)
  - [Class Blueprint vs Object Instance](#class-blueprint-vs-object-instance)
  - [The `__init__()` Constructor](#the-__init__-constructor)
  - [Understanding the `self` Parameter](#understanding-the-self-parameter)
- [🏷️ 2. Attributes & Methods](#️-2-attributes--methods)
  - [Class Attributes vs Instance Attributes](#class-attributes-vs-instance-attributes)
  - [Instance Methods](#instance-methods)
  - [Static Methods (`@staticmethod`)](#static-methods-staticmethod)
  - [Class Methods (`@classmethod`)](#class-methods-classmethod)
- [🏛️ 3. The 4 Pillars of OOP](#️-3-the-4-pillars-of-oop)
  - [1. Abstraction (Hiding Complexity)](#1-abstraction-hiding-complexity)
  - [2. Encapsulation (Data Protection & Private Members)](#2-encapsulation-data-protection--private-members)
  - [3. Inheritance & `super()` (Code Reusability)](#3-inheritance--super-code-reusability)
  - [4. Polymorphism & Method Overriding](#4-polymorphism--method-overriding)
- [🪄 4. Magic / Dunder Methods & Operator Overloading](#-4-magic--dunder-methods--operator-overloading)
  - [Common Dunder Methods (`__str__`, `__repr__`, `__len__`)](#common-dunder-methods)
  - [Operator Overloading (`__add__`, `__sub__`, `__gt__`)](#operator-overloading)
- [💻 5. Practice Problems & Solutions (WAP)](#-5-practice-problems--solutions-wap)
  - [Problem 1: Student Class with Average Marks Calculation](#problem-1-student-class-with-average-marks-calculation)
  - [Problem 2: Bank Account with Debit, Credit & Balance](#problem-2-bank-account-with-debit-credit--balance)
  - [Problem 3: Multi-level Inheritance & Employee Hierarchy](#problem-3-multi-level-inheritance--employee-hierarchy)
  - [Problem 4: 2D Vector Addition with Operator Overloading](#problem-4-2d-vector-addition-with-operator-overloading)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Overview & Evolution of Paradigms

```
┌───────────────────────────┐     ┌───────────────────────────┐     ┌───────────────────────────┐
│   Procedural Paradigm     │ ──> │   Functional Paradigm     │ ──> │  Object-Oriented (OOP)    │
│  (Step-by-step commands)  │     │ (Pure functions, no state)│     │(Objects: State + Behavior)│
└───────────────────────────┘     └───────────────────────────┘     └───────────────────────────┘
```

In **Object-Oriented Programming (OOP)**, code is organized around real-world entities called **objects**, which bundle:
1. **Attributes / State**: Data variables representing what an object *has*.
2. **Methods / Behavior**: Functions representing what an object *does*.

---

## ⚡ Quick Concept Reference (15 Core Concepts)

| # | Concept | Simple Meaning |
| :---: | :--- | :--- |
| **1** | **Class & Object** | Blueprint template & concrete instance created from it |
| **2** | **`__init__`** | Constructor method executed automatically upon object instantiation |
| **3** | **`self`** | Explicit pointer/reference to the current object instance |
| **4** | **Encapsulation** | Bundling data + methods together and restricting direct outside access |
| **5** | **Inheritance** | Derived child class acquiring attributes & methods of parent class |
| **6** | **Multiple Inheritance** | A single child class inheriting from multiple parent classes |
| **7** | **Polymorphism** | Same interface / method name exhibiting different behaviors |
| **8** | **Method Overriding** | Child class providing its own specialized implementation of a parent method |
| **9** | **Abstraction** | Exposing essential interfaces while concealing internal implementation details |
| **10** | **`super()`** | Built-in proxy to invoke parent class methods and constructor |
| **11** | **Class vs Instance Var** | Variable shared across all objects vs unique to each object |
| **12** | **`@classmethod`** | Method bound to the class (`cls`) rather than instances (`self`) |
| **13** | **`@staticmethod`** | Independent utility method inside class without `self` or `cls` access |
| **14** | **Dunder Methods** | Double-underscore methods (`__str__`, `__len__`) defining built-in behaviors |
| **15** | **Operator Overloading** | Customizing mathematical/logical operators (`+`, `-`, `==`) via dunders |

---

## 🏗️ 1. Classes, Objects & The `__init__` Constructor

### Class Blueprint vs Object Instance

```python
# 1. CLASS DEFINITION (Blueprint)
class Car:
    color = "Blue"
    brand = "BMW"

# 2. OBJECT CREATION (Instance)
car1 = Car()
print(car1.color)  # Output: Blue
print(car1.brand)  # Output: BMW
```

---

### The `__init__()` Constructor

The `__init__()` method is Python's constructor. It initializes attributes when a new object is created:

```python
class Student:
    def __init__(self, fullname, marks):
        self.name = fullname  # Instance attribute
        self.marks = marks    # Instance attribute
        print(f"Enrolled student: {self.name}")

s1 = Student("Karan", 88)
s2 = Student("Anushka", 97)

print(s1.name, "->", s1.marks)  # Output: Karan -> 88
print(s2.name, "->", s2.marks)  # Output: Anushka -> 97
```

---

### Understanding the `self` Parameter

- `self` is passed implicitly by Python as the first argument when invoking instance methods.
- Writing `s1.get_marks()` is internally translated to `Student.get_marks(s1)`.
- It distinguishes between variables belonging to the specific object instance and local function variables.

---

## 🏷️ 2. Attributes & Methods

### Class Attributes vs Instance Attributes

```python
class Student:
    college_name = "ABC College"  # Class attribute (Shared by ALL students)

    def __init__(self, name, marks):
        self.name = name          # Instance attribute (Unique to this student)
        self.marks = marks

s1 = Student("Karan", 97)
s2 = Student("Rahul", 85)

print(s1.college_name)  # ABC College
print(s2.college_name)  # ABC College
```

> [!NOTE]
> **Precedence Rule**: If an instance attribute and a class attribute share the same name, the **instance attribute takes precedence** when accessed on the object (`obj.attr`).

---

### Instance Methods

Regular methods within a class that accept `self` to read or modify instance attributes:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print(f"Welcome student, {self.name}!")

    def get_marks(self):
        return self.marks

s1 = Student("Karan", 97)
s1.welcome()
print("Marks:", s1.get_marks())
```

---

### Static Methods (`@staticmethod`)

Static methods perform independent operations without reading or modifying instance state (`self`) or class state (`cls`):

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print("Sum:", MathUtils.add(10, 20))  # Output: 30
```

---

### Class Methods (`@classmethod`)

Class methods receive the class (`cls`) as their first parameter, enabling them to modify class-level state:

```python
class Person:
    species = "Homo Sapiens"

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

print(Person.species)        # Homo Sapiens
Person.change_species("Humanoid")
print(Person.species)        # Humanoid
```

---

## 🏛️ 3. The 4 Pillars of OOP

```
                   ┌─────────────────────────────────────────┐
                   │            4 Pillars of OOP             │
                   └────────────────────┬────────────────────┘
          ┌─────────────────┬───────────┴───────────┬─────────────────┐
          ▼                 ▼                       ▼                 ▼
   1. ABSTRACTION    2. ENCAPSULATION        3. INHERITANCE    4. POLYMORPHISM
 (Hide complexity)  (Protect inner data)   (Reusing features) (Multiple forms)
```

---

### 1. Abstraction (Hiding Complexity)

Abstraction conceals the internal complexity of a mechanism and exposes only an intuitive interface.

```python
class Car:
    def __init__(self):
        self.clutch = False
        self.acc = False

    def start(self):
        # Internal operations hidden from the user
        self.clutch = True
        self.acc = True
        print("Car started successfully... 🚗")

my_car = Car()
my_car.start()  # Driver only interacts with .start()
```

---

### 2. Encapsulation (Data Protection & Private Members)

Encapsulation packages attributes and methods into a capsule and shields critical state with **private attributes** (prefixed with double underscores `__`):

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (Name Mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance  # Controlled getter

acc = BankAccount("Tony", 50000)
acc.deposit(15000)
print("Balance:", acc.get_balance())
# print(acc.__balance)  # ❌ AttributeError: 'BankAccount' object has no attribute '__balance'
```

---

### 3. Inheritance & `super()` (Code Reusability)

Inheritance enables a derived child class to inherit attributes and methods from a base parent class.

#### Single & Multi-Level Inheritance:
```python
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating food.")

# Child Class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Invoke Parent constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof! 🐶")

dog = Dog("Bruno", "German Shepherd")
dog.eat()    # Inherited from Animal
dog.speak()  # Defined in Dog
```

#### Multiple Inheritance:
```python
class Mom:
    cooking_skill = "Gourmet Chef"

class Dad:
    business_skill = "Venture Investor"

class Child(Mom, Dad):
    coding_skill = "Python Master"

c = Child()
print(c.cooking_skill)   # Inherited from Mom
print(c.business_skill)  # Inherited from Dad
print(c.coding_skill)    # Child's own
```

---

### 4. Polymorphism & Method Overriding

Polymorphism allows different classes to define methods with the exact same name, each implementing unique behavior:

```python
class Cat:
    def speak(self):
        return "Meow! 🐱"

class Dog:
    def speak(self):
        return "Woof! 🐶"

for pet in [Cat(), Dog()]:
    print(pet.speak())
```

---

## 🪄 4. Magic / Dunder Methods & Operator Overloading

Dunder (*Double Underscore*) methods define how custom objects interact with Python's built-in syntax.

### Common Dunder Methods

| Method | Triggered by | Description |
| :--- | :--- | :--- |
| `__init__(self)` | `Class()` | Object creation |
| `__str__(self)` | `print(obj)`, `str(obj)` | User-friendly string representation |
| `__repr__(self)` | `repr(obj)` | Unambiguous developer string representation |
| `__len__(self)` | `len(obj)` | Returns length |
| `__add__(self, other)` | `obj1 + obj2` | Custom addition |
| `__sub__(self, other)` | `obj1 - obj2` | Custom subtraction |
| `__eq__(self, other)` | `obj1 == obj2` | Custom equality comparison |

### Operator Overloading Example

```python
class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        # Overloading the '+' operator
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __str__(self):
        # Overloading string formatting for print()
        return f"{self.real} + {self.img}i"

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
c3 = c1 + c2  # Triggers c1.__add__(c2)

print("Result:", c3)  # Output: 4 + 6i
```

---

## 💻 5. Practice Problems & Solutions (WAP)

---

### Problem 1: Student Class with Average Marks Calculation

**Task**: Create a `Student` class that takes `name` and a list of marks as constructor arguments. Add a method `get_avg()` that computes and prints the average score.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        if not self.marks:
            print(f"No marks recorded for {self.name}.")
            return 0
        
        avg_score = sum(self.marks) / len(self.marks)
        print(f"Hi {self.name}, your average score is: {avg_score:.2f}")
        return avg_score

s1 = Student("Tony Stark", [99, 98, 97, 69])
s1.get_avg()
# Output: Hi Tony Stark, your average score is: 90.75
```

---

### Problem 2: Bank Account with Debit, Credit & Balance

**Task**: Create an `Account` class with `balance` and `account_no` attributes. Implement methods for `debit(amount)`, `credit(amount)`, and `get_balance()`.

```python
class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.account_no = acc_no

    def debit(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds!")
            return
        self.balance -= amount
        print(f"₹{amount:,} debited. Total balance = ₹{self.get_balance():,}")

    def credit(self, amount):
        if amount <= 0:
            print("❌ Invalid deposit amount!")
            return
        self.balance += amount
        print(f"₹{amount:,} credited. Total balance = ₹{self.get_balance():,}")

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 154659)
acc1.debit(1000)   # Output: ₹1,000 debited. Total balance = ₹9,000
acc1.credit(5000)  # Output: ₹5,000 credited. Total balance = ₹14,000
```

---

### Problem 3: Multi-level Inheritance & Employee Hierarchy

**Task**: Create an `Employee` base class with `role`, `dept`, and `salary`. Create an `Engineer` subclass inheriting from `Employee` that adds `name` and `age`.

```python
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print(f"Role: {self.role} | Dept: {self.dept} | Salary: ₹{self.salary:,}")

class Engineer(Employee):
    def __init__(self, name, age, salary):
        super().__init__("Software Engineer", "Engineering", salary)
        self.name = name
        self.age = age

    def show_engineer_info(self):
        print(f"Name: {self.name} (Age: {self.age})")
        self.show_details()

eng = Engineer("Keshav", 24, 1200000)
eng.show_engineer_info()
```

---

### Problem 4: 2D Vector Addition with Operator Overloading

**Task**: Create a `Vector2D` class that stores `(x, y)` coordinates and overloads `+` and `*` (dot product).

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        # Dot product
        return (self.x * other.x) + (self.y * other.y)

    def __str__(self):
        return f"({self.x}i + {self.y}j)"

v1 = Vector2D(2, 3)
v2 = Vector2D(4, 5)

v3 = v1 + v2
dot_prod = v1 * v2

print("v1 + v2 =", v3)           # Output: (6i + 8j)
print("v1 . v2 =", dot_prod)     # Output: 23
```

---

## 🚀 How to Run

1. **Verify Python Installation**:
   ```bash
   python3 --version
   ```
2. **Execute OOP Script**:
   ```bash
   python3 chapter9_oops.py
   ```

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA(TANMAY)!

</div>