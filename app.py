from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# ✅ INIT DB
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS USERS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        gender TEXT,
        hobbies TEXT,
        country TEXT
    )
''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    hobbies = ', '.join(request.form.getlist('hobbies'))
    country = request.form['country']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO USERS (name, email, gender, hobbies, country)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, email, gender, hobbies, country))
    conn.commit()
    conn.close()

    return "✅ Data Stored in Database!"

if __name__ == '__main__':
    init_db()  # ✅ Call the function with parentheses
    app.run(debug=True)
