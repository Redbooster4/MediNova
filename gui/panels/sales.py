import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from dashboard import *

sales_data = [
    {"id": "001", "medicine": "Paracetamol", "qty": 10, "amount": 500, "date": "2025-03-10"},
    {"id": "002", "medicine": "Amoxicillin", "qty": 5,  "amount": 750, "date": "2025-03-11"},
    {"id": "003", "medicine": "Cetirizine",  "qty": 8,  "amount": 320, "date": "2025-03-12"},
    {"id": "004", "medicine": "Ibuprofen",   "qty": 12, "amount": 600, "date": "2025-03-13"},
    {"id": "005", "medicine": "Metformin",   "qty": 3,  "amount": 450, "date": "2025-03-14"},
]

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
    total_revenue = sum(s["amount"] for s in sales_data)
    total_qty = sum(s["qty"] for s in sales_data)

    for label, value in [("Total Sales", total_sales), ("Revenue (₹)", total_revenue), ("Units Sold", total_qty)]:
        widget(cards_frame, label, value)

    #/#
    ttk.Label(master=sales_frame, text="Recent Transactions", font="Calibri 13 bold",
              background="#12121e", foreground="white").pack(pady=10, padx=20, anchor=W)

    table_frame = ttk.Frame(master=sales_frame)
    table_frame.pack(fill=BOTH, expand=True, padx=20, pady=5)

    tree = ttk.Treeview(
        master=table_frame, 
        columns=("ID", "Medicine", "Qty", "Amount", "Date"),
        show="headings")

    for col in ("ID", "Medicine", "Qty", "Amount", "Date"):
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor=CENTER)

    for row in sales_data:
        tree.insert("", END, values=(row["id"], row["medicine"], row["qty"], f"₹{row['amount']}", row["date"]))

    tree.pack(fill=BOTH, expand=True)
    #@/#