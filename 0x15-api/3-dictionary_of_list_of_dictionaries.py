#!/usr/bin/python3
""" Python script that fetches data from hhttps://jsonplaceholder.typicode.com/
    and export data in the JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    dict_task = {}
    users = requests.get(url + 'users').json()
    for user in users:
        usr_name = user.get('username')
        usr_id = user.get('id')
        todos = requests.get(url + 'todos?userId=' + str(usr_id)).json()
        usr_tasks = []
        for todo in todos:
            dict_t = {"username": usr_name,
                      "task": todo.get('title'),
                      "completed": todo.get('completed')}
            usr_tasks.append(dict_t)
        dict_task[str(usr_id)] = usr_tasks

    file_name = 'todo_all_employees.json'
    with open(file_name, mode='w') as f:
        json.dump(dict_task, f)
