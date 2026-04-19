from . import * #from __init__.py
from components import *
from db import *

def open_purchase(parent):
    clear(parent)
    print("Entered purchase")
    sales_frame=ttk.Frame(master=parent, style="Content.TFrame")
    sales_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=sales_frame, text="PURCHASE PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=30, padx=10)
