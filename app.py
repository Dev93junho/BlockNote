from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import urllib.request
from tqdm import trange, notebook
import pandas as pd
import requests
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def scrappy():
    page_url = input
    soup = BeautifulSoup(html_doc, 'html.parser')

    data=[]
    for no in notebook.tqdm(range(1, 76)):
        url = page_url + str(no)
        f = urllib.request.urlopen(url)
        source = f.read()

        soup = BeautifulSoup(source, "html.parser")
        tables=soup.select('table') # fixed html tag

        table_html = str(tables)
        table_df_list = pd.read_html(table_html) # LIST type

        for i in range(1):
            add_list = table_df_list[0]
            data.append(add_list)

        X= np.array(data).reshape(-1, 6)
        df = pd.DataFrame(X)


    return render_template('scrap-space.html')
    
# ########## after mvp ##############
# @app.route('/loading')
# def loading():
#     pass

# # member db
# @app.route('/login' methods=['GET','POST'])
# def login():
#     pass

# @app.route('/register')
# def register():
#     pass
# # ######################################


if __name__ == "__main__":
    app.run(debug=True)
