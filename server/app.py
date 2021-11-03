from flask import Flask, send_from_directory,jsonify # data를 송수신하는 기능을 가진것은 request
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS, cross_origin
from core.scrappy import url_search
from pymongo import MongoClient
import requests

DEFAULT_PORT = 5000
DEFAULT_HOST = '0.0.0.0'

app = Flask(__name__, static_folder='../client/build', static_url_path='')
CORS(app)
'''
If you want to change the Environment state to production,
Go to '.env', rewrite develop to production
'''
# import mongoDB
client = MongoClient('localhost', 27017)

# index page
# @app.route('/', methods=['GET', 'POST'])
# @cross_origin()
# def home():
#     pass

# index page
@app.route('/index', methods=['GET', 'POST'])
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/post', methods=['GET', 'POST'])
def post():
    if requests.methods == 'POST':
        value = requests.form['url']
        value = str(value)
        result = url_search(value)
        print(result)
        # need to output with json 

# display scrappy data to topbar
# @app.route('/dbtank/<scrap_db>')
# @cross_origin()
# def searched(url): # need to receive data from client
#     input = request.args.get('url')
#     scrappy.url_searched(input)
#     pass

# Login module
# @app.route('/login', methods=['GET','POST'])
# def login():
#     pass

# @app.route('/register')
# def register():
#     pass

# @app.route('/user/<username>')
# def get_username(username):
#     return

if __name__ == "__main__":
    app.run(debug=True)
