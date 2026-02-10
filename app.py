from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# ------------------------
# MySQL Configuration
# ------------------------


app.secret_key = os.getenv('SECRET_KEY')

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT'))


mysql = MySQL(app)

# ------------------------
# Pages
# ------------------------

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/register-page')
def register_page():
    return render_template('register.html')

# ------------------------
# Register API
# ------------------------

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'message': 'Invalid request'}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        cursor.close()
        return jsonify({'message': 'Email already registered'}), 409

    hashed_password = generate_password_hash(password)

    cursor.execute(
        "INSERT INTO users (email, password) VALUES (%s, %s)",
        (email, hashed_password)
    )
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'Registration successful'}), 201

# ------------------------
# Login API
# ------------------------

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'message': 'Invalid request'}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT id, email, password FROM users WHERE email = %s",
        (email,)
    )
    user = cursor.fetchone()
    cursor.close()

    if not user:
        return jsonify({'message': 'Invalid email or password'}), 401

    user_id, user_email, hashed_password = user

    if not check_password_hash(hashed_password, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Create session
    session['user_id'] = user_id
    session['user_email'] = user_email

    return jsonify({'message': 'Login successful'}), 200

# ------------------------
# Portfolio (Protected)
# ------------------------

@app.route('/portfolio')
def portfolio():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))

    return render_template(
        'portfolio.html',
        email=session.get('user_email')
    )

# ------------------------
# Logout
# ------------------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))

# ------------------------
# Run App
# ------------------------

if __name__ == '__main__':
    app.run(debug=True)
