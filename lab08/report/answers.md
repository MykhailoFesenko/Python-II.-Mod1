# Lab 08: Final Questions

**1. How does a for loop work with custom objects?**

A `for` loop first calls `iter(obj)`, which in turn calls the object's `__iter__` method and expects an iterator back. Then it repeatedly calls `next(iterator)` on the returned iterator until `StopIteration` is raised, which the loop silently catches to stop. Any class that provides `__iter__` (and whose iterator provides `__next__`) can be used in a `for` loop.

**2. What methods are required for iteration?**

Two methods split across two roles. The *iterable* needs `__iter__`, which must return an iterator. The *iterator* needs both `__iter__` (usually `return self`) and `__next__`, which returns the next item or raises `StopIteration`. If `StopIteration` is never raised, the loop runs forever and must be killed manually.

**3. How does the `with` statement work internally?**

`with expr as name:` evaluates `expr`, calls `expr.__enter__()`, binds its return value to `name`, runs the body, and then calls `__exit__(exc_type, exc, tb)` with information about any exception that leaked out of the body (or three `None`s if the body finished normally). If `__exit__` returns a truthy value, the exception is swallowed; otherwise it keeps propagating.

**4. When is `__exit__` called?**

Always — when the body finishes normally, when `return`, `break` or `continue` leaves the block, and when the body raises an exception. That is what makes `with` reliable for cleanup (closing files, releasing locks, etc.). If a class omits `__exit__`, Python raises `AttributeError` and the object simply cannot be used with `with`.

**5. What problem do descriptors solve?**

Descriptors let you attach validation or computed logic to attribute access without changing how callers write `obj.attr = value` or `obj.attr`. In Task C, assigning `st.grade = 120` runs through `Grade.__set__`, which rejects the value. The downside is that the descriptor must live on the class (not the instance), so it is a class-wide contract; a single stray instance attribute with the same name would bypass the descriptor.

**6. What happens if a descriptor is not used?**

Without the descriptor, `student.grade = 120` would just store whatever you hand over — Python performs no validation on plain attributes. You would need to wrap every assignment in a method or use `@property` on each class, which duplicates code. Invalid grades like `-5` or `"A+"` would silently leak into the rest of the program and probably crash somewhere far from the real mistake.

**7. Why is direct iteration preferred over index-based loops in Python?**

Direct iteration works on *any* iterable (lists, sets, generators, files, custom classes), is usually faster because it avoids repeated indexing, and reads closer to the intent of the code. Index-based loops additionally require a knowable length and support for `[i]` lookup — generators and streams do not provide either. Direct iteration is also the only way to consume infinite or lazy sources, since there is no fixed end index to loop to.
