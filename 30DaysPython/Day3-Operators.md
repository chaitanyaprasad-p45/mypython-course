#   Operators

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

