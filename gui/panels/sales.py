import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from dashboard import *
from db import fetch_sales

sales_data = fetch_sales() #connect to db
#print(sales_data)

def open_sales(parent):
    clear(parent)
    print("Entered sales")
    sales_frame=ttk.Frame(master=parent, style="Content.TFrame")
    sales_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=sales_frame, text="SALES PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=30, padx=10)

    cards_frame = ttk.Frame(master=sales_frame, style="Content.TFrame")
    cards_frame.pack(fill=X, padx=20, pady=10)

    total_sales = len(sales_data)
    total_revenue = sum(s[3] for s in sales_data)
    total_qty = sum(s[2] for s in sales_data)

    for label, value in [("Total Sales", total_sales), ("Revenue (₹)", total_revenue), ("Units Sold", total_qty)]:
        widget(cards_frame, label, value)

    second_lbl=ttk.Label(master=sales_frame, text="Recent Transactions", font="Calibri 13 bold",
              background="#12121e", foreground="white")
    second_lbl.pack(pady=10, padx=20, anchor=W)

    table_frame = ttk.Frame(master=sales_frame)
    table_frame.pack(fill=BOTH, expand=True, padx=20, pady=5)
    cols=("ID", "Medicine", "Qty", "Total", "Time Stamp")

    tree=ttk.Treeview(
        master=table_frame, 
        columns=cols,
        show="headings")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor=CENTER)

    for row in sales_data:
        tree.insert("", END, values=(row[0], row[1], row[2], row[3], row[4]))

    tree.pack(fill=BOTH, expand=True)