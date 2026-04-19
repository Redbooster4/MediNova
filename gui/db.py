import sqlite3
import bcrypt
import mysql.connector
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from datetime import date, timedelta

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        port=3307,
        database="medinova"
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
    hashed=bcrypt.hashpw(password.encode('utf-8'), salt) # encode = toBytes()
    return hashed.decode('utf-8') #to store the hashed password as a str   decode ulta

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
        sql = "SELECT password FROM login WHERE username = %s"
        cur.execute(sql, (username, ))
        record = cur.fetchone()
        if record:
            hashed_pw=record[0]
            if check(password, hashed_pw):
                Messagebox.show_info("Logged In Success", title="Logged In")
                return True
            else:
                Messagebox.show_warning("Wrong username or password", title="Invalid Credentials")
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
        cur=conn.cursor()
        sql="""INSERT INTO medicine(medicine_name, barcode, category, expiry_date, 
        manufacturer, mrp, stock_qty) 
        VALUES(%s, %s, %s, %s, %s, %s, %s)"""
        cur.execute(sql, (med["medicine_name"], med["barcode"], 
        med["category"], med["expiry_date"], med["manufacturer"], 
        med["mrp"], med["stock_qty"]))
        Messagebox.show_info("Medicine Record Added !!!", title="Success")
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        
        #<class 'str'>
        #Error: 1062 (23000): Duplicate entry '8901234567891' for key 'medicine.barcode_unique'

        if(e.errno == 1062):
            Messagebox.show_error("Duplicate QR detected", "Medicine already Scanned")
        else:
            Messagebox.show_error("Invalid QR with wrong credentials", "Wrong QR")
    finally:
        if conn: conn.close()

def fetch_sales():
    conn = None
    try:
        conn=get_connection()
        cur= conn.cursor()
        sql="""
        SELECT s.id, s.medicine_id, s.qty, s.total, s.timestamp, m.category
        FROM sales s
        JOIN medicine m
        ON s.medicine_id = m.medicine_id
        """ #Not getting login_id
        cur.execute(sql)
        record = cur.fetchall()
        return record
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if conn: conn.close()

def fetch_inventory():
    conn = None
    try:
        conn=get_connection()
        cur= conn.cursor()
        sql="SELECT * FROM medicine"
        cur.execute(sql)
        record = cur.fetchall()
        return record
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if conn: conn.close()

def fetch_inventory_statistics():
    conn = None
    try:
        conn=get_connection()
        cur= conn.cursor()
        cur.execute("SELECT COUNT(*) FROM medicine")
        total_sku = cur.fetchone()[0]

        cur.execute("SELECT SUM(stock_qty) FROM medicine")
        total_revenue=cur.fetchone()[0]
    
        cur.execute("SELECT COUNT(*) FROM medicine WHERE stock_qty < 5")
        total_qty=cur.fetchone()[0]

        expiry_sql="SELECT COUNT(*) FROM medicine WHERE expiry_date BETWEEN %s AND %s"
        cur.execute(expiry_sql, (date.today(), date.today()+timedelta(days=30)))
        expiry=cur.fetchone()[0]

        return total_sku, total_revenue, total_qty, expiry
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return 0,0,0,0
    finally:
        if conn: conn.close()

def fetch_supplier():
    conn = None
    try:
        conn=get_connection()
        cur= conn.cursor()
        sql="SELECT*FROM supplier"
        cur.execute(sql)
        record=cur.fetchall()
        return record
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if conn: conn.close()

if __name__ == '__main__':
    create_table()

# # UNIT TESTING
# medi = {
#     "name":"Paracetamol 500mg",
#     "barcode":"83451008989",
#     "category":"Tablet",
#     "expiry_date":"2027-06-30",
#     "manufacturer":"Sun Pharma",
#     "mrp":250.10,
#     "stock_qty":100
# }
# add_medicine(medi)