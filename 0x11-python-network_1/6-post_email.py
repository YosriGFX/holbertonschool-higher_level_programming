#!/usr/bin/python3
'''
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response.
'''
import requests
from sys import argv

if __name__ == '__main__':
    Payloads = {'email': argv[2]}
    ReqData = requests.post(
        argv[1],
        data=Payloads
    )
    print(ReqData.text)
