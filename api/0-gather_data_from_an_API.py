#!/usr/bin/python3
"""
Module to track TODO list progress of an employee using a REST API.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Given an employee ID, prints information about his/her TODO list progress.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = "{}/{}".format(base_url, employee_id)
    todos_url = "{}/{}/todos".format(base_url, employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    done_tasks = [todo for todo in todos if todo.get('completed')]

    name = user.get('name')
    done = len(done_tasks)
    total = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))
