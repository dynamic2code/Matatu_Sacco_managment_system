from flask import Flask
from flask import render_template, request, redirect,session, flash
import datetime
import sqlite3
import bcrypt
from bcrypt import hashpw
from secrets import secret_key

app = Flask(__name__)

app.secret_key = secret_key
global driver_details

driver_details = {"all_cars": 0, "current_car_id": 0, "makings": 0}
def lining_algo(drivers_details):
    """
    This function implements a lining algorithm.

    Args:
    None.

    Returns:
    driver_details
    """
    

    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()
    # Initialize the current car ID and capacity.
    query = f"SELECT car_id FROM car ORDER BY car_id DESC LIMIT 1"
    cursor.execute(query)
    all_cars = cursor.fetchone()[0]
    driver_details["all_cars"] = all_cars
    makings = 0
    current_car_id = 0
    current_capacity = 0
    while current_car_id < all_cars:
        print(current_car_id)
        driver_details["current_car_id"] = current_car_id
        driver_details["makings"] = makings
    # Loop until the car is full.
        while current_capacity < 14:
            # Ask the user to confirm their trip.
            confirmation = confirm_trip()

            # If the user confirms their trip, increase the capacity and print the new capacity.
            if confirmation == "Confirm":
                current_capacity += 1
                print(current_capacity)
                print(driver_details) 
        
        if current_capacity == 14:
            current_car_id += 1
            makings += 200
            current_capacity = 0
        
            # If the capacity is full, increment the current car ID.

@app.route('/')
def main():
    """
    This function shows first page.

    Args:
    None.

    Returns:
    None.
    """
    if session.get('name') is not None:
        # The session exists
        if session['type'] == "pass":
            return render_template('pass_main.html')
        elif session['type'] == "driver":
            # driver_details = lining_algo()
            print(driver_details)
            return render_template('driver_main.html', driver_details = driver_details)         
        elif session['type'] == "admin":
            # driver_details = lining_algo()
            print(driver_details)
            return render_template('admin_main.html', driver_details = driver_details)
    
    else:
  # The session does not exist
        return render_template('main.html')

#pass
@app.route('/pass_register')
def pass_register():
    """
    This function shows the passanger registration page.

    Args:
    None.

    Returns:
    None.
    """
    return render_template('pass_register.html')

@app.route('/pass_register/pass_registerd', methods=['POST'])
def pass_registerd():
    """
    This function handles the passanger registration.

    Args:
    None.

    Returns:
    None.
    """
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
    conn.commit()
    if action:
        # add to session 
        session['name'] = name
        session['phone'] = phone
        session['type'] = "pass"

        cursor.close()
        conn.close()
        return render_template('pass_main.html')
    
    else:
        error_message = "An error occurred with your registration. If you have used our services try loging in above!"
        return render_template('main.html', error_message=error_message)
    

@app.route('/pass_login')
def pass_login():
    """
    This function shows the passanger log_in page.

    Args:
    None.

    Returns:
    None.
    """
    return render_template('pass_login.html')

@app.route('/pass_login/pass_main', methods=['POST'])
def pass_main():
    """
    This function handles the passangers log_in.

    Args:
    None.

    Returns:
    None.
    """
    name = request.form['name']
    phone = request.form['phone']
    password = request.form['password']
    
        # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()

    query = f"SELECT * FROM your_table WHERE name = {name} AND phone = :phone  AND password = :password"
    action = cursor.execute(query, {'name': name, 'phone': phone, 'password': password})
    if action:
        # add to session 
        session['name'] = name
        session['phone'] = phone
        session['type'] = "pass"

        cursor.close()
        conn.close()
        return render_template('pass_main.html')
    
    else:
        error_message = "An error occurred with your log in. If you have not used our services try registering in below!"
        return render_template('main.html', error_message=error_message)

@app.route('/get_destination', methods=['POST'])
def get_destination():
    """
    This function handles the passangers input on destination.

    Args:
    None.

    Returns:
    None.
    """
    stage =  request.form['Stage']
    drop_off = request.form['drop_off']

    cost = "200"

    if (stage and drop_off):
        return render_template("pass_main.html", cost = cost)
    

@app.route('/comfirm_trip', methods=['GET','POST'])
def confirm_trip():
    """
    This function is responsible for the payment request.

    Args:
    None.

    Returns:
    None.
    """
    choise = request.form['confirmation']

    if choise == "Confirm":
        flash('Action performed successfully!', 'success')

    return render_template("pass_main.html", choise = choise)

# driver


@app.route('/driver_register')
def driver_register():
    """
    This function is responsible for displaying the driver_registration.

    Args:
    None.

    Returns:
    None.
    """
    return render_template('driver_register.html')

@app.route('/driver_register/driver_registerd', methods=['POST'])
def driver_registerd():
    """
    This function is responsible for the registration for the drivers and addition of cars.

    Args:
    None.

    Returns:
    None.
    """
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
    conn.commit()
    if action:
        # add to session 
        session['name'] = name
        session['phone'] = phone
        session['type'] = "driver"
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
        conn.commit()

        return render_template('driver_main.html', driver_details = driver_details)
    
    else:
        error_message = "An error occurred with your registration. If you have used our services try loging in above!"
        return render_template('main.html', error_message = error_message)

    

@app.route('/driver_login')
def driver_login():
    """
    This function is responsible for showing the log in page.

    Args:
    None.

    Returns:
    None.
    """
    return render_template('driver_login.html')

@app.route('/driver_login/driver_main', methods=['POST'])
def driver_main():
    """
    This function is responsible for processing the login.

    Args:
    None.

    Returns:
    None.
    """
    name = request.form['name']
    phone = request.form['phone']
    password = request.form['password']


    # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()

    
    query = f"SELECT * FROM admin WHERE name = :name AND phone_number = :phone_number  AND password = :password"
    action = cursor.execute(query, {'name': name, 'phone_number': phone, 'password': password})
    if action:
        # add to session 
        session['name'] = name
        session['phone'] = phone
        session['type'] = "driver"

        cursor.close()
        conn.close()
        
        return render_template('driver_main.html', driver_details = driver_details)
    
    else:
        error_message = "An error occurred with your registration. If you have used our services try loging in above!"
        return render_template('main.html', error_message=error_message)
    

# admin


@app.route('/admin_login')
def admin_login():
    """
    This function is responsible for displaying the admin log in.

    Args:
    None.

    Returns:
    None.
    """
    return render_template('admin_login.html')

@app.route('/admin_login/admin_main', methods=['POST'])
def admin_main():
    """
    This function is responsible for processing the log in for admin.

    Args:
    None.

    Returns:
    None.
    """
    name = request.form['name']
    phone = request.form['phone']
    password = request.form['password']

    # Connect to the database
    conn = sqlite3.connect('app.db')

    # Create a cursor object
    cursor = conn.cursor()

    query = f"SELECT * FROM admin WHERE name = :name AND id_number = :id_number  AND password = :password"
    action = cursor.execute(query, {'name': name, 'id_number': phone, 'password': password})
    if action:
        # add to session 
        session['name'] = name
        session['phone'] = phone
        session['type'] = "admin"
        cursor.close()
        conn.close()


        return render_template('admin_main.html', driver_details = driver_details )
    
    else:
        error_message = "An error occurred with your registration. If you have used our services try loging in above!"
        return render_template('main.html', error_message=error_message)

    


if __name__ == "__main__":
    app.run()