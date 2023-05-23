from flask import Flask
from flask import render_template, request, redirect
import datetime
import sqlite3
import bcrypt
from bcrypt import hashpw

app = Flask(__name__)


def lining_algo():
    # current car points to the id of the car in line
    current_car = 0
    # fetch capacity of car with the id == current car from db
    full_cappacity = 14

    #getting current car capacity
    current_capacity = 0
    if comfirm_trip():
        current_capacity += 1
    
    if current_capacity == full_cappacity:
        current_car += 1
        current_capacity = 0

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
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()


    query = f"INSERT INTO passanger (name, password, phone, email) VALUES ('{name}', '{password}', {phone}, '{email}')"
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

@app.route('/get_destination')
def get_destination():
    stage =  request.form['stage']
    drop_off = request.form['drop_off']

    cost = 200

    if (stage and drop_off):
        return cost
@app.route('/comfirm_trip', methods=['POST'])
def comfirm_trip():
    if request.form['name'] == "Confirm":
        return True
    else:
        return False

# driver
@app.route('/driver_register')
def driver_register():
    return render_template('driver_register.html')

@app.route('/driver_register/driver_registerd', methods=['POST'])
def driver_registerd():
    name = request.form['name']
    id = request.form['id']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    plates = request.form['plates']
    capacity = request.form['capacity']

    # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()

    query = f"INSERT INTO driver (name, id_number, email, phone_number, password) VALUES ('{name}', '{id}', '{email}', '{phone}', '{password}')"
    action = cursor.execute(query)
    if action:
        driver_id = cursor.lastrowid
        cursor.close()
        conn.close()

        current_capacity = 0 
        trips_today = 0
        # Connect to the database
        conn = sqlite3.connect('app.db')

        # Create a cursor object
        cursor = conn.cursor()
        car_query = f"INSERT INTO car (driver_id, full_capacity, plates, current_capacity, trips_today) VALUES ('{driver_id}', '{capacity}', '{plates}', {current_capacity},{trips_today})"
        cursor.execute(car_query)
        

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

    
    query = f"SELECT * FROM admin WHERE name = {name} AND number ={phone}  AND password = {password}"
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

    query = f"SELECT * FROM admin WHERE name = {name} AND number ={phone}  AND password = {password}"
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