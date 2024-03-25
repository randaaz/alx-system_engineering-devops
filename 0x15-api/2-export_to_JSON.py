#!/usr/bin/python3
"""Script to fetch employee TODO list and export it in JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    us = requests.get(url + "users/{}".format(user_id)).json()
    username = us.get("username")
    tod = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username
                } for i in tod]}, jsonfile)
