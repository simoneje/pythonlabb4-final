import sqlite3
from flask import Flask, escape, request, jsonify, render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    killer = [
    request.form.get('fname'),
    request.form.get('ename'),
    request.form.get('address'),
    request.form.get('zipcode'),
    request.form.get('city'),
    request.form.get('cellphone'),
    request.form.get('email'),
    request.form.get('paymenttype'),
    request.form.get('offers'),
    request.form.get('format'),
    request.form.get('comment')]

    f_name = killer[0]
    e_name = killer[1]
    address = killer[2]
    postnmr = killer[3]
    stad = killer[4]
    telnmr = killer[5]
    email = killer[6]
    betala = killer[7]
    offer = killer[8]
    form = killer[9]
    kommentar = killer[10]
    return render_template('test.html', fname = f_name, ename =e_name, address=address, postnmr =postnmr, stad=stad, tele=telnmr, email=email, pay=betala, offer=offer, for_mat=form, kommentar=kommentar)





if __name__ == '__main__':
    app.run()
    
    
