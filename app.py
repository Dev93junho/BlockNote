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
@app.route('/')
@cross_origin()
def serve():
    result = json.dumps("", ensure_ascii = False)

    return render_template("index.html", tableBy=result, strBy=result)


@app.route('/post')
@cross_origin()
def post():
    try:
        input = request.args.get('url')
        temp = url_search(input)
        #table_result = table_scrappy(temp)
        str_result = str_scrappy(temp)

        result_2 = table_scrappy_mk2(input)

        return render_template("index.html", tableBy=result_2, strBy=str_result)
      
    except:
        return redirect("/") # If block the crawl, redirect to index page

# shin 

if __name__ == "__main__":
    app.run(debug=True)
