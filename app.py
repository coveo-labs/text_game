#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
