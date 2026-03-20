import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def open_inventory(parent, clear, widget):
    clear()
    print("Entered inventory")
    sales_frame=ttk.Frame(master=parent, style="Content.TFrame")
    sales_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=sales_frame, text="INVENTORY PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=30, padx=10)