#!/usr/bin/python3
""" Python script that fetches data from hhttps://jsonplaceholder.typicode.com/
    and export to json file
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)
    url = 'https://jsonplaceholder.typicode.com/'

    res = requests.get(url + 'users/' + sys.argv[1])
    usr_name = res.json().get('name')
    usr_id = sys.argv[1]

    res = requests.get('{}todos?userId={}'.format(url, sys.argv[1]))
    todos = res.json()

    a_tasks = {str(usr_id): []}
    for todo in todos:
        a_tasks[usr_id].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": usr_name})

    file_name = '{}.json'.format(usr_id)
    with open(file_name, mode="w") as file:
        json.dump(a_tasks, file)