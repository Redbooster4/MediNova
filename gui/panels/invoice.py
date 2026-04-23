from . import * #from __init__.py
from db import *
from components import *
from datetime import datetime

def open_invoice(parent):
    clear(parent)
    print("Entered invoice")
    invoice_frame=ttk.Frame(master=parent, style="Content.TFrame")
    invoice_frame.pack(pady=10, fill=BOTH,expand=True)

    head=ttk.Label(master=invoice_frame, text="MediNova Invoice", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=25, padx=10)
    inv_id = Label(master=invoice_frame, text="Invoice ID: 101")
    inv_id.pack(padx=10)
    time_lbl = Label(master=invoice_frame)
    time_lbl.pack(padx=10)
    def update_time():
        now = datetime.now()
        current_time = now.strftime('%d/%m/%Y %H:%M:%S')
        time_lbl.config(text=f"Time: {current_time}")
        time_lbl.after(1000, update_time)
    update_time()
    invoice_data = fetch_sales()
    #[(1, 'Paracetamol 500mg', 100, 45.5, 4550.0, 'Analgesic', datetime.datetime(2026, 3, 28, 1, 16, 37)), ..]

    table_frame = ttk.Frame(master = invoice_frame)
    table_frame.pack(pady=10, fill=BOTH, expand=True)
    cols=("Name", "Quantity", "Price", "Total")
    tree=ttk.Treeview(
        master=table_frame,
        columns=cols,
        show="headings"
        )
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER, width=150)
    for row in invoice_data:
        tree.insert("", END, values=(row[1], row[2], row[3], row[4]))
    tree.pack(side="left", fill = BOTH, expand=True, padx=10, pady=10)
    
    def generate_invoice():
        subtotal = 0
        for row in tree.get_children():
            subtotal += float(tree.item(row)["values"][3])

        gst = subtotal * 0.05
        total = subtotal + gst
        subtotal_lbl.config(text=f"Subtotal: ₹{subtotal:.2f}")
        gstlbl.config(text=f"GST (5%): ₹{gst:.2f}")
        total_lbl.config(text=f"Total: ₹{total:.2f}")
    btn=ttk.Button(master=table_frame, text="Generate Invoice", command=generate_invoice)
    btn.pack(padx=10, pady=10)
    total_frame = ttk.Frame(master=table_frame)
    total_frame.pack(fill=X)

    subtotal_lbl=ttk.Label(master=total_frame, text="Subtotal: ₹0")
    subtotal_lbl.pack(anchor="e")

    gstlbl=ttk.Label(master=total_frame, text="GST (5%): ₹0")
    gstlbl.pack(anchor="e")

    total_lbl = ttk.Label(master=total_frame, text="Total: ")
    total_lbl.pack(anchor="e")