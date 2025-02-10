##  1. Addition of Two Numbers

### Variant 1: Using User Input
```python
# This program adds two numbers provided by the user.

# Step 1: Prompt the user to enter the first number.
# The input() function returns a string, so we convert it to an integer.
num1 = int(input("Enter the first number: "))

# Step 2: Prompt the user to enter the second number.
num2 = int(input("Enter the second number: "))

# Step 3: Add the two numbers using the '+' operator.
sum_result = num1 + num2

# Step 4: Print the result with a descriptive message.
print("The sum of", num1, "and", num2, "is:", sum_result)
```
**Explanation:**

*   **Input Conversion:** The inputs are converted from strings to integers so that arithmetic operations can be performed.
*   **Addition Operation:** The + operator adds the two numbers.
*   **Output:** The result is printed clearly, showing both operands and the computed sum.

### Variant 2: Using Pre-defined Constants
```python
# This program adds two pre-defined numbers.

# Define two numbers directly in the code.
num1 = 8
num2 = 12

# Compute the sum using the '+' operator.
sum_result = num1 + num2

# Output the result.
print("The sum of", num1, "and", num2, "is:", sum_result)
```
**Explanation:**

*   **Pre-defined Values:** Instead of asking for user input, the numbers are defined within the code.
*   **Same Operation:** The addition is performed in the same way.
*   **Output:** The result is printed immediately.

##  2. Subtraction of Two Numbers
###    Variant 1: Using User Input
```python
# This program subtracts one number from another using user-provided inputs.

# Step 1: Get the first number (minuend) from the user.
minuend = int(input("Enter the number to subtract from (minuend): "))

# Step 2: Get the second number (subtrahend) from the user.
subtrahend = int(input("Enter the number to subtract (subtrahend): "))

# Step 3: Subtract the second number from the first.
difference = minuend - subtrahend

# Step 4: Display the result.
print("The result of subtracting", subtrahend, "from", minuend, "is:", difference)
```
**Explanation:**

*   **Terminology:** In subtraction, the first number is called the minuend and the second is the subtrahend.
*   **Subtraction Operation:** The - operator subtracts the subtrahend from the minuend.
*   **Output:** The computed difference is clearly printed.
### Variant 2: Using Pre-defined Constants
```python
# This program subtracts two numbers defined in the code.

# Define the numbers directly.
minuend = 20
subtrahend = 5

# Perform the subtraction.
difference = minuend - subtrahend

# Print the result.
print("The result of subtracting", subtrahend, "from", minuend, "is:", difference)
```
**Explanation:**

*   **Static Values:** The subtraction is performed using constants.
*   **Same Process:** The operation and printing are identical to the input version.
*   **Clear Output:** The result is shown with descriptive text.


##  3. Multiplication of Two Numbers
### Variant 1: Using User Input
``` python
# This program multiplies two numbers provided by the user.

# Prompt the user for the first number.
num1 = int(input("Enter the first number: "))

# Prompt the user for the second number.
num2 = int(input("Enter the second number: "))

# Multiply the numbers using the '*' operator.
product = num1 * num2

# Print the multiplication result.
print("The product of", num1, "and", num2, "is:", product)
```
**Explanation:**

*   **Input Handling**: The numbers are taken as input and converted to integers.
*   **Multiplication:** The * operator is used to compute the product.
*   **Result:** A clear print statement shows the result.
### Variant 2: Using Pre-defined Constants
```python
# This program multiplies two pre-defined numbers.

# Define two numbers.
num1 = 7
num2 = 9

# Calculate the product.
product = num1 * num2

# Display the product.
print("The product of", num1, "and", num2, "is:", product)
```
**Explanation:**

*   **Constants:** Numbers are already set in the code.
*   **Operation:** Multiplication is straightforward with the * operator.
*   **Output:** The result is printed directly.

##  4. Division of Two Numbers
### Variant 1: Using User Input
```python
# This program divides one number by another using values entered by the user.

# Prompt for the numerator (the number to be divided).
numerator = float(input("Enter the numerator: "))

# Prompt for the denominator (the number to divide by).
denominator = float(input("Enter the denominator: "))

# Check for division by zero to avoid runtime errors.
if denominator != 0:
    # Perform division using the '/' operator.
    quotient = numerator / denominator
    print("The quotient is:", quotient)
else:
    print("Error: Division by zero is not allowed.")
```
**Explanation:**

