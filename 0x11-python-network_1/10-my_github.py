#!/usr/bin/python3
'''
Python script that takes your Github credentials
(username and password) and uses the Github API
to display your id
'''
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    Link = 'https://api.github.com/users/{}'.format(argv[1])
    ReqData = requests.get(
        Link,
        auth=HTTPBasicAuth(
            argv[1],
            argv[2]
        )
    )
    print(ReqData.json().get('id'))
