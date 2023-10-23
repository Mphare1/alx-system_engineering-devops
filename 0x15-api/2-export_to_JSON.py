#!/usr/bin/python3

"""
Exports data to a JSON file.
"""

import json
from requests import get
from sys import argv

if __name__ == '__main':
    tasks_list = []
    user_dict = {}
    root = 'https://jsonplaceholder.typicode.com'
    user = get(f'{root}/users/{argv[1]}').json()
    
    for i in get(f'{root}/todos').json():
        if i.get('userId') == int(argv[1]):
            task = {
                "task": i.get('title'),
                "completed": i.get('completed'),
                "username": user.get('username')
            }
            tasks_list.append(task)
    
    user_dict[argv[1]] = tasks_list

    with open(f'{argv[1]}.json', 'w') as f:
        json.dump(user_dict, f, indent=4)
