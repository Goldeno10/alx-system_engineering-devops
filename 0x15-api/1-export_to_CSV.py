#!/usr/bin/python3
"""
Python script that, using this REST API(https://jsonplaceholder.typicode.com/),
for a given employee ID, returns information about his/her
TODO list progress
"""

import csv
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

filename = f"{user_id}.csv"
with open(filename, 'w', encoding="utf8") as f:
    writer = csv.writer(f)
    for item in user_todo:
        arr = [str(user_id),
               str(EMPLOYEE_NAME),
               str(item.get('completed')),
               str(item.get('title'))]
        writer.writerow(arr)
