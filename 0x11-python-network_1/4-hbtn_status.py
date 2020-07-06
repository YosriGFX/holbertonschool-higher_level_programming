#!/usr/bin/python3
'''
Python script that fetches https://intranet.hbtn.io/status
'''
import requests

if __name__ == '__main__':
    Link = "https://intranet.hbtn.io/status"
    ReqData = requests.get(Link)
    plainText = ReqData.text
    print("Body response:")
    print("\t- type: {}".format(type(plainText)))
    print("\t- content: {}".format(plainText))
