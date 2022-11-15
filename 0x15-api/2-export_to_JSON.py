#!/usr/bin/python3
""" Python script to export data in the json format. """

import json
from urllib.request import urlopen
import sys

user_id = int(sys.argv[1])

todo_url = "https://jsonplaceholder.typicode.com/todos"
with urlopen(todo_url) as todo_resp:
    todo = todo_resp.read()
todo_data = json.loads(todo)

user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
with urlopen(user_url) as user_resp:
    user = user_resp.read()
user_data = json.loads(user)

user_todo = [item for item in todo_data if item["userId"] == user_id]
comp_todo = [item for item in user_todo if item["completed"] is True]

username = user_data.get('username')
EMPLOYEE_NAME = user_data.get('name')
TOTAL_NUMBER_OF_TASKS = len(user_todo)
NUMBER_OF_DONE_TASKS = len(comp_todo)

# print(f"Employee {EMPLOYEE_NAME} is done with\
# tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

task_l = []
for item in user_todo:
    task_dict = {}
    task_dict["username"] = username
    task_dict["task"] = item.get('title')
    task_dict["completed"] = item.get('completed')
    task_l.append(task_dict)


dict_t = {}
dict_t[str(user_id)] = task_l

filename = f"{user_id}.json"
with open(filename, 'w', encoding="utf8") as f:
    json_str = json.dumps(dict_t, indent=4)
    f.write(json_str)
