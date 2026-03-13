import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
import subprocess
import sys
import db
db.create_table()

def launch_home():
    window.destroy()
    subprocess.Popen([sys.executable, "home.py"])

def handle_login():
    uname = uname_login.get().strip()
    passw = pass_login.get().strip()
    if not uname or not passw:
        Messagebox.show_error("Please fill in all fields.", title="Error")
        return
    if db.login(uname, passw):
        window.destroy()
        subprocess.Popen([sys.executable, "home.py"])
    else:
        Messagebox.show_error("Invalid credentials!", title="Login Failed")

def on_click(event):
    window = ttk.Window(themename="darkly")
    window.grab_set()#inorder to direct all the user events to this modal window
    window.title("Register Page")
    window.geometry("1000x500")
    headtxt = ttk.Label(master=window, text="Register Now", font="Calibri 25 bold")
    headtxt.pack()
    uname_register = tk.StringVar()
    pass_register = tk.StringVar()

    frame = ttk.Frame(master=window)
    email = ttk.Entry(master=window, textvariable=uname_register, width=40)
    email.pack(pady=(80,0))
    passw = ttk.Entry(master=window, textvariable=pass_register, width=40, show="*")
    passw.pack(pady=7)
    back= ttk.Label(master=window, text="Already Registered ??", cursor="hand2")
    back.pack()
    #Anonymous func to destroy the window
    back.bind("<Button-1>", lambda e:window.destroy())

    def handle_register():
        uname = uname_register.get().strip()
        passw = pass_register.get().strip()
        if not uname or not passw:
            Messagebox.show_error("Please fill in all fields.", title="Error")
            return
        if db.register(uname, passw):
            window.destroy()
            Messagebox.show_info("Registered SuccessFully !", title="Success")
        else:
            Messagebox.show_error("Invalid credentials!", title="Login Failed")
    
    btn = ttk.Button(master=window, text="Register", width=20, command=handle_register)
    btn.pack(pady="5")
    frame.pack()
    
window = ttk.Window(themename="darkly")
window.title("Login Page")
window.geometry("1000x500")
window.resizable(False,False)

headtxt = ttk.Label(master=window, text="MediNova: Pharmacy Management", font="Calibri 25 bold")
headtxt.pack(pady=(50,10))

uname_login = tk.StringVar()
pass_login = tk.StringVar()

frame = ttk.Frame(master=window)

email = ttk.Entry(master=window, textvariable=uname_login, width=40)
email.pack(pady=(50,0))
passw = ttk.Entry(master=window, textvariable=pass_login, width=40, show="*")
passw.pack(pady=7)
register_link= ttk.Label(master=window, text="Not yet registered ??", cursor="hand2")
register_link.pack()
register_link.bind("<Button-1>", on_click)

btn = ttk.Button(master=window, text="Login", width=20, command=handle_login)
btn.pack(pady="5")
frame.pack()


window.mainloop()