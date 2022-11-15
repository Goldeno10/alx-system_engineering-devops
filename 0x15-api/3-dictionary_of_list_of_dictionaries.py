#!/usr/bin/python3
""" Python script to export data in the CSV format. """

import json
from urllib.request import urlopen
import sys


todo_url = "https://jsonplaceholder.typicode.com/todos"
with urlopen(todo_url) as todo_resp:
    todo = todo_resp.read()
todo_data = json.loads(todo)

user_url = f"https://jsonplaceholder.typicode.com/users"
with urlopen(user_url) as user_resp:
    user = user_resp.read()
user_data = json.loads(user)
dict_t = {}
for user in user_data:
    user_id = user.get("id")
    user_todo = [item for item in todo_data if item["userId"] == user_id]
    # comp_todo = [item for item in user_todo if item["completed"] is True]

    username = user.get('username')
    EMPLOYEE_NAME = user.get('name')
    # TOTAL_NUMBER_OF_TASKS = len(user_todo)
    # NUMBER_OF_DONE_TASKS = len(comp_todo)

    task_l = []
    for item in user_todo:
        task_dict = {}
        task_dict["username"] = username
        task_dict["task"] = item.get('title')
        task_dict["completed"] = item.get('completed')
        task_l.append(task_dict)

    dict_t[str(user_id)] = task_l

filename = "todo_all_employees.json"
with open(filename, 'w', encoding="utf8") as f:
    json_str = json.dumps(dict_t, indent=4)
    f.write(json_str)
