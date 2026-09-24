# Personal Mini-Toolkit
# A simple program containing useful tools for the user.

# This list stores tasks that the user adds to the to-do list.
tasks = []# To-Do List: lets the user view, add, and delete tasks stored in a list.
def todo_list():
    """Manage the to-do list."""
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Back to main menu")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            if tasks:
                print("\nCurrent tasks:")
                for number, item in enumerate(tasks, start=1):
                    print(f"{number}. {item}")
            else:
                print("No tasks yet.")

        elif choice == "2":
            task = input("Enter a task to add: ")

            if task.strip():
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("You entered an empty task.")

        elif choice == "3":
            if tasks:
                print("\nCurrent tasks:")
                for number, item in enumerate(tasks, start=1):
                    print(f"{number}. {item}")

                try:
                    task_number = int(input("Enter the task number to delete: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task deleted: {removed_task}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid task number.")
            else:
                print("No tasks to delete.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 4.")


# Calculator: performs addition, subtraction, multiplication, or division.
def calculator():
    """Perform a basic calculation."""
    print("\n--- Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your choice: ")

        if operation == "1":
            result = first_number + second_number
            print(f"Result: {result}")
        elif operation == "2":
            result = first_number - second_number
            print(f"Result: {result}")
        elif operation == "3":
            result = first_number * second_number
            print(f"Result: {result}")
        elif operation == "4":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                result = first_number / second_number
                print(f"Result: {result}")
        else:
            print("Invalid operation choice.")

    except ValueError:
        print("Please enter valid numbers.")





# Number Checker: determines whether a whole number is even or odd.
def number_checker():
    """Check whether a number is even or odd."""
    print("\n--- Number Checker ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Display the main menu.
def show_menu():
    """Display the main menu."""
    print("\n========== PERSONAL MINI-TOOLKIT ==========")
    print("1. Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")
    print("============================================")


# Main menu loop keeps the program running until the user chooses Quit.
print("Welcome to your Personal Mini-Toolkit!")

while True:
    show_menu()
    choice = input("Choose a tool (1-4): ")

    # Route the user's choice to the correct tool.
    if choice == "1":
        calculator()
    elif choice == "2":
        todo_list()
    elif choice == "3":
        number_checker()
    elif choice == "4":
        print("Thank you for using the Personal Mini-Toolkit. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number from 1 to 4.")






