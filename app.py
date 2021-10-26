from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from scrappy import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('docspace.html')

@app.route('/documents', methods=['GET', 'POST'])
def call_api():
    return render_template('docspace.html')

@app.route('/documents')
def report():
    print(request.args.get('url'))
    pass

# Login module
# member db
@app.route('/login')
def login(methods=['GET','POST']):
    
    pass

@app.route('/register')
def register():
    pass

# loading page
@app.route('/loading')
def loading():
    return render_template('loading.html')


if __name__ == "__main__":
    app.run(debug=True)
