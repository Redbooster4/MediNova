import sqlite3
import bcrypt

def create_table():
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )''')
    conn.commit()
    conn.close()

def hash(password):
    salt = bcrypt.gensalt()
    hashed=bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8') #to store the hashed password as a str

def check(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def register(username, password):
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()
    try:
        hashed_pw = hash(password)
        cursor.execute('''INSERT INTO users(username,password_hash) VALUES (?, ?)''',(username, hashed_pw))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error!!")
    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()
    cursor.execute('SELECT password_hash FROM users WHERE username = ?',(username,))
    record = cursor.fetchone()
    conn.close()
    if record:
        hashed_pw=record[0]
        if check(password, hashed_pw):
            print(f"User '{username}' logged in successfully.")
            return True
        else:
            print("Incorrect password.")
    else:
        print(f"Error: User '{username}' not found.")
    return False
if __name__ == '__main__':
    create_table()
    register("testuser", "securepassword123")

    login("testuser", "securepassword123")
    login("testuser", "wrongpassword")
