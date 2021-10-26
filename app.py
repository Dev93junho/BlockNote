from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import scrappy

DEFAULT_PORT = 5000
DEFAULT_HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('docspace.html')

@app.route('/sidebar/<scrap_db>')
def report(scrap_db):
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
