import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template
import requests
import time
# app = Flask(__name__)

# regn = randint(99,700)
# snow = randint(12,99)
# heat = randint(1,10)
# # while True:
# #     time.sleep(10)

# data_dict = {'regnfall':regn, 'snöfall':snow, 'temp':heat}
# r = requests.post('https://en0lrbodw55rno.x.pipedream.net/', json=data_dict)
# print(r.status_code)
# print(r.json())
# print(r.headers)

app = Flask(__name__)
  
@app.route('/postjson', methods = ['POST'])

def postJsonHandler():
    try:
        print(f'request.is_json: {request.is_json}')
        content = request.json
        print(f'content: {content}')
        

        
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        # c.execute("""CREATE TABLE weather(
        #     regnfall text,
        #     snofall text,
        #     temp text
        # )""")

        c.execute("INSERT INTO weather (regnfall, snofall, temp) VALUES (?,?,?)", 
        (content['regnfall'], content['snofall'], content['temp']))
        # c.execute("SELECT * FROM väder")

        conn.commit()
        conn.close()
        return {'JSON was a success'}
    except: 
        print('error')
        return 'aa nä försök igen'




    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8090)

# @app.route('/weatherstation')
# def läggIn():




#     app.run()