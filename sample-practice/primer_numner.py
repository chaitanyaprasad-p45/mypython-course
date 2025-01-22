def is_prime(number):
    if number < 2:  # Prime numbers are greater than 1
        return False
    for i in range(2, int(number ** 0.5) + 1):  # Check divisors up to √number
        if number % i == 0:  # If divisible, it's not a prime
            return False
    return True

def prime_number_checker():
    try:
        num = int(input("Enter a number to check if it's prime: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Run the checker
prime_number_checker()



'''
Logic Explanation:
Prime Number Definition:

A prime number is a natural number greater than 1 that has no divisors other than 1 and itself.
Prime Checking Function:

The is_prime() function:
Returns False for numbers less than 2.
Loops from 2 to the square root of the number (int(number ** 0.5) + 1).
If the number is divisible by any of these, it's not a prime number.
Input and Validation:

Takes a number from the user, converts it to an integer, and checks its primality.
Handles invalid inputs using try-except.
Output Result:

If the number is prime, the program outputs that it’s a prime number; otherwise, it says it isn’t.
Syntax Explanation:
number ** 0.5:
Calculates the square root of the number using exponentiation.

int():
Converts a floating-point result to an integer.

range(2, int(number ** 0.5) + 1):
Loops from 2 up to (but not including) the square root of the number + 1.

number % i:
Checks if number is divisible by i. If the remainder is 0, number is not a prime.

How to Test This Script:
Run the program.
Input a number and check if it is prime.
Enter invalid inputs (e.g., letters) to test error handling.
'''