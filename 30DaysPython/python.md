##	Built in functions
*	In Python we have lots of built-in functions. Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring. Some of the most commonly used Python built-in functions are the following: print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir(). In the following table you will see an exhaustive list of Python built-in functions taken from python documentation. https://docs.python.org/3.9/library/functions.html

##  Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

Python Variable Name Rules

*   A variable name must start with a letter or the underscore character
*   A variable name cannot start with a number
*   A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
*   Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

## Variable Names

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
---

When we assign a certain data type to a variable, it is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable. The equal sign in Python is not equality as in Mathematics.

```python
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Chaitanya',
   'lastname':'Prasad',
   'country':'India',
   'city':'Bangalore'
   }
```
---
Let us use the print() and len() built-in functions. Print function takes unlimited number of arguments. An argument is a value which we can be passed or put inside the function parenthesis, see the example below.
```python
print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument
```
---
### Declaring Multiple Variable in a Line

Multiple variables can also be declared in one line:

```python
first_name, last_name, country, age, is_married = 'Chaitanya', 'Prasad', 'India', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```
Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables.
```python
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```
---
##  Data Types

There are several data types in Python. To identify the data type we use the type built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.

##  Checking Data types and Casting
```python
# Different python data types
# Let's declare variables with various data types

first_name = 'Chaitanya'    # str
last_name = 'Prasad'        # str
country = 'India'           # str
city= 'Bangalore'           # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('chaitanya'))                    # str
print(type(first_name))                     # str
print(type(10))                             # int
print(type(3.14))                           # float
print(type(1 + 1j))                         # complex
print(type(True))                           # bool
print(type([1, 2, 3, 4]))                   # list
print(type(("apple", "banana", "cherry")))  # list
print(type({'name':'chaitanya'}))           # dict
print(type((1,2)))                          # tuple
print(type(zip([1,2],[3,4])))               # zip
```
**Casting:** Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

```python
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Chaitanya'
print(first_name)               # 'Chaitanya'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['C', 'h', 'a', 'i', 't', 'a', 'n', 'y', 'a']
```
---
### Numbers
Number data types in Python:

*   Integers: Integer(negative, zero and positive) numbers 
    *   Example: ... -3, -2, -1, 0, 1, 2, 3 ...
*   Floating Point Numbers(Decimal numbers) 
    *   Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
*   Complex Numbers 
    *   Example: 1 + j, 2 + 4j, 1 - 1j
---

##  Boolean
A boolean data type represents one of the two values: True or False. The use of these data types will be clear once we start using the comparison operator. The first letter T for True and F for False should be capital unlike JavaScript.
```python
print(True)
print(False)
```

##  Operators

Python language supports several types of operators. In this section, we will focus on few of them.


### Arithmetic Operators:
| Operator | Name           | Example     | Explanation & Usage |
|----------|---------------|------------|---------------------|
| +        | Addition       | 5 + 3 = 8  | Adds two numbers. Example: `x = 5 + 3` results in `x = 8`. Used for arithmetic operations. |
| -        | Subtraction    | 10 - 4 = 6 | Subtracts right operand from the left. Example: `x = 10 - 4` results in `x = 6`. Used to decrease values. |
| *        | Multiplication | 6 * 2 = 12 | Multiplies two numbers. Example: `x = 6 * 2` results in `x = 12`. Used for scaling values. |
| /        | Division       | 9 / 2 = 4.5| Divides left operand by right. Example: `x = 9 / 2` results in `x = 4.5`. Always returns a float. |
| %        | Modulus        | 10 % 3 = 1 | Returns the remainder of division. Example: `x = 10 % 3` results in `x = 1`. Used for even/odd checks or cyclic operations. |
| **       | Exponentiation | 2 ** 3 = 8 | Raises left operand to power of right. Example: `x = 2 ** 3` results in `x = 8`. Used for powers or exponential calculations. |
| //       | Floor Division | 9 // 2 = 4 | Divides and rounds down to nearest integer. Example: `x = 9 // 2` results in `x = 4`. Used for integer-only results. |


---

### Assignment Operators

Assignment operators are used to assign values to variables. Let us take = as an example. Equal sign in mathematics shows that two values are equal, however in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable.

