#!/usr/bin/python3
"""Script to fetch TODO lists for all employees
   and export them to a JSON file."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    uss = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            j.get("id"): [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": j.get("username")
            } for i in requests.get(url + "todos",
                                    params={"userId": j.get("id")}).json()]
            for j in uss}, jsonfile)
