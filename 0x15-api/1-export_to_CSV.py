#!/usr/bin/python3
""" Python script that fetches hhttps://jsonplaceholder.typicode.com/
"""
import csv
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

    a_tasks = []
    for todo in todos:
        a_tasks.append([usr_id,
                       usr_name,
                       todo.get('completed'),
                       todo.get('title')])

    file_name = '{}.csv'.format(usr_id)
    with open(file_name, mode='w') as employee_data:
        employee_writer = csv.writer(employee_data,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in a_tasks:
            employee_writer.writerow(task)