def fizzbuzz():
    try:
        num = int(input("Enter a number to play FizzBuzz up to: "))
        for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
            if i % 3 == 0 and i % 5 == 0:  # Divisible by both 3 and 5
                print("FizzBuzz")
            elif i % 3 == 0:  # Divisible by 3
                print("Fizz")
            elif i % 5 == 0:  # Divisible by 5
                print("Buzz")
            else:  # Not divisible by 3 or 5
                print(i)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Run the game
fizzbuzz()



'''
Logic Explanation:
FizzBuzz Rules:

If a number is divisible by 3 and 5, print "FizzBuzz".
If divisible by 3, print "Fizz".
If divisible by 5, print "Buzz".
Otherwise, print the number.
For Loop:

Loops through all numbers from 1 to the user-defined limit.
Conditional Logic:

The if, elif, and else statements check divisibility and print the corresponding result.
Input Validation:

Ensures that the input is an integer and handles invalid inputs using a try-except block.

Syntax Explanation:
for i in range(1, num + 1):
Loops from 1 to num (inclusive).

i % 3 == 0:
Checks if i is divisible by 3 (remainder is 0).

if, elif, else:
Conditional statements to handle multiple conditions.

print():
Outputs the result for each number.

How to Test This Script:
Run the program.
Enter a positive integer to play FizzBuzz.
Observe the output for numbers divisible by 3, 5, and both.
'''