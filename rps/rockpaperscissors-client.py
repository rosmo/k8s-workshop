#!/usr/bin/python3
from flask import Flask, request, jsonify, render_template
import requests
import random
import os
import json

app = Flask(__name__)

backend_url = 'http://127.0.0.1:5000/'
if 'RPSSERVER_SERVICE_HOST' in os.environ and 'RPSSERVER_SERVICE_PORT' in os.environ:
   backend_url = 'http://%s:%d/' % (os.environ['RPSSERVER_SERVICE_HOST'], int(os.environ['RPSSERVER_SERVICE_PORT']))

print('Backend URL: %s' % backend_url)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form.get('challenge'):
        response = requests.post('%splay?challenge=%s' % (backend_url, request.form.get('challenge')))
        print('Response from backend: %s' % response.content.decode('utf-8'))
        ret = json.loads(response.content)
        return render_template('index.html', played=True, response=ret['response'], backend=response.content.decode('utf-8'))

    return render_template('index.html', played=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
