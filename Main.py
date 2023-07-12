import TaskAppDriver

"""Runs the main application."""

driver = TaskAppDriver.TaskAppDriver()  # calls driver class


def ask_user():
    """Gets user input and executes corresponding action."""
    while True:
        user_input = input("Enter input: ")

        if user_input.lower() == "quit" or user_input.lower() == "q":
            driver.close_file()
            exit()
        elif user_input.lower() == "show":
            driver.show_all_tasks()
        elif user_input.lower().startswith("add"):
            driver.add_task(user_input)


ask_user()
