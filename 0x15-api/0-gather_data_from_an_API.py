#!/usr/bin/python3
""" Python script that fetches hhttps://jsonplaceholder.typicode.com/
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)
    url = 'https://jsonplaceholder.typicode.com/'

    res = requests.get(url + 'users/' + sys.argv[1])
    usr_name = res.json().get('name')

    res = requests.get('{}todos?userId={}'.format(url, sys.argv[1]))
    todos = res.json()

    tot_tasks = len(todos)
    c_tasks = []
    for todo in todos:
        if todo.get('completed') is True:
            c_tasks.append(todo)
    tasks_done = len(c_tasks)

    msg = 'Employee {} is done with tasks({}/{}):'
    print(msg.format(usr_name, tasks_done, tot_tasks))

    for todo in todos:
        print('\t {}'.format(todo.get('title')))
