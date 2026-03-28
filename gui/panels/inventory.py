import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from dashboard import *
from db import *

def open_inventory(parent):
    clear(parent)
    print("Entered inventory")
    inv_frame=ttk.Frame(master=parent, style="Content.TFrame")
    inv_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=inv_frame, text="INVENTORY PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=30, padx=10)

    cards_frame = ttk.Frame(master=inv_frame, style="Content.TFrame")
    cards_frame.pack(fill=X, padx=20, pady=10)

    total_sku, total_revenue, total_qty, expiry = fetch_inventory_statistics()

    for label, value in [("Total SKUS", total_sku), ("Total Units", total_revenue), ("Low Stock Sold", total_qty), ("Expiring Soon", expiry)]:
        widget(cards_frame, label, value)

    charts_frame = ttk.Frame(master=inv_frame, style="Content.TFrame")  
    charts_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    stock_data = {row[1]: row[7] for row in fetch_inventory()}
    