def calculator():
    print("Select Operation:")
    print("1. Addition (+)")
    print("2. Subtaction (-)")
    print("3. Multipication (*)")
    print("4. Division (/)")

    # Get User Inputs For the Operaton
    operation = input("Enter the Operation Number you wante to perform (1 or 2 or 3 or 4): ")

    # Ensure User is seleted the valid Option
    if operation not in ["1", "2", "3", "4"]:
        print("Invalid Option! Please Select the Valid Option.")
        return
    
    # Get the Inputs from the User
    try:
        num1= float(input("Enter the First Number: "))
        num2= float(input("Enter trhe Second Number: "))
    except ValueError:
        print("Invalid Input! Please Enter the Number")
        return
    
    # Calaculate the Choosen Operation
    if operation == "1":
        result = num1 + num2
        print(f"The results of {num1} + {num2} is {result}.")
    elif operation == "2":
        result = num1 - num2
        print(f"The Resulats of {num1} - {num2} is {result}.")
    elif operation == "3":
        result = num1 * num2
        print(f"The Result of {num1} * {num2} is {result}.")
    elif operation == "4":
        if num2 == 0: #Handle division by zero
            print("Division By Zero is Not Allowed")
            return
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}.")  

# Run thr Calculator
calculator()





'''
Logic Explanation:
Menu Display:
The program starts by showing a menu of operations (Addition, Subtraction, Multiplication, Division). This helps the user select the desired operation.

User Input Validation for Operation:
The input() function takes the user's choice. If the input is not one of the valid options (1, 2, 3, 4), the program prints an error message and exits.

Get Numeric Inputs:
The program prompts the user to enter two numbers. To handle invalid inputs (e.g., entering letters), the try-except block ensures the program doesn't crash and provides an error message instead.

Perform Operations:
Based on the user's choice:

Addition (+): Adds num1 and num2.
Subtraction (-): Subtracts num2 from num1.
Multiplication (*): Multiplies num1 and num2.
Division (/): Divides num1 by num2. It also checks if num2 is zero to prevent a runtime error.
Result Display:
The program displays the result of the operation in a user-friendly format, showing the operands and the operation performed.
'''