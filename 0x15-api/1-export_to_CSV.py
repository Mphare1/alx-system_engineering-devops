#!/usr/bin/python3

"""
Exports data to a CSV file.
"""

import csv
import requests
from sys import argv

if __name__ == '__main':
    tasks_list = []
    root = 'https://jsonplaceholder.typicode.com'
    user = requests.get(f'{root}/users/{argv[1]}').json()

    for i in requests.get(f'{root}/todos').json():
        if i.get('userId') == int(argv[1]):
            tasks = [argv[1], user.get('username'), i.get('completed'), i.get('title')]
            tasks_list.append(tasks)

    with open(f'{argv[1]}.csv', 'w', newline='') as f:
        f_csv = csv.writer(f, quoting=csv.QUOTE_ALL)
        f_csv.writerows(tasks_list)
