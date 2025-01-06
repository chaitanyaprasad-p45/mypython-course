
# Python Course:

## Introduction to Python Syntax
Python syntax can be executed by writing directly in the Command Line:
```python
>>> print("Hello, World!")
Hello, World!
```
Or by creating a python file on the server, using the .py file extension, and running it in the Command Line:
```python
C:\Users\Your Name>python myfile.py
```

| **Concept**              | **Syntax Example**                                       |
|--------------------------|---------------------------------------------------------|
| Print Statement          | `print("Hello, World!")`                               |
| Running a Python File    | `python myfile.py`                                      |

---

## Python Indentation

Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
Python uses indentation to indicate a block of code.

| **Concept**              | **Syntax Example**                                       |
|--------------------------|---------------------------------------------------------|
| Proper Indentation       | ```python
if 5 > 2:
    print("Five is greater than two!")
``` |
| Missing Indentation      | ```python
if 5 > 2:
print("Five is greater than two!")
``` |

Python will give you an error if you skip the indentation:
```python
if 5 > 2:
print("Five is greater than two!")
```

---

## Introduction to Python Comments

- Comments can be used to explain Python code.
- Comments can be used to make the code more readable.
- Comments can be used to prevent execution when testing code.

| **Concept**              | **Syntax Example**                                       |
|--------------------------|---------------------------------------------------------|
| Single-line Comment      | `# This is a comment`                                   |
| Multi-line Comment       | `"""This is a multi-line comment"""`                  |

---

## Introduction to Python Variables

Variables in Python are used to store data values. They act as containers for data that can be referenced and manipulated in a program.

### Key Characteristics:
- Variables in Python do not need explicit declaration.
- The assignment operator (`=`) is used to assign a value to a variable.
- Variables are case-sensitive.

---

## Rules for Naming Variables

| **Rule**                                                                 | **Examples**                           |
|--------------------------------------------------------------------------|----------------------------------------|
| Must begin with a letter (a-z, A-Z) or an underscore (`_`).              | Valid: `my_variable`, `_variable`      |
|                                                                          | Invalid: `1variable`, `#var`           |
| Can only contain alphanumeric characters and underscores.               | Valid: `my_var`, `var123`              |
|                                                                          | Invalid: `my-var`, `var@name`          |
| Cannot be a reserved keyword.                                           | Reserved keywords: `if`, `else`, etc.  |
| Case-sensitive.                                                         | `MyVar`, `myvar`, and `MYVAR` differ.  |

---

## Variable Types in Python

Python is dynamically typed, meaning you don't need to declare the type of a variable. It is inferred at runtime.

### Examples of Variable Assignments:

| **Type**       | **Example**                  |
|----------------|------------------------------|
| Integer        | `x = 10`                     |
| Float          | `y = 3.14`                   |
| String         | `name = "Alice"`            |
| Boolean        | `is_active = True`           |
| List           | `numbers = [1, 2, 3]`        |
| Dictionary     | `data = {"key": "value"}` |

---

## Dynamic Typing in Python

Variables can change types during execution:

| **Concept**              | **Syntax Example**                                       |
|--------------------------|---------------------------------------------------------|
| Dynamic Typing           | ```python
x = 5          # x is an integer
x = "Hello"    # x is now a string
``` |

---

## Best Practices for Variables

| **Practice**                       | **Example**                          |
|-------------------------------------|---------------------------------------|
| Use descriptive variable names.     | `age = 25`, `first_name = "John"`    |
| Follow snake_case for variable names.| `my_variable`, `user_name`            |
| Avoid single-character names.       | Except in loops: `for i in range(5):` |
| Use ALL_CAPS for constants.         | `PI = 3.14159`, `MAX_USERS = 100`     |

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
