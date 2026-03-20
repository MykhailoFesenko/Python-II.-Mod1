1. **What does it mean that functions in Python are first-class objects?**
It means functions are treated like any other data type (such as integers or strings). They can be assigned to variables, passed as arguments to other functions, returned from other functions, and stored in data structures like lists or dictionaries.

2. **What is the difference between a function defined with def and a lambda expression?**
A `def` statement creates a named function that can contain multiple expressions, statements, and complex logic (like loops and error handling). A `lambda` expression creates an anonymous (unnamed) function restricted to a single expression. It implicitly returns the result of that expression without the `return` keyword.

3. **What is a closure?**
A closure is a dynamically created function that "remembers" the variables from its enclosing lexical scope even after the outer function has finished executing. It pairs a function with an environment, allowing the inner function to access and modify the outer function's local variables (using the `nonlocal` keyword).

4. **In what situations are closures useful?**
Closures are highly useful for maintaining internal state without needing to define a full class (like our counter function). They are also the fundamental mechanism behind Python decorators, function factories (generating specialized functions dynamically), and data hiding (encapsulation).