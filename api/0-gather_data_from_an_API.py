#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    response = requests.get(user_url)
    user = response.json()
    response = requests.get(todos_url)
    todos = response.json()

    done_tasks = [todo for todo in todos if todo["completed"] == True]
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(todos)

    print(f"Employee {user['name']} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")

    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))
