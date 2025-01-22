def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

def factorial_calculator():
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is {result}.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Run the calculator
factorial_calculator()



'''
Logic Explanation:
Factorial Definition:

The factorial of n is the product of all positive integers less than or equal to n.
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120.
Recursive Function:

The factorial() function uses recursion:
Base case: If n is 0 or 1, return 1.
Recursive step: Multiply n by factorial(n - 1).
Input Validation:

Accepts a number from the user and ensures it’s non-negative.
Handles invalid inputs using try-except.
Output Result:

Displays the factorial of the number if valid.
Syntax Explanation:
if n == 0 or n == 1:
Checks if n is 0 or 1 and returns 1 (base case).

return n * factorial(n - 1):
Recursive call to compute the factorial of n - 1.

int(input()):
Converts user input (string) to an integer.

How to Test This Script:
Run the program.
Enter positive numbers to calculate factorials.
Try entering negative numbers or invalid inputs to test error handling.
'''