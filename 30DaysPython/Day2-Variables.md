#   Variables

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