*   **Float Conversion:** Inputs are converted to floats to allow decimal results.
*   **Safety Check:** The code checks if the denominator is zero before dividing.
*   **Division:** The / operator is used to compute the quotient.
*   **Output:** The result is printed, or an error is shown if division by zero is attempted.
### Variant 2: Using Pre-defined Constants
```python
# This program divides two numbers defined in the code.

# Pre-defined numerator and denominator.
numerator = 50
denominator = 10

# Check to ensure the denominator is not zero.
if denominator != 0:
    quotient = numerator / denominator
    print("The quotient of", numerator, "divided by", denominator, "is:", quotient)
else:
    print("Error: Division by zero is not allowed.")
```
**Explanation:**
*   **Defined Values:** The numerator and denominator are pre-set.
*   **Division Operation:** The same division logic and safety check are used.
*   **Output:** The result is printed directly.
##  5. Floor Division
### Variant 1: Using User Input
```python
# This program performs floor division, which returns the largest whole number less than or equal to the quotient.

# Get the dividend (number to be divided) from the user.
dividend = int(input("Enter the dividend (number to be divided): "))

# Get the divisor from the user.
divisor = int(input("Enter the divisor (number to divide by): "))

# Ensure that the divisor is not zero.
if divisor != 0:
    # Floor division uses the '//' operator.
    floor_result = dividend // divisor
    print("The floor division result is:", floor_result)
else:
    print("Error: Division by zero is not allowed.")
```
**Explanation:**

*   **Floor Division Concept:** Unlike standard division, floor division discards any fractional part.
*   **User Input:** Values are obtained from the user.
*   **Operator:** The // operator performs the floor division.
*   **Output:** The integer quotient is printed.
### Variant 2: Using Pre-defined Constants
```python
# This program performs floor division using pre-defined numbers.

# Set the dividend and divisor.
dividend = 23
divisor = 4

# Check for a valid divisor.
if divisor != 0:
    floor_result = dividend // divisor
    print("The floor division of", dividend, "by", divisor, "is:", floor_result)
else:
    print("Error: Division by zero is not allowed.")
```
**Explanation:**

*   **Static Values:** Numbers are hard-coded.
*   **Operation:** The // operator is used as before.
*   **Output:** The floor division result is printed after ensuring safe division.
##  6. Modulus (Remainder)
### Variant 1: Using User Input
```python
# This program calculates the remainder when one number is divided by another.

# Prompt the user for the dividend.
dividend = int(input("Enter the dividend: "))

# Prompt the user for the divisor.
divisor = int(input("Enter the divisor: "))

# Check for division by zero.
if divisor != 0:
    # The '%' operator returns the remainder.
    remainder = dividend % divisor
    print("The remainder is:", remainder)
else:
    print("Error: Division by zero is not allowed.")
```
**Explanation:**

*   **Remainder Calculation:** The % operator gives the remainder after division.
*   **Input Handling:** Two numbers are taken from the user and converted to integers.
*   **Error Handling:** A check is made for division by zero.
*   **Output:** The remainder is printed clearly.
### Variant 2: Using Pre-defined Constants
```python
# This program calculates the remainder using pre-defined values.

# Define the dividend and divisor.
dividend = 29
divisor = 6

# Perform the modulus operation if the divisor is valid.
if divisor != 0:
    remainder = dividend % divisor
    print("The remainder when", dividend, "is divided by", divisor, "is:", remainder)
else:
    print("Error: Division by zero is not allowed.")
```
**Explanation:**
*   **Pre-defined Values:** The values are set in the code.
*   **Modulus Operation:** The % operator is applied.
*   **Output:** The result is printed with a descriptive message.
##  7. Exponentiation (Power)
### Variant 1: Using User Input
```python
# This program calculates the power of a number based on user inputs.

# Prompt the user for the base.
base = float(input("Enter the base number: "))

# Prompt the user for the exponent.
exponent = float(input("Enter the exponent: "))

# Use the '**' operator to raise the base to the power of the exponent.
power_result = base ** exponent

# Print the result using an f-string for formatting.
print(f"{base} raised to the power of {exponent} is: {power_result}")
```
**Explanation:**

