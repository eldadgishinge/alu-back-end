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
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    response = requests.get(user_url)
    user = response.json()

    response = requests.get(todos_url)
    todos = response.json()

    done_tasks = [todo for todo in todos if todo.get('completed') == True]
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(user.get('name'), number_of_done_tasks, total_number_of_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))

