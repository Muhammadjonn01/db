import psycopg2
from typing import Any
import datetime
from datetime import datetime
def make_conn():
    conn = psycopg2.connect(
        database="uraaa",
        user="postgres",
        password="Nigga.01",
        host="localhost"
    )
    return conn
def destroy_conn(conn):
    conn.close()
class Task:
    def __init__(self, name, description, priority, deadline):
        self.name = name
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = False

class TodoListManager:
    def __init__(self):
        self.tasks = []
    def make_conn():
        conn = psycopg2.connect(
            database="uraaa", user="postres", password="Nigga.01"
        )
        return conn
    def add_task(self):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        priority = int(input("Enter task priority (1-10): "))
        deadline = input("Enter task deadline (DD-MM-YYYY): ")
        comp = 'Not comleted'
        conn = make_conn()
        curr = conn.cursor()
        query = f"INSERT INTO all_tasks (title,description,priority,due_date,completed) VALUES ('{name}', '{description}','{priority}','{deadline}','{comp}')"
        curr.execute(query)
        conn.commit()
        destroy_conn(conn)        
        print("Task added!")
    def remove_task(self):
        name = input("Input task name: ")
        conn = make_conn()
        curr = conn.cursor()
        query = f"DELETE FROM all_tasks WHERE title = '{name}'"
        curr.execute(query)
        conn.commit()
        destroy_conn(conn)
        print('Task removed successfully!')
    def view_tasks(self):
        conn = make_conn()
        curr = conn.cursor()
        query = f"SELECT * FROM all_tasks"
        curr.execute(query)
        result = curr.fetchall()
        conn.commit()
        destroy_conn(conn)
        
        for row in result:
            name = row[1]
            description = row[2]
            priority = row[3]
            deadline = row[4]
            status = row[5]
            
            print(f"Name: {name}.\nDescription: {description}.\nPriority (1-10): {priority}.\nDeadline: {deadline}.\nStatus: {status}.")
            print("-----------------------------")
    def mark_task_as_completed(self):
        name = input("Input task name: ")
        conn = make_conn()
        curr = conn.cursor()
        query = f"UPDATE all_tasks SET completed = 'Completed' WHERE title = '{name}'"
        curr.execute(query)
        conn.commit()
        destroy_conn(conn)
        print('Task marked as completed successfully!')

    def show_todays_tasks(self):
        date_string = datetime.today()
        conn = make_conn()
        curr = conn.cursor()
        query = f"SELECT * FROM all_tasks WHERE due_date = '{date_string}'"
        curr.execute(query)
        result = curr.fetchall()
        conn.commit()
        destroy_conn(conn)
        
        for row in result:
            name = row[1]
            description = row[2]
            priority = row[3]
            deadline = row[4]
            status = row[5]
            
            print(f"Name: {name}.\nDescription: {description}.\nPriority (1-10): {priority}.\nDeadline: {deadline}.\nStatus: {status}.")
            print("-----------------------------")
    def sort_by_priority():
        conn = make_conn()
        curr = conn.cursor()
        query = f"SELECT * FROM all_tasks ORDER BY priority"
        curr.execute(query)
        conn.commit()
        destroy_conn(conn)
        print('Tasks sorted  successfully!')