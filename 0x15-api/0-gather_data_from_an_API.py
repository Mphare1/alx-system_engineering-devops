#!/usr/bin/python3

"""
Returns information about employee TODO list progress based on id.
"""

import requests
from sys import argv

if __name__ == '__main__':
    done = 0
    tasks = []
    root = 'https://jsonplaceholder.typicode.com'
    name = requests.get(f'{root}/users/{argv[1]}').json().get('name')

    for i in requests.get(f'{root}/todos').json():
        if i.get('userId') == int(argv[1]):
            tasks.append(i)
            if i.get('completed') is True:
                done += 1

    print(f'Employee {name} is done with tasks({done}/{len(tasks)}):')
    for i in tasks:
        if i.get('completed') is True:
            print(f'\t {i.get("title")}')
