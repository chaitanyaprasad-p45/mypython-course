# Python Course: Variables

## Introduction to Variables

Variables in Python are used to store data values. They act as containers for data that can be referenced and manipulated in a program.

### Key Characteristics:
- Variables in Python do not need explicit declaration.
- The assignment operator (`=`) is used to assign a value to a variable.
- Variables are case-sensitive.

---

## Rules for Naming Variables

1. **Must begin with a letter (a-z, A-Z) or an underscore (`_`).**
   - Valid: `my_variable`, `_variable`
   - Invalid: `1variable`, `#var`

2. **Can only contain alphanumeric characters and underscores.**
   - Valid: `my_var`, `var123`
   - Invalid: `my-var`, `var@name`

3. **Cannot be a reserved keyword.**
   - Reserved keywords include `if`, `else`, `while`, etc.

4. **Case-sensitive.**
   - `MyVar`, `myvar`, and `MYVAR` are distinct.

---

## Variable Types in Python

Python is dynamically typed, meaning you don't need to declare the type of a variable. It is inferred at runtime.

### Examples of Variable Assignments:

```python
# Integer
x = 10

# Float
y = 3.14

# String
name = "Alice"

# Boolean
is_active = True

# List
numbers = [1, 2, 3]

# Dictionary
data = {"key": "value"}
```

---

## Dynamic Typing in Python

Variables can change types during execution:

```python
x = 5          # x is an integer
x = "Hello"    # x is now a string
```

---

## Best Practices for Variables

- Use descriptive variable names:
  ```python
  age = 25
  first_name = "John"
  ```
- Follow snake_case for variable names.
- Avoid single-character names (except in loops or mathematical contexts).
- Use constants for fixed values by conventionally using ALL_CAPS:
  ```python
  PI = 3.14159
  MAX_USERS = 100
  ```

---

## Exercise

1. Create variables for the following:
   - Your name
   - Your age
   - A list of your favorite fruits
   - A dictionary with keys `city` and `country` for your location

2. Print the type of each variable using the `type()` function.

---

## Summary

Variables are the foundation of any Python program. By understanding how to create, name, and use variables effectively, you can write clean and efficient Python code.
