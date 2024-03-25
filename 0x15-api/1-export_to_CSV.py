#!/usr/bin/python3
"""Script to fetch employee TODO list and export it in CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    us = requests.get(url + "users/{}".format(user_id)).json()
    username = us.get("username")
    tod = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, i.get("completed"), i.get("title")]
            ) for i in tod]
