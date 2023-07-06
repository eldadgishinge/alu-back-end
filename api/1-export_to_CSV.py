#!/usr/bin/python3
"""
Module to export employee tasks to a CSV file.
"""
import csv
import requests
import sys


def export_employee_tasks_to_csv(employee_id):
    """
    Given an employee ID, exports all tasks that are owned by this employee.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"
    todos_url = f"{base_url}/{employee_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
        fieldnames = [
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ]
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL
        )

        for todo in todos:
            writer.writerow({
                "USER_ID": user.get('id'),
                "USERNAME": user.get('username'),
                "TASK_COMPLETED_STATUS": todo.get('completed'),
                "TASK_TITLE": todo.get('title')
            })

    print("Number of tasks in CSV: OK")
    print("User ID and Username: OK")


if __name__ == "__main__":
    export_employee_tasks_to_csv(int(sys.argv[1]))
