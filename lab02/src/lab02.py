print("A) Truthiness")

values_to_test = [0, 1, [], [1], "", "hello", None]

for val in values_to_test:
    print(f"value: {val!r} -> {bool(val)}")


print("\nB) Identity vs Equality")
print("1. Equal values but different objects")
a = [1, 2]
b = [1, 2]
print(f"a == b -> {a == b}")
print(f"a is b -> {a is b}")

print("2. Identical objects")
c = a
print(f"a == c -> {a == c}")
print(f"a is c -> {a is c}")

print("3. Behaviour with immutable values")
x = 100
y = 100
print(f"x == y -> {x == y}")
print(f"x is y -> {x is y}")


print("\nC) Control Flow")

def describe_number(x):
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif 0 < x < 10:
        return "small positive"
    elif x >= 10:
        return "large positive"

test_numbers = [-5, 0, 5, 10, 15]
for num in test_numbers:
    print(f"describe_number({num}) -> {describe_number(num)}")


print("\nD) Pattern Matching")

events = [
    ("click", 10, 20),
    ("keypress", "A"),
    ("quit",)
]

for event in events:
    match event:
        case ("click", x, y):
            print(f"click at {x} {y}")
        case ("keypress", key):
            print(f"key pressed: {key}")
        case ("quit",):
            print("quit event")


print("\nE) Comprehensions")

squares = [x**2 for x in range(1, 21)]
print(squares)

even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(even_squares)

squares_dict = {x: x**2 for x in range(1, 11)}
print(squares_dict)


print("\nF) Generators")

def even_numbers(limit):
    for i in range(0, limit, 2):
        yield i

for num in even_numbers(10):
    print(num)

sum_of_squares = sum(x**2 for x in even_numbers(1000000))
print(f"\nSum of squares of even numbers < 1,000,000: {sum_of_squares}")