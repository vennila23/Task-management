import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    deadline DATE,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
''')

# Function to add a new task
def add_task(title, description, deadline, user_id):
    cursor.execute('INSERT INTO tasks (title, description, deadline, user_id) VALUES (?, ?, ?, ?)',
                   (title, description, deadline, user_id))
    conn.commit()

# Function to get all tasks for a user
def get_tasks(user_id):
    cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,))
    return cursor.fetchall()

# Example usage
add_task('Task 1', 'This is a task', datetime(2024, 7, 15), 1)
add_task('Task 2', 'This is another task', datetime(2024, 7, 20), 1)

tasks = get_tasks(1)
for task in tasks:
    print(task)

# Close the database connection
conn.close()




import sqlite3

# Connect to the database
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Function to add a new user
def add_user(username, password, email):
    cursor.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                   (username, password, email))
    conn.commit()

# Function to get user by username
def get_user(username):
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    return cursor.fetchone()

# Example usage
add_user('john', 'password123', 'john@example.com')

user = get_user('john')
print(user)

# Close the database connection
conn.close()