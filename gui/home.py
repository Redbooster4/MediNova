import subprocess
import sys
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from scanner import launch_scanner

def open_scanner():
    launch_scanner(master=window, on_result=on_scan_result)

def on_scan_result(result):
    lbl_med_name.configure(text=result["med"]["name"])
    lbl_expiry.configure(text=result["med"]["expiry"])
    btn_scan.configure(state="normal")

window = ttk.Window(themename="darkly")
window.title("Home Page")
window.geometry("1000x500")
window.resizable(False,False)

headtxt = ttk.Label(master=window, text="MediNova: Pharmacy Management", font="Calibri 25 bold")
headtxt.pack(pady=(50,10))

btn = ttk.Button(master=window, text="Scan Your Medicine", width=20, command=open_scanner)
btn.pack(pady="5")

window.mainloop()