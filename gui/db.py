import sqlite3
import bcrypt
import mysql.connector
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        port="3307",
        database="MediNova"
    )

def create_table():
    conn = None
    try: 
        conn=get_connection()
        cur=conn.cursor()
        sql="""CREATE TABLE IF NOT EXITS login(
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL)"""
        cur.execute(sql)
        conn.commit()
    except mysql.connector.Error:
            print("Error")
    finally:
        if conn: 
            conn.close()

def hash(password):
    salt = bcrypt.gensalt()
    hashed=bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8') #to store the hashed password as a str

def check(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def register(username, password):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO login(username, password) VALUES(%s, %s)"
        cur.execute(sql, (username, hash(password)))
        conn.commit()
        Messagebox.show_info("Registration Sucess", title="SUCCESS")
        return True
    except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
    finally:
        if conn: 
            conn.close()

def login(username, password):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = """
            SELECT password FROM login WHERE username = %s
        """
        cur.execute(sql, (username, ))
        record = cur.fetchone()
        if record:
            hashed_pw=record[0]
            if check(password, hashed_pw):
                Messagebox.show_info("Logged In Success", title="Logged In")
                return True
            else:
                print("Incorrect password.")
        else:
            Messagebox.show_error("Kindly Register First", title="User Not Found")
            return False
    except mysql.connector.Error as e:
            print(f"Error:{e}")
    finally:
        if conn: 
            conn.close()

def add_medicine(med):
    conn=None
    try:
        conn=get_connection()
        cur=con.cursor()
        sql="INSERT INTO medicine() VALUES(%s, %s, %s)",(med["barcode"], med["name"], med["expiry"])
        conn.commit()
    except mysql.connector.Error:
        print("errr")
    finally:
        if conn: conn.close()


if __name__ == '__main__':
    create_table()