*   **User Inputs:** The base and exponent are taken as inputs and converted to floats.
*   **Exponentiation:** The ** operator calculates the power.
*   **Output:** A formatted string prints the result clearly.
### Variant 2: Using Pre-defined Constants
```python
# This program calculates the power using pre-defined values.

# Define the base and exponent.
base = 3
exponent = 4

# Compute the power.
power_result = base ** exponent

# Display the result.
print(f"{base} raised to the power of {exponent} is: {power_result}")
```
**Explanation:**
*   **Static Values:** The base and exponent are set in the code.
*   **Operation:** The ** operator is used just as in the interactive version.
*   **Output:** The result is printed immediately.
##  8. Calculating the Average of Three Numbers
### Variant 1: Using User Input
```python
# This program calculates the average of three numbers provided by the user.

# Prompt the user for three numbers and convert them to floats.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the average by summing the numbers and dividing by 3.
average = (num1 + num2 + num3) / 3

# Print the result.
print("The average of the three numbers is:", average)
```
**Explanation:**

*   **Input Conversion:** Numbers are converted to floats to allow for decimal values.
*   **Calculation:** The average is computed by adding the numbers and dividing by the count.
*   **Output:** The computed average is displayed clearly.
### Variant 2: Using Pre-defined Constants
```python
# This program calculates the average of three pre-defined numbers.

# Define three numbers.
num1 = 12
num2 = 18
num3 = 24

# Compute the average.
average = (num1 + num2 + num3) / 3

# Output the result.
print("The average of", num1, ",", num2, "and", num3, "is:", average)
```
**Explanation:**

*   **Static Values:** The numbers are already provided.
*   **Calculation:** The arithmetic average is computed in the same way.
*   **Output:** The average is printed with context.
##  9. Converting Celsius to Fahrenheit
### Variant 1: Using User Input
```python
# This program converts a temperature from Celsius to Fahrenheit.

# Prompt the user for a temperature in Celsius.
celsius = float(input("Enter temperature in Celsius: "))

# Use the conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Print the result in a formatted string.
print(f"{celsius}°C is equal to {fahrenheit}°F")
```
**Explanation:**

*   **Input:** The Celsius temperature is taken as a float.
*   **Conversion Formula:** The formula (C * 9/5) + 32 converts Celsius to Fahrenheit.
*   **Output:** The converted temperature is displayed.
### Variant 2: Using Pre-defined Constants
```python
# This program converts a pre-defined Celsius temperature to Fahrenheit.

# Define a Celsius temperature.
celsius = 30

# Apply the conversion formula.
fahrenheit = (celsius * 9/5) + 32

# Display the result.
print(f"{celsius}°C is equal to {fahrenheit}°F")
```
**Explanation:**

*   **Static Value:** The Celsius temperature is set in the code.
*   **Conversion:** The same formula is used to compute the Fahrenheit temperature.
*   **Output:** The result is printed clearly.
##  10. Calculating Simple Interest
### Variant 1: Using User Input
```python
# This program calculates the simple interest based on user inputs.

# Prompt the user for the principal amount, rate of interest, and time period.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Use the simple interest formula: SI = (Principal * Rate * Time) / 100
simple_interest = (principal * rate * time) / 100

# Print the computed simple interest.
print("The simple interest is:", simple_interest)
```
**Explanation:**

*   **User Inputs:** The principal, rate, and time are input by the user.
*   **Calculation:** The formula (P * R * T) / 100 computes the simple interest.
*   **Output:** The simple interest is printed with context.
### Variant 2: Using Pre-defined Constants
```python
# This program calculates simple interest using pre-defined values.

# Define the principal, rate of interest, and time period.
principal = 1000  # e.g., in dollars or any currency
rate = 5          # e.g., 5%
time = 3          # e.g., 3 years

# Calculate the simple interest.
simple_interest = (principal * rate * time) / 100

# Print the result with a detailed message.
print("The simple interest for a principal of", principal, "at a rate of", rate, 
      "% for", time, "years is:", simple_interest)
```
**Explanation:**

*   **Static Values:** The principal, rate, and time are already defined.
*   **Operation:** The simple interest formula is applied directly.
*   **Output:** The computed interest is printed clearly.