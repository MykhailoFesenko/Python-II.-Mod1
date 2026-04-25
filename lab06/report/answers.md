# Lab 06: Final Questions

**1. What is stored in `obj.__dict__`?**

`obj.__dict__` is a regular Python dictionary that holds all instance attributes of the object as key-value pairs. For a `Student` object it would contain `{'name': 'Mykhailo', 'group': 'KH-124', 'average_grade': 8.5}`. It only stores instance-level data, not class-level methods or class variables.

**2. What is the difference between a class and an object?**

A class is a blueprint or template that defines the structure and behavior (attributes and methods) of something. An object is a specific instance created from that blueprint. For example, `Student` is the class, and `Student("Mykhailo", "KH-124", 8.5)` is a concrete object in memory with its own data. You can create many independent objects from the same class.

**3. What does `__init__` do?**

`__init__` is the initializer (constructor) method. Python calls it automatically right after a new object is created. Its job is to set up the initial state of the object by assigning values to instance attributes. Without it, the object would exist but have no data attached to it.

**4. Who calls `__str__`, and when?**

Python calls `__str__` automatically whenever a human-readable string representation of the object is needed. The most common cases are: `print(obj)`, `str(obj)`, and f-strings like `f"{obj}"`. It is designed for end-user output, not debugging.

**5. What is the difference between `==` and `is`?**

`==` calls `__eq__` and checks whether two objects are *equal in value* — it compares the contents. `is` checks whether two variables point to the *exact same object in memory* (same identity). Two different `Student` objects with identical fields will have `==` return `True` but `is` return `False`, because they are two separate objects.

**6. Why do we use `other: object` in `__eq__` and `__lt__`?**

Python's type system requires that `__eq__` and `__lt__` accept `other: object` rather than `other: Student` because Python may call these methods with any type during comparisons (for example, when checking membership in a list or sorting mixed collections). Accepting `object` and then using `isinstance` to check the actual type is the correct, type-safe pattern — it prevents crashes and satisfies `mypy --strict`.
