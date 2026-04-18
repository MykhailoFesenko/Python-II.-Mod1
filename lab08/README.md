# Lab 08: Iteration, Context Managers, and Descriptors

## 1. Description
This laboratory implements a `StudentCollection` that supports the iteration protocol (`__iter__`, `__next__` via a separate iterator class), the context manager protocol (`__enter__`, `__exit__`), and uses a `Grade` descriptor on `Student` to validate that grades stay in the range 0..100.

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
