#!/usr/bin/python3
"""
    python script that returns TODO list progress for a given employee ID
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    """
        request user info by employee ID
    """
    response = requests.get(user_url)
    user = response.json()
    response = requests.get(todos_url)
    todos = response.json()
    """
        convert json to dictionary
    """
    done_tasks = [todo for todo in todos if todo["completed"] == True]
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(todos)

    """
        extract employee name
    """
    print(f"Employee {user['name']} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")

    """
        request user's TODO list
    """
    for task in done_tasks:
        print(f"\t {task['title']}")
    """
        dictionary to store task status in boolean format
    """
    if __name__ == "__main__":
        get_employee_todo_progress(int(sys.argv[1]))
