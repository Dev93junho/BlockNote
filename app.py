from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import scrappy

DEFAULT_PORT = 5000
DEFAULT_HOST = '0.0.0.0'

app = Flask(__name__)

# index page
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('docspace.html')

# display scrappy data to sidebar
@app.route('/sidebar/<scrap_db>')
def report(scrap_db):
    pass


# writing function

# Login module
@app.route('/login', methods=['GET','POST'])
def login():
    pass

@app.route('/register')
def register():
    pass

@app.route('/user/<username>')
def get_username(username):
    return 

if __name__ == "__main__":
    app.run(debug=True)
