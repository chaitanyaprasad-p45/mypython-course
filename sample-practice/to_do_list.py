def to_do_list():
    tasks = []  # Initialize an empty list to store tasks

    while True:
        print("\nTo-Do List Options:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':  # View tasks
            if not tasks:  # Check if the list is empty
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == '2':  # Add a task
            task = input("Enter the task to add: ")
            tasks.append(task)  # Append the task to the list
            print(f"'{task}' has been added to your to-do list.")
        elif choice == '3':  # Remove a task
            if not tasks:
                print("Your to-do list is empty. Nothing to remove.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"'{removed_task}' has been removed from your to-do list.")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
to_do_list()


'''
Logic Explanation:
Define a List to Store Tasks:

tasks = [] initializes an empty list to store the tasks added by the user.
Menu Display and Input:

The program repeatedly shows a menu of options using a while True loop.
The user selects an option by entering a number.
Option Logic:

Option 1 (View Tasks):
Checks if the list is empty using if not tasks. If empty, it informs the user.
If not, it enumerates the tasks using enumerate() to display them with numbers.
Option 2 (Add Task):
Prompts the user to input a task and appends it to the tasks list using tasks.append(task).
Option 3 (Remove Task):
If the list is empty, informs the user. Otherwise, it displays tasks with numbers and allows the user to remove one using pop().
Option 4 (Exit):
Exits the loop using break.
Input Validation:

Ensures the user enters valid task numbers and handles non-numeric input using try-except.
Syntax Explanation:
tasks = []:
Initializes an empty list to store user tasks.

while True:
Runs the menu indefinitely until the user chooses to exit.

input():
Reads user input as a string.

if choice == '1':
Checks the user's choice and executes the corresponding block of code.

tasks.append(task):
Adds a new task to the list.

enumerate(tasks, 1):
Loops over the tasks list and pairs each task with a number starting from 1.

tasks.pop(task_num - 1):
Removes a task based on the user-provided index.

How to Test This Script:
Run the script.
Add, view, and remove tasks.
Exit the program using option 4.
'''