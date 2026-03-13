**Task A**
In Python, names are bindings, not containers. When we do `a = 7`, we are rebinding `a` to a new object, which changes the name-object relationship. The original integer object `5` itself is not modified. Therefore, the binding of `b` remains unchanged and still points to `5`.

**Task B**
Both names see the change because `a` and `b` are bound to the exact same list object in memory. Mutation modifies the object itself in place, whereas rebinding assigns a name to a completely new object.

**Task C**
Argument passing in Python is binding, not copying. Function parameters are just new local names. Mutating the object through this local name affects the caller, but rebinding the local parameter to a completely new object does not change the caller's original binding.

**Task D**
The list keeps growing because default argument values are evaluated only once when the function is defined. Because of this, every call to the function without an explicit argument reuses the exact same mutable list object in memory.

**Task E**
A shallow copy creates a new outer list but keeps bindings to the original nested objects. Modifying a nested object changes it everywhere. A deep copy recursively creates completely independent copies of all objects, including nested ones.

**Task F**
The reference count for `5` is unusually high due to a CPython optimization. Small integers are pre-allocated and cached as "immortal objects", meaning many internal parts of the interpreter share bindings to this exact same object, inflating its count. This behavior is strictly a CPython implementation detail, not a rule guaranteed by the Python language specification.