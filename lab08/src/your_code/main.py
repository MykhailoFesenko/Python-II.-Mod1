from types import TracebackType


class Grade:
    _name: str

    def __set_name__(self, owner: type, name: str) -> None:
        self._name = "_" + name

    def __get__(self, obj: object, objtype: type | None = None) -> int:
        value = getattr(obj, self._name)
        assert isinstance(value, int)
        return value

    def __set__(self, obj: object, value: int) -> None:
        if not 0 <= value <= 100:
            raise ValueError(f"grade must be in [0, 100], got {value!r}")
        setattr(obj, self._name, value)


class Student:
    grade = Grade()

    def __init__(self, name: str, group: str, grade: int) -> None:
        self.name = name
        self.group = group
        self.grade = grade

    def __str__(self) -> str:
        return f"{self.name} ({self.group}) - {self.grade}"


class StudentIterator:
    def __init__(self, items: list[Student]) -> None:
        self._items = items
        self._i = 0

    def __iter__(self) -> "StudentIterator":
        return self

    def __next__(self) -> Student:
        if self._i >= len(self._items):
            raise StopIteration
        item = self._items[self._i]
        self._i += 1
        return item


class StudentCollection:
    def __init__(self, students: list[Student]) -> None:
        self._students = students

    def __iter__(self) -> StudentIterator:
        return StudentIterator(self._students)

    def __enter__(self) -> "StudentCollection":
        print("Entering context: collection opened")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        print("Exiting context: collection closed")


students = [
    Student("Mykhailo", "KH-124", 85),
    Student("Sofia", "KH-124", 99),
    Student("Olena", "KH-125", 75),
    Student("Ivan", "KH-125", 60),
]


print("--- Task A ---")
collection = StudentCollection(students)
for s in collection:
    print(s)
print("What do we see? Students are printed one by one without any index.")
print("Why does it work? for calls __iter__ on the collection and __next__ on the iterator until StopIteration.")

print("\n--- Task B ---")
with StudentCollection(students) as c:
    print("inside the with block")
print("What do we see? Entering and exiting messages wrap the body of the with block.")
print("Why does it work? with calls __enter__ before the block and __exit__ after it.")

print("\n--- Task B (with error) ---")
try:
    with StudentCollection(students) as c:
        raise RuntimeError("boom")
except RuntimeError as e:
    print("caught outside:", e)
print("What do we see? The exiting message still prints even though the body raised.")
print("Why does it work? __exit__ runs during stack unwinding; returning None lets the exception propagate.")

print("\n--- Task C ---")
st = Student("Daryna", "KH-126", 70)
print("initial grade:", st.grade)
st.grade = 95
print("after valid set:", st.grade)
try:
    st.grade = 120
except ValueError as e:
    print("rejected:", e)
try:
    _ = Student("Bohdan", "KH-126", -5)
except ValueError as e:
    print("rejected in __init__:", e)
print("What do we see? Out-of-range values are rejected; valid ones are stored.")
print("Why does it work? The Grade descriptor intercepts every assignment via __set__.")

print("\n--- Task D ---")
with StudentCollection(students) as c:
    for s in c:
        print(s.grade)
print("What do we see? Iteration, context manager and descriptor-backed grade all work together.")
print("Why does it work? Each protocol is independent: __iter__ drives the loop, __enter__/__exit__ frame the block, Grade validates each assignment.")
