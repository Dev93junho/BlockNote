from flask import Flask, render_template
import requests
import pandas as pd
from bs4 import BeautifulSoup 


app = Flask(__name__)

#User input the url
response = requests.url(input)

@app.route('/')
def home():
    return "home"

@app.route('/scrap')
def scrap(response):
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
    else:
        print(response.status_code)


@app.route('result')
def result():
    return "this page for print scrap result"

if __name__ == '__main__':
    app.run(debug=True)