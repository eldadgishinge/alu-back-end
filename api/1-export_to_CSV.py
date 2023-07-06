#!/usr/bin/python3

"""
Python script to retrieve and export TODO list progress for a given employee ID in CSV format.
"""

import requests
import sys
import csv


def get_employee_todo_list(employee_id):
    """
    Retrieves and exports the TODO list progress for a given employee ID in CSV format.
    """

    # Making a GET request to the API endpoint
    response = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={'userId': employee_id}
    )

    # Checking if the request was successful
    if response.status_code != 200:
        print(f"Error: Failed to retrieve TODO list for employee {employee_id}")
        return

    todos = response.json()

    # Preparing the CSV filename
    filename = f"{employee_id}.csv"

    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Writing each task as a row in the CSV file
        for todo in todos:
            user_id = todo['userId']
            username = todo['username']
            task_completed = todo['completed']
            task_title = todo['title']

            writer.writerow([user_id, username, task_completed, task_title])

    print(f"TODO list progress exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
