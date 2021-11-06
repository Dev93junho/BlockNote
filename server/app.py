from flask import Flask, render_template, send_from_directory, request
# from flask_restful import Api, Resouce, reqpasre
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
@app.route('/', defaults={'path':''})
@cross_origin()
def serve(path):
    return render_template('index.html')


@app.route('/post/<url>')
@cross_origin()
def post():
    try:
        input = request.args.get('url')
        search_result = str_scrappy(url_search(input))

        # print(search_result)
        return json.dumps(search_result)
    except:
        return redirect("/") # If block the crawl, redirect to index page



if __name__ == "__main__":
    app.run(debug=True)
