from queue import Queue


class TaskAppDriver:
    """Actions within task app."""

    def add_task(self, task):
        """Numbers new task and appends to file."""
        task_num = self.total_num_of_tasks()  # 0-based numbering
        file = open("tasklist.txt", "a")
        file.write(f"{task_num} {task}\n")
        print("Added")

    def edit_task(self, n):
        """Edits the nth task."""
        file = open("tasklist.txt", "r")
        q = Queue(maxsize=0)  # infinite size
        not_found = 0  # Tracks if nth task exists

        # If task exists, let user edit
        for task in file.readlines():
            task_num = task.split()[0]

            # Puts tasks into queue. Only inserts task, numbering added later.
            if task_num == n:
                # Put new task into queue
                task = input(f"New task #{n}: ")
            else:
                task = task.split()[1]

            q.put(task)

        if not_found == 1:
            print("Task not found.")
        else:
            self.rewrite_file(q)
            print("Edited")

    def remove_task(self, n):
        """Removes the nth task."""
        file = open("tasklist.txt", "r")
        q = Queue(maxsize=0)  # infinite size
        not_found = 0  # Tracks if nth task exists

        # If task exists, nth task deleted
        for task in file.readlines():
            task_num = task.split()[0]

            # Puts tasks into queue ONLY if not deleted one.
            # Only inserts task, numbering added later.
            if task_num != n:
                task = task.split()[1]
                q.put(task)

        if not_found == 1:
            print("Task not found.")
        else:
            self.rewrite_file(q)
            print("Removed")

    def rewrite_file(self, q):
        """Rewrites file given a queue of tasks (FIFO)."""
        # Clears file
        self.clear_file()
        # Add tasks from queue into file
        while not q.empty():
            self.add_task(q.get())

    def clear_file(self):
        """Clears all tasks from file."""
        try:
            file = open("tasklist.txt", "r+")
            file.seek(0)
            file.truncate()  # truncates file to 0th byte
            print("Cleared all tasks!")
        except FileNotFoundError:
            print("Already clear!")

    def show_all_tasks(self):
        """Prints out all tasks on file."""
        try:
            file = open("tasklist.txt", "r")
            for task in file.readlines():
                print(f"{task[:-1]}")  # Leaves out newline char
        except FileNotFoundError:
            print("No tasks to show.")

    def total_num_of_tasks(self):
        """Returns the total number of tasks currently on file."""
        file = open("tasklist.txt", "r")
        return len(file.readlines())

    def close_file(self):
        """Closes file."""
        try:
            open("tasklist.txt", "r").close()  # Read mode so file not overwritten
        except FileNotFoundError:
            None  # File doesn't exist
