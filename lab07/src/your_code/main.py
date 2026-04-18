from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


class Serializable(Protocol):
    def serialize(self) -> str: ...


def export(obj: Serializable) -> None:
    print(obj.serialize())


class StudentRegular:
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"{self.name}, {self.group}, {self.average_grade}"


@dataclass
class StudentData:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"{self.name}, {self.group}, {self.average_grade}"


@dataclass(slots=True)
class StudentSlots:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"{self.name}, {self.group}, {self.average_grade}"


class SerializableABC(ABC):
    @abstractmethod
    def serialize(self) -> str: ...


class StudentABC(SerializableABC):
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"{self.name}, {self.group}, {self.average_grade}"


print("--- Task A ---")
a = StudentRegular("Mykhailo", "KH-124", 8.5)
export(a)
print("What do we see? A class that does not inherit from anything still works with export().")
print("Why does it work? Protocol checks that the method exists, not the base class.")

print("\n--- Task B ---")
b = StudentData("Sofia", "KH-124", 9.9)
export(b)
print("What do we see? Same result with less code - __init__ and __repr__ are generated.")
print("Why does it work? @dataclass only adds dunder methods; serialize() still matches the Protocol.")

print("\n--- Task C ---")
c = StudentSlots("Olena", "KH-125", 7.5)
export(c)
print("__slots__:", StudentSlots.__slots__)
print("has __dict__:", hasattr(c, "__dict__"))
try:
    c.new_field = "x"  # type: ignore[attr-defined]
except AttributeError as e:
    print("AttributeError:", e)
print("What do we see? No __dict__ and a new attribute is rejected.")
print("Why does it work? slots=True fixes the attribute layout, but serialize() is still there.")

print("\n--- Task D ---")
d = StudentABC("Ivan", "KH-125", 6.0)
print("isinstance(d, SerializableABC):", isinstance(d, SerializableABC))
export(d)
try:
    _ = SerializableABC()  # type: ignore[abstract]
except TypeError as e:
    print("TypeError:", e)
print("What do we see? StudentABC satisfies both the ABC (inheritance) and the Protocol (shape).")
print("Why does it work? ABC enforces inheritance at creation; Protocol checks the method at the call site.")
