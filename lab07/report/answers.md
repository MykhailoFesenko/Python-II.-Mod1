# Lab 07: Final Questions

**1. What is duck typing?**

Duck typing means the type of an object is decided by what it can do, not by what class it inherits from. `StudentRegular` has a `serialize()` method and that alone is enough for `export()` to accept it. The downside is that there is no up-front check: if the method is missing or misspelled, you only find out at runtime as an `AttributeError`.

**2. How does Protocol differ from ABC?**

Protocol uses structural typing: any class that has the right methods with matching signatures is compatible, and the check is done mostly by mypy. ABC uses nominal typing: a class must explicitly inherit from the abstract base and implement every `@abstractmethod`, and the check happens at runtime when you try to create an instance. Protocol is more flexible; ABC gives a stronger runtime guarantee but forces inheritance.

**3. Does Protocol require inheritance? Why or why not?**

No. Protocol is structural, so it only checks that the required methods exist with matching signatures. `StudentRegular`, `StudentData` and `StudentSlots` all satisfy `Serializable` without inheriting from it. If you need `isinstance()` at runtime, the Protocol has to be marked `@runtime_checkable`, and even then it only checks method names, not their signatures.

**4. What problem does ABC solve?**

ABC enforces a contract at object creation time. If a subclass forgets to implement an `@abstractmethod`, Python raises `TypeError` on instantiation — you cannot even create the object. The abstract class itself also cannot be instantiated, as shown in Task D. The trade-off is that ABC forces inheritance and cannot describe required attributes, only methods.

**5. What does `@dataclass` generate automatically?**

It generates `__init__`, `__repr__` and `__eq__` from the declared fields. With extra flags it can also add ordering (`order=True`), make instances immutable (`frozen=True`), or generate `__slots__` (`slots=True`). That is why `StudentData` has almost no code but still behaves like a full class. Dataclasses are meant for data containers — complex construction logic has to go through `__post_init__`, and mutable defaults must use `field(default_factory=...)`.

**6. What changes when using slots?**

`slots=True` adds a `__slots__` declaration, so the instance no longer has a `__dict__`. Attributes live in a fixed layout, only declared names are allowed, and memory usage drops. In Task C, assigning `c.new_field` raises `AttributeError`. The restrictions: you lose dynamic attribute attachment, and combining non-empty `__slots__` from multiple base classes can fail.

**7. Why does Protocol work with different implementations (regular class, dataclass, slots)?**

Because Protocol only looks at the shape of the object — whether `serialize(self) -> str` exists with a matching signature. Regular classes, dataclasses and slot-based dataclasses all end up with that method, so all of them satisfy `Serializable`. The class hierarchy is irrelevant. The limitation is that "same shape" does not mean "same meaning": two classes with a `serialize()` returning very different things both pass the check.
