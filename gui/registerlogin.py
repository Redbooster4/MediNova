from tkinter import *
#from ttkbootstrap import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from db import *
import subprocess
import sys

def launch_home():
    window.destroy()
    subprocess.Popen(["python","home.py"])

def handle_login():
    uname = uname_login.get().strip()
    passw = pass_login.get().strip()
    if not uname or not passw:
        Messagebox.show_error("Please fill in all fields", title="Error")
        return
    if login(uname, passw):
        launch_home()
    
#validator funcs
def isUserName(x):
    if x.isdigit():
        Messagebox.show_error("Numbers not allowed", title="Input Error")
        return False
    else:
        return True

def on_click(event):
    r_window = Toplevel(window)
    r_window.title("Register Page")
    r_window.geometry("1000x500")
    headtxt = ttk.Label(master=r_window, text="Register Now", font="Calibri 25 bold")
    headtxt.pack(pady=10)
    uname_register=StringVar()
    pass_register=StringVar()

    ttk.Label(master=r_window, text="Username").pack(pady=(40,0))
    user = ttk.Entry(master=r_window, textvariable=uname_register, width=40)
    user.pack()
    ttk.Label(master=r_window, text="Password").pack(pady=(10,0))
    passw = ttk.Entry(master=r_window, textvariable=pass_register, width=40, show="*")
    passw.pack()
    back= ttk.Label(master=r_window, text="Already Registered ??", cursor="hand2")
    back.pack(pady=30)
    #Anonymous func to destroy the r_window
    back.bind("<Button-1>", lambda e:r_window.destroy())
    def handle_register():
        register_uname = uname_register.get().strip()
        register_passw = pass_register.get().strip()
        if not register_uname or not register_passw:
            Messagebox.show_error("Please fill in all fields", title="Error")
            return
        if register(register_uname, register_passw):
            r_window.destroy()
        else:
            Messagebox.show_error("Invalid credentials!", title="Registration Failed")
    
    btn = ttk.Button(master=r_window, text="Register", width=20, command=handle_register, bootstyle="success")
    btn.pack(pady=5)
    
window = ttk.Window(themename="darkly")
window.title("Login Page")
window.geometry("1000x500")
window.resizable(False,False)

headtxt = ttk.Label(master=window, text="MediNova: Pharmacy Management", font="Calibri 25 bold")
headtxt.pack(pady=(50,10))

uname_login = StringVar()
pass_login = StringVar()

user_validate=window.register(isUserName)
ttk.Label(master=window, text="Username").pack(pady=(40,0))
usern = ttk.Entry(master=window, textvariable=uname_login, width=40, validate="key", validatecommand=(user_validate, '%P'))
usern.pack()
ttk.Label(master=window, text="Password").pack(pady=(10,0))
passw = ttk.Entry(master=window, textvariable=pass_login, width=40, show="*")
passw.pack()

register_link= ttk.Label(master=window, text="Not yet registered ??", cursor="hand2")
register_link.pack()
register_link.bind("<Button-1>", on_click)

btn = ttk.Button(master=window, text="Login", width=20, command=handle_login, bootstyle="success")
btn.pack(pady=30)
window.bind("<Return>", lambda e: handle_login())
window.mainloop()