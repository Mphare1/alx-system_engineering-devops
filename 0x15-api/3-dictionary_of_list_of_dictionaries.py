#!/usr/bin/python3

"""
Exports data to JSON.
"""

import json
from requests import get

if __name__ == '__main':
    user_dict = {}
    root = 'https://jsonplaceholder.typicode.com'
    user_id = None  # Initialize user_id to None

    for i in get(f'{root}/todos').json():
        current_user_id = i.get('userId')

        if current_user_id != user_id:
            # Create a new list of tasks for a different user
            tasks_list = []
            user_id = current_user_id

        user = get(f'{root}/users/{current_user_id}').json()
        task = {
            "username": user.get('username'),
            "task": i.get('title'),
            "completed": i.get('completed')
        }

        tasks_list.append(task)
        user_dict[current_user_id] = tasks_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_dict, f, indent=4)
