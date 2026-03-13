import copy
import sys
print("A) Binding / Rebinding")
a = 5
b = a
print("Initial:")
print(f"a={a}, b={b}")
print(f"id(a)={id(a)}")
print(f"id(b)={id(b)}")

a = 7
print("\nAfter rebinding a=7:")
print(f"a={a}, b={b}")
print(f"id(a)={id(a)}")
print(f"id(b)={id(b)}")
print("\n")


print("\nB) Mutation vs Rebinding")
a = [1, 2]
b = a
print("Initial:")
print(f"a={a}")
print(f"b={b}")

b.append(3)
print("\nAfter mutation:")
print(f"a={a}")
print(f"b={b}")
print(f"id(a) == id(b): {id(a) == id(b)}")
print("\n")


print("\nC) Function arguments\n")

def mutate_list(lst):
    lst.append(1)

def rebind_list(lst):
    lst = [999]

a = []
print("Before call:")
print(f"a={a}")

mutate_list(a)
print("\nAfter mutate_list(a):")
print(f"a={a}")

rebind_list(a)
print("\nAfter rebind_list(a):")
print(f"a={a}")
print("\n")


print("\nD) Default argument behavior")

def f(x=[]):
    x.append(1)
    return x

print("\nFirst call:")
print(f())

print("\nSecond call:")
print(f())
print("\n")


print("\nE) Copy semantics")
a = [[1, 2]]
print("\nOriginal:")
print(f"a={a}")

b = a.copy()
c = copy.deepcopy(a)

b[0].append(3)

print("\nAfter modifying b:")
print(f"a={a}")
print(f"b={b}")
print(f"c={c}")
print("\n")


print("\nF) Reference counting / GC")

# Part 1: normal object
x = []
print("Refcount(x):", sys.getrefcount(x))
y = x
print("Refcount(x) after y=x:", sys.getrefcount(x))

# Part 2: small integer ("immortal" object)
print("Refcount(5):", sys.getrefcount(5))
print("Refcount(123456):", sys.getrefcount(123456))