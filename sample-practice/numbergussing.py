import random

def number_gussing_game():
    # Generate a random numer between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Gussing Gane!")
    print("I have seleted a number between 1 and 100. Can You Guess IT?")

    while True:
        try:
            # Get the Users Guss
            guess = int(input("Enter Your Guess: "))
            attempts += 1 # increase attenps with each guess

            if guess < random_number:
                print("Too Low! Try Again.")
            elif guess > random_number:
                print("Too High! Try Again.")
            else:
                print(f"Congratulations! You Guessed the Number in {attempts} attempts. ")
                break # Exit the Loop when the guess is correct
        except ValueError:
            print("Invalid Input! Please Enter a Number.")

# Run the Game
number_gussing_game()

'''
Logic Explanation:
Generate a Random Number:

The random.randint(1, 100) function generates a random integer between 1 and 100 (inclusive).
This is the target number the user will try to guess.
Infinite Loop for User Guesses:

The while True loop runs indefinitely until the correct guess is made.
Each iteration asks the user for input.
User Input Validation:

The try-except block ensures the program doesn’t crash if the user enters invalid input (e.g., a letter instead of a number).
Conditions for Feedback:

If the guess is less than the random number, the program prints "Too low!"
If the guess is greater than the random number, the program prints "Too high!"
If the guess is correct, it congratulates the user and breaks out of the loop.
Track Attempts:

A counter (attempts) tracks the number of guesses the user makes.
Syntax Explanation:
import random:
This imports the random library, which provides functions to generate random numbers.

random.randint(a, b):
Returns a random integer between a and b, inclusive.

while True:
Creates an infinite loop that runs until explicitly stopped (e.g., break statement).

try-except block:
Handles exceptions. In this case, it ensures the program doesn’t crash if the user enters non-numeric input.

input("Enter your guess: "):
Prompts the user to enter a value. The input is a string, so it is converted to an integer with int().

How to Test This Script:
Run the script.
Enter guesses as prompted.
Observe the feedback and the number of attempts it takes to guess the number.
'''