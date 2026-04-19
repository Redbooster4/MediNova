import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from db import login, register
import subprocess
import sys

def launch_home():
    window.destroy()
    subprocess.run([sys.executable, "home.py"])

def handle_login():
    uname = uname_login.get().strip()
    passw = pass_login.get().strip()
    if not uname or not passw:
        Messagebox.show_error("Please fill in all fields", title="Error")
        return
    if login(uname, passw):
        window.destroy()
        subprocess.run([sys.executable, "home.py"])
    
#validator funcs
def isUserName(x)->bool:
    if x.isdigit():
        Messagebox.show_error("Numbers not allowed", title="Input Error")
        return False
    else:
        return True

def on_click(event):
    r_window = tk.Toplevel(window)
    r_window.title("Register Page")
    r_window.geometry("1000x500")
    headtxt = ttk.Label(master=r_window, text="Register Now", font="Calibri 25 bold")
    headtxt.pack()
    uname_register = tk.StringVar()
    pass_register = tk.StringVar()

    frame = ttk.Frame(master=r_window)
    user = ttk.Entry(master=r_window, textvariable=uname_register, width=40)
    user.pack(pady=(80,0))
    passw = ttk.Entry(master=r_window, textvariable=pass_register, width=40, show="*")
    passw.pack(pady=7)
    back= ttk.Label(master=r_window, text="Already Registered ??", cursor="hand2")
    back.pack()
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
    
    btn = ttk.Button(master=r_window, text="Register", width=20, command=handle_register)
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

user_validate=window.register(isUserName)

usern = ttk.Entry(master=window, textvariable=uname_login, width=40, validate="focus", validatecommand=(user_validate, '%P'))
usern.pack(pady=(50,0))
passw = ttk.Entry(master=window, textvariable=pass_login, width=40, show="*")
passw.pack(pady=7)

register_link= ttk.Label(master=window, text="Not yet registered ??", cursor="hand2")
register_link.pack()
register_link.bind("<Button-1>", on_click)

btn = ttk.Button(master=window, text="Login", width=20, command=handle_login)
btn.pack(pady="5")
frame.pack()


window.mainloop()