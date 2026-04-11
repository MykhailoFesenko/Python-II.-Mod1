# Lab 06: Python Object Model and Basic Object Behavior

## 1. Description

This lab implements a `Student` class and gradually extends it into a well-behaved Python object. It covers instance attribute storage, dunder methods (`__str__`, `__repr__`, `__eq__`, `__lt__`), operator overloading, sorting, and type-safe code with `mypy --strict`.

## 2. Environment

* **Python version used:** Python 3.12

## 3. Setup and Run Instructions

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# To run the code:
python src/your_code/main.py

# To run mypy strict type check:
mypy --strict src/your_code/main.py
```
