from . import * #from __init__.py
from db import *
from components import *
import FPDF

def open_invoice(parent):
    clear(parent)
    print("Entered sales")
    invoice_data = fetch_invoice()

    sales_frame=ttk.Frame(master=parent, style="Content.TFrame")
    sales_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=sales_frame, text="INVOICE PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=25, padx=10)

    