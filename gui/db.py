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
            cur.close()
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
            cur.close()
            conn.close()

def login(username, password):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor(buffered=True)
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
            cur.close()
            conn.close()

def add_medicine(med):
    conn=None
    try:
        conn=get_connection()
        cur=conn.cursor()
        sql="""INSERT INTO medicine(supplier_id, medicine_name, barcode, category, expiry_date, 
        manufacturer, mrp, stock_qty) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
        cur.execute(sql, (med["supplier_id"], med["medicine_name"], med["barcode"], 
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
        if conn:
            cur.close() 
            conn.close()

def to_mail_providers():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = """
            SELECT m.medicine_name, m.stock_qty, s.email
            FROM supplier s
            JOIN medicine m
            ON m.supplier_id = s.supplier_id
            WHERE m.stock_qty<15 OR m.expiry_date BETWEEN %s AND %s
        """ 
        cur.execute(sql,(date.today(), date.today()+timedelta(days=20)))
        record = cur.fetchall()
        return record
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if conn:
            cur.close()
            conn.close()

def provider_medicine_count():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = """
            SELECT s.supplier_name, COUNT(m.medicine_id)
            FROM medicine m
            JOIN supplier s
            ON m.supplier_id = s.supplier_id
            GROUP BY s.supplier_name
        """ 
        cur.execute(sql)
        record = cur.fetchall()
        return record
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if conn:
            cur.close()
            conn.close()

def fetch_purchases():
    conn = None
    try:
        conn=get_connection()
        cur= conn.cursor()
        sql="""
            SELECT p.id, s.supplier_name, m.medicine_name, p.qty, p.total, p.date
            FROM purchases p
            JOIN supplier s
            ON p.supplier_id = s.supplier_id
            JOIN medicine m
            ON m.medicine_id = p.medicine_id
        """
        cur.execute(sql)
        record = cur.fetchall()
        return record
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if conn:
            cur.close() 
            conn.close()

def add_purchase(sup_id, med_id, qty, total, date):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO purchases(supplier_id, medicine_id, qty, total, date) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(sql, (sup_id, med_id, qty, total, date))
        conn.commit()
        Messagebox.show_info("New Record Added !", title="SUCCESS")
    except mysql.connector.Error as e:
        print(f"Err:{e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def upd_purchase(id, sup_id, med_id, qty, total, date):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql="""UPDATE purchases SET supplier_id = %s, medicine_id = %s, qty=%s, total=%s, date=%s
        WHERE id = %s"""
        cur.execute(sql, (sup_id, med_id, qty, total, date, id))
        conn.commit()
        Messagebox.show_info("Record Updated !", title="SUCCESS")
    except mysql.connector.Error as e:
        print(f"Err:{e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def top_supplier():
    conn = None
    try:
        conn=get_connection()
        cur= conn.cursor()
        sql="""
            SELECT s.supplier_name, COUNT(p.id) count
            FROM purchases p
            JOIN supplier s
            ON s.supplier_id = p.supplier_id
            GROUP BY s.supplier_name
            ORDER BY count DESC
            LIMIT 1
        """
        cur.execute(sql)
        record=cur.fetchall()
        return record
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if conn:
            cur.close() 
            conn.close()

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
        if conn:
            cur.close() 
            conn.close()

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
        if conn:
            cur.close() 
            conn.close()

def fetch_inventory_statistics():
    conn = None
    try:
        conn=get_connection()
        cur= conn.cursor()
        cur.execute("SELECT COUNT(*) FROM medicine")
        total_sku = cur.fetchone()[0]
        cur.execute("SELECT SUM(stock_qty) FROM medicine")
        total_revenue=cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM medicine WHERE stock_qty <= 15")
        total_qty=cur.fetchone()[0]
        expiry_sql="SELECT COUNT(*) FROM medicine WHERE expiry_date BETWEEN %s AND %s"
        cur.execute(expiry_sql,(date.today(), date.today()+timedelta(days=20))) # today,20 days
        expiry=cur.fetchone()[0]
        return total_sku, total_revenue, total_qty, expiry
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return 0,0,0,0
    finally:
        if conn:
            cur.close() 
            conn.close()

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
        if conn:
            cur.close() 
            conn.close()

def add_supplier(id, name, number, email):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO supplier(supplier_id, supplier_name, phone_number, email) VALUES(%s, %s, %s, %s)"
        cur.execute(sql, (id, name, number, email))
        conn.commit()
        Messagebox.show_info("New Supplier Added !", title="SUCCESS")
        return True
    except mysql.connector.Error as e:
            print(f"Error: {e}")
            if(e.errno == 1062):
                Messagebox.show_error("Duplicates Not Allowed", "Medicine already Scanned")
            return False
    finally:
        if conn: 
            cur.close()
            conn.close()

def upd_supplier(sup_id, name, number, email):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = """UPDATE supplier
        SET supplier_name = %s, phone_number = %s, email = %s
        WHERE supplier_id = %s
        """
        cur.execute(sql, (name, number, email, sup_id))
        conn.commit()
        Messagebox.show_info("Supplier Updated !", title="SUCCESS")
        return True
    except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
    finally:
        if conn: 
            cur.close()
            conn.close()

def del_supplier(sup_id):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = "DELETE FROM supplier WHERE supplier_id = %s"
        cur.execute(sql, (sup_id, ))
        conn.commit()
        Messagebox.show_info("Supplier Deleted !", title="SUCCESS")
        return True
    except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False
    finally:
        if conn: 
            cur.close()
            conn.close()

# Qr data:) 
# medi = {
#     "supplier_id": "1", or "101" .......
#     "name":"Paracetamol 500mg",
#     "barcode":"83451008989",
#     "category":"Tablet",
#     "expiry_date":"2027-06-30",
#     "manufacturer":"Sun Pharma",
#     "mrp":250.10,
#     "stock_qty":100
# }
# add_medicine(medi)