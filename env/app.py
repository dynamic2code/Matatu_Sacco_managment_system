from flask import Flask
from flask import render_template, request, redirect
import datetime
import sqlite3

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/pass_login')
def pass_login():
    return 'Hello, World!'

@app.route('/admin_login')
def admin_login():
    return 'Hello, World!'

@app.route('/drivers_login')
def drivers_login():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()