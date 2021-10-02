from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import numpy as np
import os
from core import scrappy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    return scrappy
    
    
########## Login Module ##############
# member db
@app.route('/login')
def login(methods=['GET','POST']):
    pass

@app.route('/register')
def register():
    pass

########## Loading page ##############
@app.route('/loading')
def loading():
    return render_template('loading.html')


if __name__ == "__main__":
    app.run(debug=True)
