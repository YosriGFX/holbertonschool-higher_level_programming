#!/usr/bin/python3
'''
Python script that takes in 3 strings
and sends a search request to the Twitter API
'''
import base64
from sys import argv
import requests


def search_twitter():
    '''
    Takes in 3 strings and sends a search request to the Twitter API.
    '''
    client_key = argv[1]
    client_secret = argv[2]
    search = argv[3]
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')
    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    authResponse = requests.post(
        auth_url,
        headers=auth_headers,
        data=auth_data
    )
    access_token = authResponse.json()['access_token']
    search_headers = {
        'Authorization': 'Bearer {}'.format(
            access_token
        )
    }
    params = {
        'q': search,
        'result_type': 'recent',
        'count': 5
    }
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    ReqData = requests.get(search_url, headers=search_headers, params=params)
    jsonData = ReqData.json()
    for s in jsonData['statuses']:
        tid = s['id']
        tt = s['text']
        tun = s['user']['name']
        print('[{}] {} by {}'.format(tid, tt, tun))

if __name__ == "__main__":
    search_twitter()
