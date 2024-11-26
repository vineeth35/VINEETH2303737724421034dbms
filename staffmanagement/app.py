from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'gowtham'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'  # Replace with your MySQL host
app.config['MYSQL_USER'] = 'root'     # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = '12345678'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'restaurant'   # Replace with your MySQL database name
mysql = MySQL(app)

# Route to display the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to display the staff list
@app.route('/staff')
def staff():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM staff")  # Fetch all staff details
    staff_members = cur.fetchall()
    cur.close()
    return render_template('staff.html', staff=staff_members)

# Route to add a new staff member
@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        staff_name = request.form['staff_name']
        position = request.form['position']
        salary = request.form['salary']
        
        # Insert into the staff table in the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO staff (staff_name, position, salary) VALUES (%s, %s, %s)", 
                    (staff_name, position, salary))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('staff'))  # Redirect to the staff list

    return render_template('add_staff.html')  # If GET request, display the form to add staff

# Route to delete a staff member
@app.route('/delete/<int:staff_id>', methods=['GET'])
def delete(staff_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM staff WHERE staff_id = %s", (staff_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('staff'))

# Route to update a staff member
@app.route('/update/<int:staff_id>', methods=['POST', 'GET'])
def update(staff_id):
    if request.method == 'POST':
        staff_name = request.form['staff_name']
        position = request.form['position']
        salary = request.form['salary']
        
        # Update staff details in the database
        cur = mysql.connection.cursor()
        cur.execute("UPDATE staff SET staff_name = %s, position = %s, salary = %s WHERE staff_id = %s",
                    (staff_name, position, salary, staff_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('staff'))  # Redirect to staff list after update
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM staff WHERE staff_id = %s", (staff_id,))
    staff_member = cur.fetchone()
    cur.close()
    return render_template('edit_staff.html', staff=staff_member)  # If GET request, show staff details in the form

if __name__ == "__main__":
    app.run(debug=True)
