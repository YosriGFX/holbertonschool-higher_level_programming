#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL
'''
import urllib.error as error
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    ReqData = request.Request(argv[1])
    try:
        with request.urlopen(ReqData) as Data:
            print(Data.read().decode('utf-8'))
    except error.HTTPError as excep:
        print("Error code: {}".format(excep.code))
