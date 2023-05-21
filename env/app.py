from flask import Flask
from flask import render_template, request, redirect
import datetime
import sqlite3

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')
#pass
@app.route('/pass_login')
def pass_login():
    return render_template('pass_login.html')

@app.route('/pass_login/pass_main')
def pass_main():
    return render_template('pass_main.html')

# admin
@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

# driver
@app.route('/drivers_login')
def driver_login():
    return render_template('driver_login.html')

if __name__ == "__main__":
    app.run()