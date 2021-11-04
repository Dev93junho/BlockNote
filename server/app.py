from flask import Flask, render_template, send_from_directory,jsonify, request # data를 송수신하는 기능을 가진것은 request
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS, cross_origin
from core.scrappy import url_search
from pymongo import MongoClient
import requests
import json


# app = Flask(__name__, static_folder='../client/build', static_url_path='')
app = Flask(__name__)
CORS(app)

'''
If you want to change the Environment state to production,
Go to '.env', rewrite develop to production
'''

# index page
@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def serve():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def post():
    value = request.form["url"]
    search_result = url_search(value)
    print(search_result)
    return 


if __name__ == "__main__":
    app.run(debug=True)
