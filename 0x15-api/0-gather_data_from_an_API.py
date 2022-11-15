#!/usr/bin/python3
""" Python script that uses jsonplaceholder API to get
information about a given employee. """

import sys
from urllib.request import urlopen
import json

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

EMPLOYEE_NAME = user_data.get('name')
TOTAL_NUMBER_OF_TASKS = len(user_todo)
NUMBER_OF_DONE_TASKS = len(comp_todo)

print(f"Employee {EMPLOYEE_NAME} is done with\
 tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

for item in comp_todo:
    print(f"     {item.get('title')}")
