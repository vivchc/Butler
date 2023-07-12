class TaskAppDriver:
    """Actions in task app."""

    def add_task(self, task):
        """Numbers new task and appends it to the end of file."""
        task_num = self.total_num_of_tasks()  # 0-based numbering
        file = open("tasklist.txt", "a")
        file.write(f"{task_num} {task[4:]}\n")  # Leave "add" cmd out

    def show_all_tasks(self):
        """Prints out all tasks on file."""
        file = open("tasklist.txt", "r")
        for line in file.readlines():
            print(f"{line[:-1]}")  # Leaves out newline char

    def total_num_of_tasks(self):
        """Returns the total number of tasks currently on file."""
        file = open("tasklist.txt", "r")
        return len(file.readlines())

    def close_file(self):
        """Closes file."""
        open("tasklist.txt", "r").close()
