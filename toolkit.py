# Personal Mini-Toolkit
# A simple program containing useful tools for the user.

# This list stores tasks that the user adds to the to-do list.
tasks = []


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


def todo_list():
    """Add and display tasks."""
    print("\n--- To-Do List ---")

    task = input("Enter a task to add: ")

    if task.strip():
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("You entered an empty task.")

    print("\nCurrent tasks:")

    if tasks:
        for number, item in enumerate(tasks, start=1):
            print(f"{number}. {item}")
    else:
        print("No tasks yet.")


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
