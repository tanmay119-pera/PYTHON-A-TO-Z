<div align="center">

# 🔐 Project 2: "Random Password Generator"

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Google Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="center">
  <strong>A customizable, cryptographically secure password generator in Python: demonstrates the <code>string</code> module, <code>random</code> vs <code>secrets</code> modules, list comprehensions, character set pooling, and password complexity guarantees.</strong>
</p>

---

</div>

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🔤 1. The `string` Module Constants](#-1-the-string-module-constants)
- [🎲 2. Random Selection Mechanics](#-2-random-selection-mechanics)
  - [`random.choice()` (Standard)](#randomchoice-standard)
  - [`secrets.choice()` (Cryptographically Secure)](#secretschoice-cryptographically-secure)
- [⚡ 3. Three Implementation Approaches](#-3-three-implementation-approaches)
  - [Approach 1: Standard `for` Loop Accumulator](#approach-1-standard-for-loop-accumulator)
  - [Approach 2: List Comprehension with `str.join()`](#approach-2-list-comprehension-with-strjoin)
  - [Approach 3: Guaranteed Complexity (Enterprise-Grade)](#approach-3-guaranteed-complexity-enterprise-grade)
- [🛡️ 4. Password Strength & Security Principles](#️-4-password-strength--security-principles)
- [💻 5. Complete Interactive CLI Implementation](#-5-complete-interactive-cli-implementation)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)

---

## 📌 Project Overview

A strong password generator produces unpredictable, high-entropy character sequences that defend against dictionary attacks, brute-force algorithms, and credential stuffing.

This project demonstrates how to assemble custom character pools (letters, digits, symbols), sample characters randomly, and enforce security policies (minimum lengths, required character categories).

---

## 🔤 1. The `string` Module Constants

Python's built-in `string` module provides pre-defined constant character sets:

```python
import string

print(string.ascii_letters)    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)           # 0123456789
print(string.punctuation)      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Combining Character Sets:
```python
# Pool of all 94 printable ASCII characters
char_pool = string.ascii_letters + string.digits + string.punctuation
print("Total Pool Size:", len(char_pool))  # 94 characters
```

---

## 🎲 2. Random Selection Mechanics

### `random.choice()` (Standard)
Picks a pseudo-random element from a non-empty sequence:

```python
import random
import string

char = random.choice(string.ascii_letters)
print("Random Character:", char)
```

### `secrets.choice()` (Cryptographically Secure)
The `secrets` module uses system entropy sources (e.g., `/dev/urandom` on Unix/macOS) designed specifically for security tokens, API keys, and passwords.

```python
import secrets
import string

secure_char = secrets.choice(string.ascii_letters + string.digits)
print("Cryptographically Secure Char:", secure_char)
```

---

## ⚡ 3. Three Implementation Approaches

### Approach 1: Standard `for` Loop Accumulator

```python
import random
import string

pass_len = 12
char_pool = string.ascii_letters + string.digits + string.punctuation

password = ""
for _ in range(pass_len):
    password += random.choice(char_pool)

print(f"Generated Password ({len(password)} chars): {password}")
```

---

### Approach 2: List Comprehension with `str.join()`

List comprehensions combined with `"".join()` are faster and more idiomatic in Python:

```python
import random
import string

pass_len = 16
char_pool = string.ascii_letters + string.digits + string.punctuation

# Generate list of characters and join into a single string
password = "".join([random.choice(char_pool) for _ in range(pass_len)])

print(f"Generated Password: {password}")
```

---

### Approach 3: Guaranteed Complexity (Enterprise-Grade)

Pure random sampling might accidentally produce a password missing digits or special symbols. This approach guarantees **at least one uppercase, one lowercase, one digit, and one special character**, then fills the remainder randomly and shuffles:

```python
import random
import string

def generate_strong_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 to satisfy complexity rules.")

    # 1. Guarantee at least 1 character from each category
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # 2. Fill the remaining length from the full combined pool
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_chars += [random.choice(all_chars) for _ in range(length - 4)]

    # 3. Shuffle so guaranteed characters aren't in predictable starting positions
    random.shuffle(password_chars)

    return "".join(password_chars)

print("Strong Guaranteed Password:", generate_strong_password(14))
```

---

## 🛡️ 4. Password Strength & Security Principles

```
           ┌───────────────────────────────────────────────┐
           │        Entropy = L × log₂(Pool Size)          │
           └───────────────────────────────────────────────┘
```

| Length | Character Pool | Total Combinations | Entropy | Strength Rating |
| :---: | :---: | :---: | :---: | :---: |
| **8** | Digits only ($10$) | $10^8 \approx 100 \text{ Million}$ | $\approx 26.6$ bits | 🔴 Very Weak |
| **8** | Letters + Digits ($62$) | $62^8 \approx 2.18 \times 10^{14}$ | $\approx 47.6$ bits | 🟡 Moderate |
| **12** | Letters + Digits + Symbols ($94$) | $94^{12} \approx 4.75 \times 10^{23}$ | $\approx 78.7$ bits | 🟢 Strong |
| **16** | Letters + Digits + Symbols ($94$) | $94^{16} \approx 3.67 \times 10^{31}$ | $\approx 104.9$ bits | 🛡️ Ultra Secure |

---

## 💻 5. Complete Interactive CLI Implementation

```python
import secrets
import string

def generate_custom_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    pool = ""
    guaranteed = []

    if use_lower:
        pool += string.ascii_lowercase
        guaranteed.append(secrets.choice(string.ascii_lowercase))
    if use_upper:
        pool += string.ascii_uppercase
        guaranteed.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        pool += string.digits
        guaranteed.append(secrets.choice(string.digits))
    if use_symbols:
        pool += string.punctuation
        guaranteed.append(secrets.choice(string.punctuation))

    if not pool:
        raise ValueError("At least one character set must be selected.")

    if length < len(guaranteed):
        length = len(guaranteed)

    # Fill remainder
    remaining_count = length - len(guaranteed)
    guaranteed += [secrets.choice(pool) for _ in range(remaining_count)]

    # Cryptographically shuffle characters
    secrets.SystemRandom().shuffle(guaranteed)
    return "".join(guaranteed)

def main():
    print("=" * 45)
    print("🔐 RANDOM PASSWORD GENERATOR 🔐")
    print("=" * 45)

    try:
        user_len = int(input("👉 Enter desired password length (e.g. 12, 16): ") or 12)
    except ValueError:
        user_len = 12

    pwd = generate_custom_password(length=user_len)
    print("\n" + "-" * 45)
    print(f"🔑 Your Secure Password ({len(pwd)} chars):")
    print(f"👉 {pwd}")
    print("-" * 45)

if __name__ == "__main__":
    main()
```

---

## 🚀 How to Run

1. **Run the Script**:
   ```bash
   python3 project2_password_generator.py
   ```
2. **Follow Prompt**:
   - Enter desired password length (default 12).
   - Copy your generated high-entropy password.

---

## 📄 License

This repository is maintained for educational reference and Python mastery. Free to use, adapt, and share!
