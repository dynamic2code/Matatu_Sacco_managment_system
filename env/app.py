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
    name = request.form['name']
    password = request.form['password']
    phone = request.form['phone']
    email = request.form['email']
    

    # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()

    query = f"INSERT INTO passanger '{name}','{password}', '{phone}', '{email}'"
    action = cursor.execute(query)
    if action:
        cursor.close()
        conn.close()
        return render_template('pass_main.html')
    
    else:
        error_message = "An error occurred with your registration. If you have used our services try loging in above!"
        return render_template('main.html', error_message=error_message)
    

@app.route('/pass_login')
def pass_login():
    return render_template('pass_login.html')

@app.route('/pass_login/pass_main', methods=['POST'])
def pass_main():
    name = request.form['name']
    phone = request.form['phone']
    password = request.form['password']
    
        # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()

    query = f"SELECT * FROM your_table WHERE name = {name} AND number ={phone}  AND password = {password}"
    action = cursor.execute(query)
    if action:
        cursor.close()
        conn.close()
        return render_template('pass_main.html')
    
    else:
        error_message = "An error occurred with your log in. If you have not used our services try registering in below!"
        return render_template('main.html', error_message=error_message)
    

# driver
@app.route('/driver_register')
def driver_register():
    return render_template('driver_register.html')

@app.route('/driver_register/driver_registerd', methods=['POST'])
def driver_registerd():
    name = request.form['name']
    id = request.form['ID']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']

    plates = request.form['plates']
    capacity = request.form['capacity']

    # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()

    query = f"INSERT INTO driver '{name}', '{id}', '{email}', '{phone}', '{password}'"
    action = cursor.execute(query)
    if action:
        driver_id = cursor.lastrowid

        car_query = f"INSERT INTO car '{driver_id}', '{capacity}', '{plates}'"
        cursor.execute(car_query)
        
        cursor.close()
        conn.close()
        return render_template('driver_main.html')
    
    else:
        error_message = "An error occurred with your registration. If you have used our services try loging in above!"
        return render_template('main.html', error_message=error_message)

    

@app.route('/driver_login')
def driver_login():
    return render_template('driver_login.html')

@app.route('/driver_login/driver_main', methods=['POST'])
def driver_main():
    name = request.form['name']
    phone = request.form['phone']
    password = request.form['password']

    # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()

    
    query = f"SELECT * FROM your_table WHERE name = {name} AND number ={phone}  AND password = {password}"
    action = cursor.execute(query)
    if action:
        cursor.close()
        conn.close()
        return render_template('driver_main.html')
    
    else:
        error_message = "An error occurred with your registration. If you have used our services try loging in above!"
        return render_template('main.html', error_message=error_message)
    

# admin
@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin_login/admin_main', methods=['POST'])
def admin_main():
    name = request.form['name']
    phone = request.form['phone']
    password = request.form['password']

    # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()

    query = f"SELECT * FROM your_table WHERE name = {name} AND number ={phone}  AND password = {password}"
    action = cursor.execute(query)
    if action:
        cursor.close()
        conn.close()
        return render_template('admin_main.html')
    
    else:
        error_message = "An error occurred with your registration. If you have used our services try loging in above!"
        return render_template('main.html', error_message=error_message)

    


if __name__ == "__main__":
    app.run()