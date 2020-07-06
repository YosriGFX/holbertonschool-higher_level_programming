#!/usr/bin/python3
'''
sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter
'''
import requests
from sys import argv

if __name__ == '__main__':
    Query = argv[1] if len(argv) == 2 else ""
    Link = 'http://0.0.0.0:5000/search_user'
    ReqData = requests.post(Link, data={'Query': Query})
    try:
        ResponseDict = ReqData.json()
        id, name = ResponseDict.get('id'), ResponseDict.get('name')
        if len(ResponseDict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(ResponseDict.get('id'), ResponseDict.get('name')))
    except:
        print("Not a valid JSON")
