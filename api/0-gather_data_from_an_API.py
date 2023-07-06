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
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    response = requests.get(user_url)
    user = response.json()

    if 'name' in user:
        print("Employee {}: OK".format(user.get('name')))


if __name__ == "__main__":
    check_employee_existence(int(sys.argv[1]))
