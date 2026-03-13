import subprocess
import sys
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
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

# Style for the Frame
# style = ttk.Style()
# style.configure(background="white")
# style.configure("SideBar.TFrame", background="lightblue")

frame = ttk.Frame(master=window, padding=20, bootstyle="darkly")
frame.pack(side=TOP, fill=X, pady=0)

headtxt = ttk.Label(master=frame, text="MediNova: Pharmacy Management", font="Calibri 30 bold")
headtxt.pack(pady=18,padx=30)
btn = ttk.Button(master=frame, text="Scan Your Medicine", width=20, command=open_scanner)
btn.pack(anchor=E)

main_area = ttk.Frame(master=window)
main_area.pack(side=TOP, fill=BOTH, expand=True)

sideBar=ttk.Frame(master=main_area, bootstyle="secondary", width=180)
sideBar.pack(side=LEFT, fill=Y)
sideBar.pack_propagate(False)

nav_button = {"Sales":open_sales, "Inventory":open_inventory, "Purchases":open_purchase, "Ledger":open_ledger, "Report":open_report}
for btn_txt,cmd in nav_button:
    btn=ttk.Button(master=sideBar, text=btn_txt, bootstyle="outline-light", width=25, command=cmd)
    btn.pack(pady=8, padx=10)

def clear():
    for widget in content_frame.winfo_children():
        widget.destroy()

def open_sales():
    clear()

def open_inventory():
    clear()

def open_purchase():
    clear()

def open_ledger():
    clear()

def open_report():
    clear()

lbl = ttk.Label(
    master=main_area,
    text="DashBoard",
    font=("Helvetica", 13, "bold"),
    bootstyle="inverse-secondary"
).pack(pady=20, padx=10)

content_frame = ttk.Frame(master=main_area)
content_frame.pack(side=LEFT, fill=BOTH, expand=True)

window.mainloop()