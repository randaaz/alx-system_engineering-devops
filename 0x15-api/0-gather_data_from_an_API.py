#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    use = requests.get(url + "users/{}".format(sys.argv[1])).json()
    tod = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    comp = [t.get("title") for t in tod if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        use.get("name"), len(comp), len(tod)))
    [print("\t {}".format(c)) for c in comp]
