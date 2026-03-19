**Task A**
Python treats empty containers (like `[]`, `""`, `{}`) as `False` by design to simplify control flow. This allows developers to write concise checks (e.g., `if my_list:`) to determine if a collection contains data, avoiding more verbose length checks like `if len(my_list) > 0:`.

**Task B**
The `is` operator should be used when you need to check object identity—meaning both variables point to the exact same memory address. It is primarily used to compare variables against built-in singletons like `None`, `True`, or `False`. For comparing the actual content or values of numbers, strings, or lists, `==` must be used.

**Task D**
The `match` statement is convenient for analyzing structured data because it performs structural pattern matching. It simultaneously verifies the shape of the data (e.g., a tuple of a specific length) and automatically unpacks its contents into variables in a single, highly readable block, eliminating the need for complex chains of `if/elif`, `isinstance()`, and length checks.

**Task F**
1. A list comprehension evaluates immediately, computes all items, and stores the entire list in memory at once. A generator expression computes one item at a time on demand, using a minimal and constant amount of memory regardless of the sequence size.
2. Generators are considered "lazy" because they do not compute their yielded values upfront. They pause execution at the `yield` statement and only compute the next value when explicitly requested (e.g., via a `for` loop).
3. When a generator finishes execution (reaches the end of its function logic or hits a `return`), it raises a `StopIteration` exception. This automatically signals to loops or consuming functions that there are no more items to process.