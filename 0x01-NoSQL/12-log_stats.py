#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


def requestLogs():
    """returns the list of school having a specific topic"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    print("{} logs".format(logs.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = len(list(logs.find({"method": "GET", "path": "/status"})))
    print("{} status check".format(status_check))



if __name__ == "__main__":
    requestLogs()
