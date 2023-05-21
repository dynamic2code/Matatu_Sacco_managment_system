from flask import Flask
from flask import render_template, request, redirect
import datetime
import sqlite3

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

#pass
@app.route('/pass_register')
def pass_register():
    return render_template('pass_register.html')

@app.route('/pass_register/pass_registerd', methods=['POST'])
def pass_registerd():
    return render_template('pass_main.html')

@app.route('/pass_login')
def pass_login():
    return render_template('pass_login.html')

@app.route('/pass_login/pass_main', methods=['POST'])
def pass_main():
    return render_template('pass_main.html')

# driver
@app.route('/driver_register')
def driver_register():
    return render_template('driver_register.html')

@app.route('/driver_register/driver_registerd', methods=['POST'])
def driver_registerd():
    return render_template('driver_main.html')

@app.route('/driver_login')
def driver_login():
    return render_template('driver_login.html')

@app.route('/driver_login/driver_main', methods=['POST'])
def driver_main():
    return render_template('driver_main.html')

# admin
@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin_login/admin_main', methods=['POST'])
def admin_main():
    return render_template('admin_main.html')


if __name__ == "__main__":
    app.run()