| Operator | Example    | Same As       | Explanation & Usage |
|----------|------------|--------------|---------------------|
| `=`      | `x = 5`    | `x = 5`      | Assigns the value `5` to `x`. Example: `x = 5` |
| `+=`     | `x += 3`   | `x = x + 3`  | Adds `3` to `x` and assigns the result back to `x`. Example: `x = 5; x += 3  # x becomes 8` |
| `-=`     | `x -= 3`   | `x = x - 3`  | Subtracts `3` from `x` and assigns the result back to `x`. Example: `x = 10; x -= 3  # x becomes 7` |
| `*=`     | `x *= 3`   | `x = x * 3`  | Multiplies `x` by `3` and assigns the result back to `x`. Example: `x = 4; x *= 3  # x becomes 12` |
| `/=`     | `x /= 3`   | `x = x / 3`  | Divides `x` by `3` and assigns the result back to `x`. Example: `x = 9; x /= 3  # x becomes 3.0` |
| `%=`     | `x %= 3`   | `x = x % 3`  | Assigns the remainder of `x` divided by `3` to `x`. Example: `x = 10; x %= 3  # x becomes 1` |
| `//=`    | `x //= 3`  | `x = x // 3` | Performs floor division and assigns the result back to `x`. Example: `x = 10; x //= 3  # x becomes 3` |
| `**=`    | `x **= 3`  | `x = x ** 3` | Raises `x` to the power of `3` and assigns the result. Example: `x = 2; x **= 3  # x becomes 8` |
| `&=`     | `x &= 3`   | `x = x & 3`  | Performs bitwise AND and assigns the result. Example: `x = 5; x &= 3  # x becomes 1` |
| `|=`     | `x |= 3`   | `x = x | 3`  | Performs bitwise OR and assigns the result. Example: `x = 5; x |= 3  # x becomes 7` |
| `^=`     | `x ^= 3`   | `x = x ^ 3`  | Performs bitwise XOR and assigns the result. Example: `x = 5; x ^= 3  # x becomes 6` |
| `>>=`    | `x >>= 3`  | `x = x >> 3` | Shifts bits of `x` right by `3` places. Example: `x = 8; x >>= 3  # x becomes 1` |
| `<<=`    | `x <<= 3`  | `x = x << 3` | Shifts bits of `x` left by `3` places. Example: `x = 2; x <<= 3  # x becomes 16` |
| `:=`     | `print(x := 3)` | `x = 3; print(x)` | Walrus operator: assigns `3` to `x` inside `print()`. Example: `print(x := 5)  # prints 5 and assigns 5 to x` |

## Additional Notes:
- The `:=` operator (Walrus operator) is useful for assignments within expressions like loops and conditionals.
- Bitwise operators (`&=, |=, ^=, >>=, <<=`) are mostly used for low-level programming or working with binary data.
---

##  Comparison Operators

In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. 

| Operator | Name                        | Example   | Explanation & Usage |
|----------|-----------------------------|-----------|---------------------|
| `==`     | Equal to                    | `x == y`  | Returns `True` if `x` is equal to `y`, otherwise `False`. Example: `5 == 5  # True` |
| `!=`     | Not equal to                | `x != y`  | Returns `True` if `x` is not equal to `y`. Example: `5 != 3  # True` |
| `>`      | Greater than                | `x > y`   | Returns `True` if `x` is greater than `y`. Example: `5 > 3  # True` |
| `<`      | Less than                   | `x < y`   | Returns `True` if `x` is less than `y`. Example: `3 < 5  # True` |
| `>=`     | Greater than or equal to    | `x >= y`  | Returns `True` if `x` is greater than or equal to `y`. Example: `5 >= 5  # True` |
| `<=`     | Less than or equal to       | `x <= y`  | Returns `True` if `x` is less than or equal to `y`. Example: `3 <= 5  # True` |

## Additional Notes:
- These operators are commonly used in conditional statements, loops, and logical expressions.
- The result of a comparison operation is always a Boolean value (`True` or `False`).
- Example usage in an `if` statement:
---


| Operator | Description                                | Example                          | Explanation & Usage |
|----------|--------------------------------------------|----------------------------------|---------------------|
| `and`    | Returns `True` if both conditions are `True` | `x < 5 and x < 10`               | Evaluates both conditions; returns `True` only if both are `True`. Example: `x = 3; x < 5 and x < 10  # True` |
| `or`     | Returns `True` if at least one condition is `True` | `x < 5 or x < 4`                 | Evaluates both conditions; returns `True` if at least one is `True`. Example: `x = 3; x < 5 or x < 2  # True` |
| `not`    | Reverses the result; returns `False` if the condition is `True` | `not(x < 5 and x < 10)`          | If the condition is `True`, `not` makes it `False`, and vice versa. Example: `x = 3; not(x < 5 and x < 10)  # False` |

## Logical Operators

Unlike other programming languages python uses keywords and, or and not for logical operators. Logical operators are used to combine conditional statements:

| Operator | Description                                | Example                          | Explanation & Usage |
|----------|--------------------------------------------|----------------------------------|---------------------|
| `and`    | Returns `True` if both conditions are `True` | `x < 5 and x < 10`               | Evaluates both conditions; returns `True` only if both are `True`. Example: `x = 3; x < 5 and x < 10  # True` |
| `or`     | Returns `True` if at least one condition is `True` | `x < 5 or x < 4`                 | Evaluates both conditions; returns `True` if at least one is `True`. Example: `x = 3; x < 5 or x < 2  # True` |
| `not`    | Reverses the result; returns `False` if the condition is `True` | `not(x < 5 and x < 10)`          | If the condition is `True`, `not` makes it `False`, and vice versa. Example: `x = 3; not(x < 5 and x < 10)  # False` |

---
