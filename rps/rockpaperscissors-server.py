#!/usr/bin/python3
from flask import Flask, request, jsonify, abort
import random

app = Flask(__name__)

def rps():
    return random.choice([ 'rock', 'paper', 'scissors' ])

@app.route("/play", methods=['GET', 'POST'])
def play():
    if request.method == 'POST' and request.args.get('challenge'):
        win_matrix = { 'scissors' : 'rock', 'paper' : 'scissors' , 'rock' : 'paper' }
        if request.args.get('challenge') not in win_matrix:
            abort(500)
        my_result = rps()
        return jsonify({ 'response' : request.args.get('challenge') == win_matrix[my_result], 'result' : my_result })
    else:
        return jsonify({ 'challenge' : rps() })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
