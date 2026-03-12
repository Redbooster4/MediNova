import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import subprocess
import sys

def launch_home():
    window.destroy()
    subprocess.Popen([sys.executable, "home.py"])

def on_click(event):
    window = ttk.Window(themename="darkly")
    window.grab_set()#inorder to direct all the user events to this modal window
    window.title("Register Page")
    window.geometry("1000x500")
    headtxt = ttk.Label(master=window, text="Register Now", font="Calibri 25 bold")
    headtxt.pack()
    var_email = tk.StringVar()
    var_pass = tk.StringVar()

    frame = ttk.Frame(master=window)
    email = ttk.Entry(master=window, textvariable=var_email, width=40)
    email.pack(pady=(80,0))
    passw = ttk.Entry(master=window, textvariable=var_pass, width=40)
    passw.pack(pady=7)
    back= ttk.Label(master=window, text="Already Registered ??", cursor="hand2")
    back.pack()
    #Anonymous func to destroy the window
    back.bind("<Button-1>", lambda e: window.destroy())

    btn = ttk.Button(master=window, text="Register", width=20)
    btn.pack(pady="5")
    frame.pack()
    
window = ttk.Window(themename="darkly")
window.title("Login Page")
window.geometry("1000x500")
window.resizable(False,False)

headtxt = ttk.Label(master=window, text="MediNova: Pharmacy Management", font="Calibri 25 bold")
headtxt.pack(pady=(50,10))

var_email = tk.StringVar()
var_pass = tk.StringVar()

frame = ttk.Frame(master=window)

email = ttk.Entry(master=window, textvariable=var_email, width=40)
email.pack(pady=(50,0))
passw = ttk.Entry(master=window, textvariable=var_pass, width=40)
passw.pack(pady=7)
register_link= ttk.Label(master=window, text="Not yet registered ??", cursor="hand2")
register_link.pack()
register_link.bind("<Button-1>", on_click)

btn = ttk.Button(master=window, text="Login", width=20, command=launch_home)
btn.pack(pady="5")
frame.pack()


window.mainloop()