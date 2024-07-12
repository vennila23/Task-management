# Task-management
The task management code is a simple command-line application that allows you to manage tasks. Here's a breakdown of the features:

- Add Task: Allows you to add a new task with a title, description, deadline, and user ID.

- Get Tasks: Retrieves and displays all tasks for a specific user ID.

- Update Task: Updates the title and deadline of an existing task.

- Delete Task: Deletes a task by its task ID.

The code uses a SQLite database to store tasks in a table called "tasks". The database is created automatically when you run the code for the first time.

Here's a step-by-step overview of how the code works:

1. Connects to the SQLite database.
2. Creates the "tasks" table if it doesn't exist.
3. Defines functions for adding, getting, updating, and deleting tasks.
4. Allows users to interact with the task manager through the command line.
