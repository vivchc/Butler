import TaskAppDriver

"""Runs the main application."""

driver = TaskAppDriver.TaskAppDriver()  # calls driver class
print("Type 'help' for to see cmds.")


def ask_user():
    """Gets user input and executes corresponding action."""
    while True:
        user_input = input("Enter input: ")

        if user_input.lower() == "quit" or user_input.lower() == "q":
            driver.close_file()
            exit()
        elif user_input.lower() == "help":
            help_key()
        elif user_input.lower().startswith("add"):
            add_tasks(user_input)
        elif user_input.lower().startswith("rm"):
            remove_tasks(user_input)
        elif user_input.lower().startswith("edit"):
            edit_tasks(user_input)
        elif user_input.lower() == "show":
            show_tasks()
        elif user_input.lower() == "clc":
            clear_tasks()


def help_key():
    """String representating help menu."""
    key = """
    Add task: add <task>
    Edit task: edit <task #>
    Remove task: rm <task #>
    Clear all tasks: clc
    Show tasks: show
    Show help key: help
    Exit app: quit or q
    """
    print(key)


def clear_tasks():
    """Clear tasks and handles errors."""
    try:
        driver.clear_file()
        print("Cleared all tasks!")
    except FileNotFoundError:
        print("Already clear!")


def show_tasks():
    """Show tasks and handle errors."""
    error_msg = "No tasks to show."
    try:
        if driver.total_num_of_tasks() == 0:
            print(error_msg)
        else:
            driver.show_tasks()
    except FileNotFoundError:
        print(error_msg)


def add_tasks(user_input):
    """Adds a new task."""
    driver.add_task(user_input.split()[1])  # Leave "add" cmd out
    print("Added")


def remove_tasks(user_input):
    """Removes a task. Prints message stating (un)successful."""
    input = user_input.split()[1]  # Leave "rm" cmd out
    if driver.remove_task(input):
        print("Removed")
    else:
        print("Task not found.")


def edit_tasks(user_input):
    """Lets user edit task. Prints message stating (un)successful."""
    input = user_input.split()[1]  # Leave "edit" cmd out
    if driver.edit_task(input):
        print("Edited")
    else:
        print("Task not found.")


ask_user()
