print("A) Functions as Objects")

def apply_twice(func, x):
    return func(func(x))

print(apply_twice(lambda x: x + 1, 3))
print(apply_twice(abs, -5))

def double_value(x):
    return x * 2

print(apply_twice(double_value, 10))


print("\nB) Sorting with Lambda")

people = [
    ("Alice", 25),
    ("Bob", 20),
    ("Carol", 30),
    ("Dave", 22)
]

sorted_by_age = sorted(people, key=lambda p: p[1])
print("Sorted by age:")
print(sorted_by_age)

sorted_by_name = sorted(people, key=lambda p: p[0])
print("Sorted by name:")
print(sorted_by_name)


print("\nC) Function Factory")

def make_multiplier(k):
    return lambda x: x * k

times3 = make_multiplier(3)
print(times3(10))

times5 = make_multiplier(5)
print(times5(10))


print("\nD) Closure Counter")

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())
print(c())
print(c())


print("\nE) Lambda vs def")

def square_def(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(square_def(5))
print(square_lambda(5))
print(square_def(5) == square_lambda(5))


print("\nF) Functional Composition")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = filter(lambda x: x % 2 == 0, numbers)
squared_gen = (x ** 2 for x in evens)
total_sum = sum(squared_gen)

print(total_sum)