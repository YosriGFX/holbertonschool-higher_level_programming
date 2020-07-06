#!/usr/bin/python3
'''
Write a Python script that takes in a URL,
sends a request to the URL
and displays the body of the response.
'''
import requests
from sys import argv

if __name__ == '__main__':
    ReqData = requests.get(argv[1])
    status_code = ReqData.status_code
    print(ReqData.text) if status_code < 400 else print(
        "Error code: {}".format(ReqData.status_code))
