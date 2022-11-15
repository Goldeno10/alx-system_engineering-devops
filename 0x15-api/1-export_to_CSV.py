#!/usr/bin/python3
"""Python script to export data in the CSV format."""

import csv
import json
from urllib.request import urlopen
import sys

if __name__ == "__main__":
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
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for item in user_todo:
            arr = [user_id,
                   EMPLOYEE_NAME,
                   item.get('completed'),
                   item.get('title')]
            writer.writerow(arr)
