# Python Course:

## Topics:
* **[Python Syntax](#python-syntax):** Write and execute Python code in the command line or .py files.
* **[Indentation](#python-indentation):** Python uses indentation to define blocks of code.
* **[Comments](#introduction-to-python-comments):** Use # for single-line and triple quotes for multi-line comments.
* **[Variables](#introduction-to-python-variables):** Dynamically typed, case-sensitive, and follow naming rules.
    * **[Output Variables](#python---output-variables):** Use print() and f-strings for formatted output.
    * **[Global Variables](#python---global-variables):** Use the global keyword to modify variables globally.
    * **[Dynamic Typing](#dynamic-typing-in-python):** Python automatically determines variable types at runtime.
* **[DataTypes](#python-data-types):** Variables can store data of different types, and different types can do different things..

## Python Syntax
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

Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.

**Proper Indentation**   
```python
if 5 > 2:
    print("Five is greater than two!")
``` 
**Missing Indentation**  
```python
if 5 > 2:
print("Five is greater than two!")
``` 

> **Note:** Python will raise an `IndentationError` if indentation is skipped:
---
## Introduction to Python Comments

- Comments can be used to explain Python code.
- Comments can be used to make the code more readable.
- Comments can be used to prevent execution when testing code.

| **Concept**              | **Syntax Example**                                       |
|--------------------------|---------------------------------------------------------|
| **Single-line Comment**  | `# This is a comment`                                   |
| **Multi-line Comment**   | `"""This is a multi-line comment"""`                  |

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
| Must begin with a letter (a-z, A-Z) or an underscore (`_`).              | Valid: `my_variable`, `_variable`   <br>  Invalid: `1variable`, `#var`  |
| Can only contain alphanumeric characters and underscores.                | Valid: `my_var`, `var123` <br>   Invalid: `my-var`, `var@name`            |
| Cannot be a reserved keyword.                                            | Reserved keywords: `if`, `else`, etc.  |
| Case-sensitive.                                                          | `MyVar`, `myvar`, and `MYVAR` differ.  |

---

## Multi Words Variable Names
| **Case**                              |   **Example**                             |   **Description**                                         |
|---------------------------------------|-------------------------------------------|-----------------------------------------------------------|
|Camel Case                             |`myVariableName` = "John"                    |Each word, except the first, starts with a capital letter  |
|Pascal Case                            |`MyVariableName` = "John"                    |Each word starts with a capital letter                     |
|Snake Case                             |`my_variable_name` = "John"                  |Each word is separated by an underscore character          |


## Variable Types in Python

Python is dynamically typed, meaning you don't need to declare the type of a variable. It is inferred at runtime.

### Examples of Variable Assignments:

| **Type**       | **Example**                  | **Use Case**                                                                 | **Sample**                       |
|----------------|------------------------------|-------------------------------------------------------------------------------|-----------------------------------|
| **Integer**    | `x = 10`                     | Representing quantities, such as `age = 25` or `number_of_items = 100`.       | `x + 5` for calculations         |
| **Float**      | `y = 3.14`                   | Handling measurements like `temperature = 36.6` or calculations like `area`. | `y * 2` for scaling values       |
| **String**     | `name = "Alice"`            | Storing text data, such as `message = "Hello, World!"` or `filename = "data.txt"`. | Concatenating `name + " Doe"`    |
| **Boolean**    | `is_active = True`           | Representing states, e.g., `is_logged_in = False` or toggles like `feature_enabled`. | Conditional checks: `if is_active:` |
| **List**       | `numbers = [1, 2, 3]`        | Managing collections, e.g., `shopping_list = ["milk", "eggs", "bread"]`.     | Iterating: `for num in numbers:` |
| **Dictionary** | `data = {"key": "value"}` | Storing mappings, such as `user = {"name": "Alice", "age": 30}` or configurations. | Accessing: `data["key"]`       |

---

## Assign Multiple Values

Python allows you to assign values to multiple variables in one line:

| Multiple Variables                         | One Value to Multiple Variables         | Unpack a Collection                      |
|--------------------------------------------|-----------------------------------------|------------------------------------------|
| x, y, z = "Orange", "Banana", "Cherry"     | x = y = z = "Orange"                    | fruits = ["apple", "banana", "cherry"]   |
| print(x)                                   | print(x)                                | x, y, z = fruits                         |
| print(y)                                   | print(y)                                | print(x)                                 |
| print(z)                                   | print(z)                                | print(y)                                 |
|                                            |                                         | print(z)                                 |


## Python - Output Variables

In Python, you can display the values of variables using the `print()` function. 

**Basic Usage:**

```python
x = 5
y = "Hello, World!"
z = True
print(x)  # Output: 5
print(y)  # Output: Hello, World!
print(z)  # Output: True
```
**Multiple Variables:**

You can print multiple variables in a single line using commas to separate them:
```python
name = "Alice"
age = 30
print("Name:", name, "Age:", age) 
# Output: Name: Alice Age: 30
```

**Formatted Output:**

For more control over the output format, use f-strings (formatted string literals):
```python
temperature = 25.5
print(f"The current temperature is {temperature:.2f} degrees Celsius.")
# Output: The current temperature is 25.50 degrees Celsius.
```

## Python - Global Variables

**Global Variables** in Python are variables that are defined outside of any function. They can be accessed from anywhere within the program, including inside functions.

**Key Concepts:**

* **Scope:** Global variables have global scope, meaning they are accessible throughout the entire program.
* **Modification:** 
    * To modify a global variable within a function, you must use the `global` keyword within the function.
    * If you don't use `global`, the variable will be treated as a local variable within the function, and any changes made will not affect the global variable.

**Example:**

```python
# Global variable
count = 0

def increment():
    global count  # Declare count as global within the function
    count += 1

increment()
print(count)  # Output: 1
```
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
```python
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
```
## Dynamic Typing in Python

**Dynamic Typing** is a core feature of the Python programming language. It means that you don't need to explicitly declare the data type of a variable before assigning a value to it. Python automatically determines the data type at runtime based on the assigned value.

**Key Characteristics:**

* **Flexibility:** This flexibility allows for rapid development and experimentation, as you don't need to worry about type declarations.
* **Implicit Type Conversion:** Python can often implicitly convert data types when necessary, such as converting an integer to a float in arithmetic operations.
* **Duck Typing:** Python emphasizes "duck typing," which means that if an object "quacks like a duck," it's treated as a duck. In other words, the focus is on the object's behavior rather than its specific type.

**Example:**

```python
x = 5       # x is an integer
x = "Hello"  # x is now a string
x = True     # x is now a boolean

print(type(x))  # Output: <class 'bool'>
```

> **Tip:** This flexibility can be powerful, but it is essential to use type-checking (`type()` function) when working with complex codebases.
---

# Python Data Types

Python provides several built-in data types that allow developers to store and manipulate different kinds of data effectively. Below is an overview of Python's fundamental data types.

| **Category**        | **Type**        | **Description**           | **Example**                                  |
|---------------------|-----------------|---------------------------|----------------------------------------------|
| **Numeric Types**   | `int`          | Represents whole numbers (positive, negative, or zero).            | x = 10 <br> y = -5 <br> z = 0                                                 |
|                     | `float`        | Represents decimal numbers.                                        | x = 3.14 <br> y = -2.71                                                       |
|                     | `complex`      | Represents complex numbers with real and imaginary parts.          | z = 3 + 4j <br> print(z.real)  # Output: 3.0 <br> print(z.imag)  # Output: 4.0|
| **Sequence Types**  | `str` (String) | Represents a sequence of characters. Strings are immutable.        | name = "Alice" <br> greeting = 'Hello, World!'                                |
|                     | `list`         | Represents an ordered, mutable collection of items.                | numbers = [1, 2, 3, 4] <br> mixed = [1, "hello", 3.14]                        |
|                     | `tuple`        | Represents an ordered, immutable collection of items.              | coordinates = (10, 20) <br> names = ("Alice", "Bob")                          |
|                     | `range`     | Represents an immutable sequence of numbers, typically used in loops. | for i in range(5): <br> print(i)  # Outputs 0, 1, 2, 3, 4                     |
| **Set Types**       | `set`          | Represents an unordered collection of unique items.                | fruits = {"apple", "banana", "cherry"}                                        |
|                     | `frozenset`    | Immutable version of a set.                                        | frozen_fruits = frozenset(["apple", "banana", "cherry"])                      |
| **Mapping Type**    | `dict`         | Represents a collection of key-value pairs.                        | student = {"name": "Alice", "age": 20}                                        |
| **Boolean Type**    | `bool`         | Represents `True` or `False` values.                               | is_active = True <br> is_admin = False                                        |
| **Binary Types**    | `bytes`        | Represents immutable sequences of bytes.                           | data = b"hello"                                                               |
|                     | `bytearray`    | Represents mutable sequences of bytes.                             | data = bytearray(b"hello") <br> data[0] = 104  # Modifies the first byte      |
|                     | `memoryview`   | Provides a memory view of a bytes object.                          | data = memoryview(b"hello")                                                   |
| **None Type**       | `NoneType`     | Represents the absence of a value.                                 | result = None                                                                 |

## Type Checking
- Use the `type()` function to check the type of a variable.
  ```python
  x = 10
  print(type(x))  # Output: <class 'int'>
  ```

- Use `isinstance()` to check if an object belongs to a specific type.
  ```python
  x = 10
  print(isinstance(x, int))  # Output: True
  ```
---