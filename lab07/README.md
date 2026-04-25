# Lab 07: Behavior, Protocols, ABC, Dataclasses, Slots

## 1. Description
This laboratory implements one concept — an object that can be serialized — in several ways: a `Serializable` Protocol, a regular class (duck typing), a dataclass, a dataclass with `slots=True`, and an ABC-based version. All of them share the same `serialize()` method and work with the same `export()` helper.

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
