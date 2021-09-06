from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def scrappy():
    pass

@app.route('/loading')
def loading():
    pass

# member db
@app.route('/login')
def login():
    pass

@app.route('/register')
def register():
    pass

@app.route


if __name__ == "__main__":
    app.run(debug=True)
