def reverse_string():
    string = input("ENter a String in Reverse: ")
    reversed_string = string[::-1] # Reverse the String using slicing
    print(f"The reversed string is: {reversed_string}")

# Run the FUnction
reverse_string()



'''
Logic Explanation:
String Slicing:

Strings in Python can be sliced using start:end:step.
Using [::-1] means:
Start from the end.
Move backward (step -1).
Stop at the beginning.
Reverse Logic:

The slicing operation creates a reversed version of the string.
Output:

The reversed string is printed.
Syntax Explanation:
[::-1]:
Slicing syntax to reverse the string.

input():
Takes input from the user.

print():
Displays the reversed string.

How to Test This Script:
Run the program.
Enter a string.
Verify the reversed string is correct.
'''