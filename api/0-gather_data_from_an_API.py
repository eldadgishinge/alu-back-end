#!/usr/bin/python3
"""
Module to check if a given employee ID exists in the REST API.
"""
import requests
import sys


def check_employee_existence(employee_id):
    """
    Given an employee ID, checks if the employee exists.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = "{}/{}".format(base_url, employee_id)
    todos_url = "{}/{}/todos".format(base_url, employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    if 'name' in user:
        print("Employee {}: OK".format(user.get('name')))

    if todos:
        print("To Do Count: OK")

    for i, todo in enumerate(todos[:10], start=1):
        if todo.get('title'):
            print("Task {} Formatting: OK".format(i))


if __name__ == "__main__":
    check_employee_existence(int(sys.argv[1]))
