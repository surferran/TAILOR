# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 10:42:30 2018

from
https://www.tocode.co.il/blog/2018-06-hello-flask-api

http://localhost:5000

"""

import flask
import flask_cors

print flask.__version__
print flask_cors.__version__

from flask import Flask, jsonify
from flask_cors import CORS


app = Flask('helloworld')
CORS(app)

# Decorator defines a route
# http://localhost:5000/
@app.route('/')
def index():
#    return "Hello World!"
    return jsonify({ 'text': 'Hello World!' })

if __name__ == '__main__':
    app.run()