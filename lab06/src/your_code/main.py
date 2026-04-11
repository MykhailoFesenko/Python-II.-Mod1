class Student:
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def __str__(self) -> str:
        return f"Student: {self.name} (group={self.group}, grade={self.average_grade})"

    def __repr__(self) -> str:
        return f"Student(name='{self.name}', group='{self.group}', average_grade={self.average_grade})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return (
            self.name == other.name
            and self.group == other.group
            and self.average_grade == other.average_grade
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            raise TypeError(
                f"'<' not supported between instances of 'Student' and '{type(other).__name__}'"
            )
        return self.average_grade < other.average_grade


# --- Task A ---
print("--- Task A ---")
mykhailo = Student("Mykhailo", "KH-124", 8.5)
print("name:", mykhailo.name)
print("group:", mykhailo.group)
print("average_grade:", mykhailo.average_grade)
print("What do we see? All three attributes are stored inside the object and accessible via dot notation.")

# --- Task B ---
print("\n--- Task B ---")
print("__dict__:", mykhailo.__dict__)
print("What do we see? __dict__ is a regular Python dictionary that holds all instance attributes as key-value pairs.")
mykhailo.__dict__["average_grade"] = 9.0
print("After modifying average_grade via __dict__:", mykhailo.average_grade)
print("What does it mean? Modifying __dict__ directly changes the real attribute — there is no copy.")

# --- Task C ---
print("\n--- Task C ---")
sofia = Student("Sofia", "KH-124", 9.9)
print(sofia)
print("What do we see? print() calls __str__ automatically and produces a human-readable line.")

# --- Task D ---
print("\n--- Task D ---")
print(repr(sofia))
print("What do we see? repr() calls __repr__ and produces a developer-friendly, unambiguous representation.")

# --- Task E ---
print("\n--- Task E ---")
s1 = Student("Olena", "KH-124", 7.5)
s2 = Student("Olena", "KH-124", 7.5)
s3 = Student("Ivan", "KH-125", 6.0)
print("s1 == s2 (identical):", s1 == s2)
print("s1 == s3 (different):", s1 == s3)
print("s1 == 'hello' (wrong type):", s1 == "hello")
print("What do we see? Two students with all equal fields compare as True. Wrong types safely return False.")

# --- Task F ---
print("\n--- Task F ---")
print("s1 (7.5) < s3 (6.0):", s1 < s3)
print("s3 (6.0) < s1 (7.5):", s3 < s1)
try:
    _ = s1 < 42  # type: ignore[operator]
except TypeError as e:
    print("TypeError when comparing with int:", e)
print("What do we see? Ordering works by average_grade. Incompatible types raise TypeError.")

# --- Task G ---
print("\n--- Task G ---")
students = [
    Student("Mykhailo", "KH-124", 8.5),
    Student("Sofia", "KH-124", 9.9),
    Student("Olena", "KH-124", 7.5),
    Student("Ivan", "KH-125", 6.0),
    Student("Daryna", "KH-125", 9.1),
    Student("Bohdan", "KH-126", 7.0),
]
students.sort()
for s in students:
    print(s)
print("What do we see? list.sort() uses __lt__ under the hood — students are sorted by average_grade ascending.")
