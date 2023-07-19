"""
Driver class for task app.
"""
from queue import Queue
import SortTasks


class TaskAppDriver:
    """Actions within task app."""

    def __init__(self):
        """Constructor."""
        try:
            # Read mode; prevent data overwritten
            file = open("output/tasklist.txt", "r")
        except FileNotFoundError:
            # Create file if doesn't exist
            file = open("output/tasklist.txt", "w")
        file.close()

    def add_task(self, new_task):
        """Adds and sorts tasks based on zero-shot classification scores."""
        self.write_to_file(task=f"{new_task}\n", clear=0)  # 1st task

        if self.total_num_of_tasks() != 0:
            SortTasks.SortTasks()  # output scores for each time of day
            nlp_output = open("output/sort_tasks_output.txt", "r")
            morning, afternoon, evening = (
                Queue(maxsize=0),
                Queue(maxsize=0),
                Queue(maxsize=0),
            )  # Infinite size queues

            # Sort tasks into the queue for appropriate time
            for output in nlp_output.readlines():
                dict = eval(output)  # str to dict
                # Labels already sorted largest to smallest
                time_done = dict["labels"][0]
                task = dict["sequence"][:-1]  # remove newline char

                if time_done == "morning":
                    morning.put(task)
                elif time_done == "afternoon":
                    afternoon.put(task)
                else:
                    evening.put(task)

            self.write_to_file(q=morning)
            # Appends afternoon and evening after morning
            self.write_to_file(q=afternoon, clear=0)
            self.write_to_file(q=evening, clear=0)

    def edit_task(self, n):
        """Edits the nth task."""
        file = open("output/tasklist.txt", "r")
        q = Queue(maxsize=0)  # infinite size
        found = 0  # Tracks if nth task exists

        # If task exists, let user edit
        for task in file.readlines():
            task_num = task.split()[0]

            # Puts tasks into queue. Only inserts task, numbering added later.
            if task_num == n:
                # Put new task into queue
                task = input(f"New task #{n}: ")
                found = 1
                q.put(task)
            else:
                task = task.split()[1:]
                q.put(" ".join(task))

        if found == 1:
            self.write_to_file(q=q)
        return found

    def remove_task(self, n):
        """Removes the nth task."""
        file = open("output/tasklist.txt", "r")
        q = Queue(maxsize=0)  # infinite size
        found = 0  # Tracks if nth task exists

        # If task exists, nth task deleted
        for task in file.readlines():
            task_num = task.split()[0]

            # Puts tasks into queue ONLY if not deleted one.
            # Only inserts task, numbering added later.
            if task_num != n:
                task = task.split()[1:]
                q.put(" ".join(task))
            else:
                found = 1

        if found == 1:
            self.write_to_file(q=q)
        return found

    def write_to_file(self, q: Queue = None, task: str = None, clear=1):
        """
        Appends a task to tasklist or rewrites file given a queue of
        tasks (FIFO). Clears file by default.
        """
        if clear:
            # Clear tasks from file
            self.clear_file()

        with open("output/tasklist.txt", "a") as file:
            if task:
                # Append a single task to file
                file.write(task)
            elif q:
                # Add tasks from queue to file
                while not q.empty():
                    # Adds new task
                    file.write(f"{q.get()}\n")

    def show_tasks(self):
        """Prints out all tasks with 1-based numbering to file."""
        file = open("output/tasklist.txt", "r")
        for task_num, task in enumerate(file.readlines()):
            print(f"{task_num} {task[:-1]}")  # Don't print newline char

    def total_num_of_tasks(self):
        """Returns the total number of tasks currently on file."""
        file = open("output/tasklist.txt", "r")
        return len(file.readlines())

    def clear_file(self):
        """Clears all tasks from file."""
        with open("output/tasklist.txt", "r+") as file:
            file.seek(0)
            file.truncate()  # truncates file to 0th byte

    def close_file(self):
        """Closes file."""
        try:
            open(
                "output/tasklist.txt", "r"
            ).close()  # Read mode so file not overwritten
        except FileNotFoundError:
            None  # File doesn't exist
