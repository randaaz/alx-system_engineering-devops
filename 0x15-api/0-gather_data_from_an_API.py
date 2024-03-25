#!/usr/bin/python3
"""Script to fetch and display employee TODO list progress from a REST API."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    us = requests.get(url + "users/{}".format(sys.argv[1])).json()
    to = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    comp = [t.get("title") for t in to if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        us.get("name"), len(compl), len(to)))
    [print("\t {}".format(c)) for c in comp]
