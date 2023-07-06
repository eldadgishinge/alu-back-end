#!/usr/bin/python3

"""
Module: todo_exporter.py
This module exports data in JSON format containing all tasks from all employees.
The format of the exported JSON is:
{
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    ...
}
The exported JSON file is named todo_all_employees.json.
"""

import json
import requests


def export_todo_all_employees():
    """
    Export all tasks from all employees to a JSON file.
    """
    # Fetch all users
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    # Fetch tasks for each user
    tasks_by_user = {}
    for user in users:
        user_id = str(user['id'])
        tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
        tasks = tasks_response.json()
        tasks_by_user[user_id] = [
            {
                'username': user['username'],
                'task': task['title'],
                'completed': task['completed']
            }
            for task in tasks
        ]

    # Export tasks to JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(tasks_by_user, file)


if __name__ == '__main__':
    export_todo_all_employees()
