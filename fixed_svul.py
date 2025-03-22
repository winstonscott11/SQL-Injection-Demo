from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3
app = Flask(__name__)
app.secret_key = "basic_secret_key_for_demo"
# Database initialization
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'user'
    )
    ''')
    
    # Check if we need to insert sample users
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                      ('admin', 'admin123', 'admin'))
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                      ('user', 'user123', 'user'))
    
    conn.commit()
    conn.close()
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # FIXED CODE: Using parameterized query to prevent SQL injection
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Secure query using parameters
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        
        try:
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            
            if user:
                session['username'] = username
                session['role'] = user[3]  # Role is at index 3
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid credentials. Please try again.'
        except sqlite3.Error as e:
            error = f"Database error: {e}"
        finally:
            conn.close()
    
    return render_template('login_simple.html', error=error)
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard_simple.html', username=session['username'], role=session['role'])
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
