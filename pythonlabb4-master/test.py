import requests
import time
from random import randint
from flask import Flask, escape, request, jsonify, render_template


def test():
    while True:
        try:
            regn = randint(99,700)
            snow = randint(12,99)
            heat = randint(1,10)
            # while True:
            #     time.sleep(10)

            data_dict = {'regnfall':regn, 'snofall':snow, 'temp':heat}

            r = requests.post('http://127.0.0.1:8090/postjson', json=data_dict)
            print(r.status_code)
            print(r.headers)
            time.sleep(10)
        except:
            print('error')

test()