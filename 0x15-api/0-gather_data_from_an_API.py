#!/usr/bin/python3
"""Python script that uses jsonplaceholder API to get
information about a given employee.
"""

import sys
from urllib.request import urlopen
import json

if __name__ == "__main__":
    #user id gotten from command line input
    user_id = int(sys.argv[1])

    #url to "todo" API
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    with urlopen(todo_url) as todo_resp:
        todo = todo_resp.read()
    # Json representation of the response
    todo_data = json.loads(todo)

    # url to "user info" API
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    with urlopen(user_url) as user_resp:
        user = user_resp.read()
    # JSON representation of the response
    user_data = json.loads(user)

    # Array user todos and completed todos
    user_todo = [item for item in todo_data if item["userId"] == user_id]
    comp_todo = [item for item in user_todo if item["completed"] is True]

    # Username nomber of tasks and number of comleted task as goten from the API 
    EMPLOYEE_NAME = user_data.get('name')
    TOTAL_NUMBER_OF_TASKS = len(user_todo)
    NUMBER_OF_DONE_TASKS = len(comp_todo)

    print(f"Employee {EMPLOYEE_NAME} is done with\
     tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for item in comp_todo:
        print(f"     {item.get('title')}")
