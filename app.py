from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def scrappy():
    return "scrappy"

if __name__ == "__main__":
    app.run(debug=True)
