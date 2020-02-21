import sqlite3
from flask import Flask, escape, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def databaspost():
    try:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT regnfall FROM weather")
        r = c.fetchall()
        rain = ''
        for x in r:
            rain = rain + x[0] + "cm, "

        c.execute("SELECT snofall FROM weather")
        s = c.fetchall()
        snow = ''
        for y in s:
            snow = snow + y[0] + "cm, "

        c.execute("SELECT temp FROM weather")
        h = c.fetchall()
        heat = ''
        for z in h:
            heat = heat + z[0] + "°C, "
        
        return render_template('databas.html', rain=rain, snow=snow, heat=heat)
    except:
        print('error')
        return 'Något gick fel'

if __name__ == '__main__':
    app.run()

    