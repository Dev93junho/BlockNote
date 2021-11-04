from flask import Flask, render_template, send_from_directory,jsonify, request # data를 송수신하는 기능을 가진것은 request
from werkzeug.utils import redirect, secure_filename
import os
from flask_cors import CORS, cross_origin
from core.scrappy import *
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
@app.route('/')
@cross_origin()
def serve():
    return render_template('index.html')


@app.route('/post')
@cross_origin()
def post():
    try:
        input = request.args.get('url')
        search_result = str_scrappy(url_search(input))

        # print(search_result)
        return render_template("test_result.html", searchingBy=search_result)
    except:
        return redirect("/") # If block the crawl, redirect to index page



if __name__ == "__main__":
    app.run(debug=True)
