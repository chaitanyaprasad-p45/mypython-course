def fibonacci_sequence():
    try:
        n = int(input("Enter the number of terms in the Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fib_sequence = [0, 1]  # Start the sequence with 0 and 1
            for _ in range(2, n):  # Generate the sequence up to n terms
                next_term = fib_sequence[-1] + fib_sequence[-2]
                fib_sequence.append(next_term)
            print(f"The first {n} terms of the Fibonacci sequence are:")
            print(fib_sequence[:n])
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Run the generator
fibonacci_sequence()


'''
Logic Explanation:
Fibonacci Sequence Definition:

Each number is the sum of the two preceding ones.
Starts with 0 and 1.
Generate Terms:

Append each new term (fib_sequence[-1] + fib_sequence[-2]) to the list.
Input Validation:

Ensures the number of terms (n) is a positive integer.
Output:

Prints the first n terms of the sequence.
Syntax Explanation:
fib_sequence = [0, 1]:
Initializes the sequence with the first two terms.

fib_sequence[-1]:
Accesses the last term in the list.

fib_sequence.append(next_term):
Adds the next term to the sequence.

How to Test This Script:
Run the program.
Enter a positive integer for the number of terms.
Verify the generated sequence matches the Fibonacci definition.
'''