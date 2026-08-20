<div align="center">

# 🏛️ ADVANCED IN PYTHON OBJECT ORIENTED PROGRAMMING 2 — CHAPTER 9.2

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A comprehensive deep-dive into Advanced Object-Oriented Programming in Python: The <code>del</code> keyword & destructors, Private attributes/methods & Name Mangling, All types of Inheritance, <code>super()</code> mechanics, <code>@classmethod</code>, the <code>@property</code> decorator (Getters/Setters), Polymorphism, and Operator Overloading with Dunder methods.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [🗑️ 1. The `del` Keyword & `__del__()` Destructor](#️-1-the-del-keyword--__del__-destructor)
  - [Deleting Object Attributes](#deleting-object-attributes)
  - [Deleting Entire Objects & Garbage Collection](#deleting-entire-objects--garbage-collection)
- [🔒 2. Private Attributes & Methods (Encapsulation Deep-Dive)](#-2-private-attributes--methods-encapsulation-deep-dive)
  - [Private Naming Convention (`__`)](#private-naming-convention)
  - [Name Mangling (`_ClassName__var`)](#name-mangling)
  - [Controlled Access via Getters & Setters](#controlled-access-via-getters--setters)
- [🧬 3. Inheritance Deep-Dive](#-3-inheritance-deep-dive)
  - [1. Single Inheritance](#1-single-inheritance)
  - [2. Multi-Level Inheritance](#2-multi-level-inheritance)
  - [3. Multiple Inheritance & Method Resolution Order (MRO)](#3-multiple-inheritance--method-resolution-order-mro)
- [⚡ 4. The `super()` Method](#-4-the-super-method)
  - [Calling Parent Constructor (`super().__init__()`)](#calling-parent-constructor)
  - [Invoking Parent Methods](#invoking-parent-methods)
- [🏷️ 5. `@classmethod` vs Instance Methods](#️-5-classmethod-vs-instance-methods)
  - [Modifying Class-Level State](#modifying-class-level-state)
  - [The 3 Ways to Update Class Variables](#the-3-ways-to-update-class-variables)
- [✨ 6. The `@property` Decorator (Getters & Setters)](#-6-the-property-decorator-getters--setters)
  - [Dynamic Attribute Calculation](#dynamic-attribute-calculation)
  - [Defining Property Setters (`@prop.setter`)](#defining-property-setters)
- [🪄 7. Polymorphism & Operator Overloading](#-7-polymorphism--operator-overloading)
  - [Dunder Methods for Arithmetic Operators](#dunder-methods-for-arithmetic-operators)
  - [Dunder Methods for Comparison Operators](#dunder-methods-for-comparison-operators)
  - [Complex Numbers & Custom Arithmetic Class](#complex-numbers--custom-arithmetic-class)
- [💻 8. Practice Problems & Solutions (WAP)](#-8-practice-problems--solutions-wap)
  - [Problem 1: Circle Class (Area & Perimeter)](#problem-1-circle-class-area--perimeter)
  - [Problem 2: Employee & Engineer Hierarchy](#problem-2-employee--engineer-hierarchy)
  - [Problem 3: Order Class with Price Comparison (`__gt__`)](#problem-3-order-class-with-price-comparison-__gt__)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Overview

While basic OOP introduces classes and objects, **Advanced OOP** enables enterprise-grade architectural design:
- Strict information hiding (private attributes and encapsulation).
- Reusable class hierarchies across single, multi-level, and multiple inheritance.
- Clean interfaces using `@property` and `@classmethod`.
- Intuitive mathematical syntax for domain objects using **Operator Overloading**.

```
┌─────────────────────────────────────────────────────────────┐
│                     Advanced OOP Features                   │
├──────────────────────────────┬──────────────────────────────┤
│  Data & State Protection     │  Hierarchy & Polymorphism    │
│  • Private Attributes (__)   │  • Multi-Level Inheritance   │
│  • Name Mangling             │  • Multiple Inheritance & MRO│
│  • @property (Getters/Setters│  • super() Proxy             │
│  • @classmethod              │  • Operator Overloading      │
└──────────────────────────────┴──────────────────────────────┘
```

---

## 🗑️ 1. The `del` Keyword & `__del__()` Destructor

The `del` keyword removes object references and attributes from memory.

### Deleting Object Attributes
```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = Student("Alex", 101)
print(s1.name)  # Output: Alex

del s1.name     # Deletes only the 'name' attribute
# print(s1.name) # ❌ AttributeError: 'Student' object has no attribute 'name'
```

### Deleting Entire Objects & Garbage Collection
When all references to an object are deleted with `del`, Python's garbage collector automatically invokes the `__del__()` destructor method:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Object for '{self.name}' has been destroyed from memory!")

s1 = Student("Alex")
del s1  # Explicitly deletes reference -> Triggers __del__()
```

---

## 🔒 2. Private Attributes & Methods (Encapsulation Deep-Dive)

In Python, prefixing an attribute or method name with double underscores (`__`) marks it as **private**.

### Private Naming Convention (`__`)

```python
class BankAccount:
    def __init__(self, acc_no, password):
        self.acc_no = acc_no          # Public attribute
        self.__password = password    # Private attribute

    def __authenticate(self):         # Private method
        print("Authenticating internal security tokens...")

    def get_password(self):           # Public getter
        self.__authenticate()
        return self.__password

acc = BankAccount("ACC-9876", "SecretPass123")
print("Account Number:", acc.acc_no)
print("Password via Getter:", acc.get_password())

# Direct outside access fails:
# print(acc.__password)       # ❌ AttributeError
# acc.__authenticate()        # ❌ AttributeError
```

### Name Mangling

Python implements privacy using **Name Mangling**. An attribute named `__password` in class `BankAccount` is internally renamed to `_BankAccount__password`.

```python
# Technically accessible via mangled name (NOT recommended in practice):
print("Mangled Access:", acc._BankAccount__password)
```

---

## 🧬 3. Inheritance Deep-Dive

```
   1. SINGLE             2. MULTI-LEVEL             3. MULTIPLE
 ┌──────────┐             ┌──────────┐        ┌─────────┐   ┌─────────┐
 │  Parent  │             │Grandparent│       │ ParentA │   │ ParentB │
 └────┬─────┘             └────┬─────┘        └────┬────┘   └────┬────┘
      ▼                        ▼                   └──────┬──────┘
 ┌──────────┐             ┌──────────┐                    ▼
 │  Child   │             │  Parent  │               ┌─────────┐
 └──────────┘             └────┬─────┘               │  Child  │
                               ▼                     └─────────┘
                          ┌──────────┐
                          │  Child   │
                          └──────────┘
```

### 1. Single Inheritance
A child class inherits from one single parent class:

```python
class Vehicle:
    def start(self):
        print("Vehicle engine started.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

c = Car()
c.start()  # Inherited
c.drive()
```

### 2. Multi-Level Inheritance
A class inherits from a child class, forming a grandparent-parent-child chain:

```python
class Vehicle:
    def start(self):
        print("Engine running...")

class ToyotaCar(Vehicle):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, fuel_type):
        super().__init__("Toyota")
        self.fuel_type = fuel_type

car = Fortuner("Diesel")
print(f"Brand: {car.brand} | Fuel: {car.fuel_type}")
car.start()  # Inherited from Vehicle
```

### 3. Multiple Inheritance & Method Resolution Order (MRO)
A child class inherits directly from two or more distinct parent classes:

```python
class BackendDeveloper:
    backend_skill = "Python & PostgreSQL"

class FrontendDeveloper:
    frontend_skill = "React & CSS"

class FullStackEngineer(BackendDeveloper, FrontendDeveloper):
    devops_skill = "Docker & Kubernetes"

dev = FullStackEngineer()
print(dev.backend_skill)   # Inherited from BackendDeveloper
print(dev.frontend_skill)  # Inherited from FrontendDeveloper
print(dev.devops_skill)    # Own skill

# Inspect Method Resolution Order
print("MRO:", FullStackEngineer.__mro__)
```

---

## ⚡ 4. The `super()` Method

`super()` provides direct access to parent class methods and constructors, avoiding hardcoding parent names.

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from Parent, {self.name}!")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Execute parent initialization
        self.age = age

    def greet(self):
        super().greet()         # Call parent method
        print(f"I am {self.age} years old.")

ch = Child("Karan", 21)
ch.greet()
```

---

## 🏷️ 5. `@classmethod` vs Instance Methods

### Modifying Class-Level State

By default, methods operate on object instances (`self`). To modify class variables cleanly without creating an instance, use `@classmethod` with `cls`.

```python
class Person:
    name = "Anonymous"  # Class attribute

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name

print("Before:", Person.name)   # Anonymous
Person.change_name("Alex")
print("After:", Person.name)    # Alex
```

### The 3 Ways to Update Class Variables

```python
# Method 1 (Incorrect for class var): Creates instance variable, leaves class var unchanged
self.name = "Alex"

# Method 2 (Valid via instance):
self.__class__.name = "Alex"

# Method 3 (Best Practice):
@classmethod
def change_name(cls, new_name):
    cls.name = new_name
```

---

## ✨ 6. The `@property` Decorator (Getters & Setters)

The `@property` decorator allows a method to be accessed like an attribute without using parentheses `()`. It ensures dependent attributes stay synchronized when underlying data changes.

### Dynamic Attribute Calculation

```python
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        # Automatically recalculates whenever accessed!
        avg = (self.phy + self.chem + self.math) / 3
        return f"{avg:.2f}%"

stud = Student(98, 97, 99)
print("Initial percentage:", stud.percentage)  # Output: 98.00%

# Updating physics marks
stud.phy = 86
print("Updated percentage:", stud.percentage)  # Output: 94.00% (Updated dynamically!)
```

### Defining Property Setters (`@prop.setter`)

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible!")
        self._celsius = value

temp = Temperature(25)
temp.celsius = 30  # Invokes setter
print("Temperature:", temp.celsius)
```

---

## 🪄 7. Polymorphism & Operator Overloading

**Operator Overloading** allows custom classes to define their own behavior for standard Python operators (`+`, `-`, `*`, `>`, `==`) using **Dunder Methods**.

### Dunder Methods for Arithmetic Operators

| Operator | Expression | Dunder Method |
| :---: | :---: | :--- |
| `+` | `a + b` | `a.__add__(b)` |
| `-` | `a - b` | `a.__sub__(b)` |
| `*` | `a * b` | `a.__mul__(b)` |
| `/` | `a / b` | `a.__truediv__(b)` |
| `//` | `a // b` | `a.__floordiv__(b)` |
| `%` | `a % b` | `a.__mod__(b)` |
| `**` | `a ** b` | `a.__pow__(b)` |

---

### Dunder Methods for Comparison Operators

| Operator | Expression | Dunder Method |
| :---: | :---: | :--- |
| `>` | `a > b` | `a.__gt__(b)` |
| `<` | `a < b` | `a.__lt__(b)` |
| `>=` | `a >= b` | `a.__ge__(b)` |
| `<=` | `a <= b` | `a.__le__(b)` |
| `==` | `a == b` | `a.__eq__(b)` |
| `!=` | `a != b` | `a.__ne__(b)` |

---

### Complex Numbers & Custom Arithmetic Class

```python
class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        sign = "+" if self.img >= 0 else "-"
        return f"{self.real} {sign} {abs(self.img)}j"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = (self.real * other.real) - (self.img * other.img)
        img_part = (self.real * other.img) + (self.img * other.real)
        return ComplexNumber(real_part, img_part)

c1 = ComplexNumber(1, 3)
c2 = ComplexNumber(4, 6)

print("c1 =", c1)          # 1 + 3j
print("c2 =", c2)          # 4 + 6j
print("c1 + c2 =", c1 + c2) # 5 + 9j
print("c1 - c2 =", c1 - c2) # -3 - 3j
print("c1 * c2 =", c1 * c2) # -14 + 18j
```

---

## 💻 8. Practice Problems & Solutions (WAP)

---

### Problem 1: Circle Class (Area & Perimeter)

**Task**: Define a `Circle` class initialized with radius $r$. Implement `area()` ($\pi r^2$) and `perimeter()` ($2 \pi r$) methods.

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

c1 = Circle(21)
print(f"Radius: {c1.radius}")
print(f"Area: {c1.area():.2f}")          # Output: 1385.44
print(f"Perimeter: {c1.perimeter():.2f}") # Output: 131.95
```

---

### Problem 2: Employee & Engineer Hierarchy

**Task**: 
1. Create an `Employee` class with attributes `role`, `dept`, `salary`, and a method `show_details()`.
2. Create an `Engineer` subclass inheriting from `Employee` that adds `name` and `age`, while leveraging `super()`.

```python
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print(f"Role: {self.role} | Department: {self.dept} | Salary: ₹{self.salary:,}")

class Engineer(Employee):
    def __init__(self, name, age, salary=85000, role="Software Engineer", dept="IT"):
        super().__init__(role, dept, salary)
        self.name = name
        self.age = age

    def show_details(self):
        print(f"--- Employee Profile: {self.name} (Age: {self.age}) ---")
        super().show_details()

emp = Employee("HR Lead", "Human Resources", 60000)
emp.show_details()

print()
eng = Engineer("Tanmay", 22, salary=120000)
eng.show_details()
```

---

### Problem 3: Order Class with Price Comparison (`__gt__`)

**Task**: Create an `Order` class storing `item` and `price`. Overload the `>` operator using `__gt__()` to compare order values.

```python
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

    def __str__(self):
        return f"{self.item} (₹{self.price})"

ord1 = Order("Chips", 20)
ord2 = Order("Tea", 15)

print(f"{ord1} > {ord2} :", ord1 > ord2)  # Output: True
print(f"{ord2} > {ord1} :", ord2 > ord1)  # Output: False
```

---

## 🚀 How to Run

1. **Verify Python Installation**:
   ```bash
   python3 --version
   ```
2. **Execute Advanced OOP Script**:
   ```bash
   python3 chapter9_part2_oops.py
   ```

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!

---

<div align="center">

Made with ❤️ for mastering Python | ⭐ Star this repo if you found it helpful AUTHOR - ADESH SRIVASTAVA!

</div>