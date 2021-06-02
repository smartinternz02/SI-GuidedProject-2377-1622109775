# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:39:23 2021

@author: Suprathi
"""

from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer
import re
import requests
import os


app = Flask(__name__)

def check(language,output):
    url = "https://rapidapi.p.rapidapi.com/translateLanguage/translate"
    payload = "{\"target\": \""+language+"\",\"text\": \""+output+"\",\"type\": \"plain\"\r\n}"
    
    print(payload)
    headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "5d797ab107mshe668f26bd044e64p1ffd34jsnf47bfa9a8ee4",
    'x-rapidapi-host': "language-translation.p.rapidapi.com"

    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()['translatedText']

#home page
@app.route('/')
def home():
    return render_template('home.html')

#home page
@app.route('/translator')
def translator():
    return render_template('translator.html')

#translator pagerun
@app.route('/translate',  methods=['POST'])
def translate():
    language=request.form['type']
    output = request.form['output']
    print(output)
    translated = check(language,output)
    return render_template('translate.html',translated=translated)

port=os.getenv('VCAP_APP_PORT','5000')
    
if __name__ == "__main__":
    app.secret_key=os.urandom(12)
    app.run(debug=True,host='0.0.0.0',port=port)
    