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
        elif user_input.lower() == "show":
            driver.show_all_tasks()
        elif user_input.lower() == "help":
            help_key()
        elif user_input.lower() == "clear":
            try:
                driver.clear_file()
                print("Cleared all tasks!")
            except FileNotFoundError:
                print("Already clear!")
        elif user_input.lower().startswith("add"):
            driver.add_task(user_input.split()[1])  # Leave "add" cmd out
            print("Added")
        elif user_input.lower().startswith("edit"):
            driver.edit_task(user_input.split()[1])  # Leave "edit" cmd out
            print("Edited")
        elif user_input.lower().startswith("rm"):
            driver.remove_task(user_input.split()[1])  # Leave "rm" cmd out
            print("Removed")


def help_key():
    key = """
    Add task: add <task>
    Edit task: edit <task #>
    Remove task: rm <task #>
    Clear all tasks: clear
    Show tasks: show
    Show help key: help
    Exit app: quit or q
    """
    print(key)


ask_user()
