from . import * #from __init__.py
from components import *
from db import *
from datetime import datetime

def new_purchase(parent, dict_supplier, dict_medicine):
    root = Toplevel(parent)
    root.title("New Purchase Form")
    root.geometry("510x250")
    now = datetime.now()
    label1 = Label(root, text="Supplier Name", width=20).grid(row=0, column=0)
    label2 = Label(root, text="Medicine Name", width=20).grid(row=1, column=0)
    label3 = Label(root, text="Quantity", width=20).grid(row=2, column=0)
    label4 = Label(root, text="Total", width=20).grid(row=3, column=0)

    e1 = Combobox(root, width=28, values=list(dict_supplier.keys()))
    e1.grid(row=0, column=1)
    e2 = Combobox(root, width=28, values=list(dict_medicine.keys()))
    e2.grid(row=1, column=1)
    e3 = Entry(root, width=30)
    e3.grid(row=2, column=1)
    e4 = Entry(root, width=30)
    e4.grid(row=3, column=1)
    
    def submit():
        sup_name = e1.get()
        med_name = e2.get()
        sup_id = dict_supplier.get(sup_name)
        med_id = dict_medicine.get(med_name)
        quantity = e3.get().strip()
        tot = e4.get().strip()
        
        if not sup_id or not med_id:
            Messagebox.show_error("Combobox Not Chosen", title = "ERROR")
            return
        if not quantity.isdigit():
            Messagebox.show_error("Quantity must be a number", title = "ERROR")
            return
        if not tot:
            Messagebox.show_error("Total not Valid", title = "ERROR")
            return 
        if not date:
            Messagebox.show_error("Date not Valid", title = "ERROR")
            return 
        db_date = now.strftime("%Y-%m-%d")#2026-01-15 = YYYY-MM-DD
        add_purchase(sup_id, med_id, quantity, tot, db_date)

    submit_btn = ttk.Button(master = root, text="SUBMIT", command=submit)
    submit_btn.grid(row=5, column=1, pady=10)

def update_purchase(parent, dict_supplier, dict_medicine):
    root = Toplevel(parent)
    root.title("Update Purchase Form")
    root.geometry("510x250")
    now = datetime.now()
    label0 = Label(root, text="ID", width=20).grid(row=0, column=0)
    label1 = Label(root, text="Supplier Name", width=20).grid(row=1, column=0)
    label2 = Label(root, text="Medicine Name", width=20).grid(row=2, column=0)
    label3 = Label(root, text="Quantity", width=20).grid(row=3, column=0)
    label4 = Label(root, text="Total", width=20).grid(row=4, column=0)

    e0 = Entry(root, width=30)
    e0.grid(row=0, column=1)
    e1 = Combobox(root, width=28, values=list(dict_supplier.keys()))
    e1.grid(row=1, column=1)
    e2 = Combobox(root, width=28, values=list(dict_medicine.keys()))
    e2.grid(row=2, column=1)
    e3 = Entry(root, width=30)
    e3.grid(row=3, column=1)
    e4 = Entry(root, width=30)
    e4.grid(row=4, column=1)
    
    def submit():
        id = e0.get()
        sup_name = e1.get()
        med_name = e2.get()
        sup_id = dict_supplier.get(sup_name)
        med_id = dict_medicine.get(med_name)
        quantity = e3.get().strip()
        tot = e4.get().strip()
        
        if not sup_id or not med_id:
            Messagebox.show_error("Combobox Not Chosen", title = "ERROR")
            return
        if not quantity.isdigit():
            Messagebox.show_error("Quantity must be a number", title = "ERROR")
            return
        if not tot:
            Messagebox.show_error("Total not Valid", title = "ERROR")
            return 
        if not date:
            Messagebox.show_error("Date not Valid", title = "ERROR")
            return 
        db_date = now.strftime("%Y-%m-%d")#2026-01-15 = YYYY-MM-DD
        upd_purchase(id, sup_id, med_id, quantity, tot, db_date)

    submit_btn = ttk.Button(master = root, text="SUBMIT", command=submit)
    submit_btn.grid(row=6, column=1, pady=10)

def delete_purchase(parent, dict_medicine):
    root = Toplevel(parent)
    root.title("Delete Purchase Form")
    root.geometry("510x200")
    now = datetime.now()
    label0 = Label(root, text="ID", width=20)
    label0.grid(row=0, column=0)
    e0 = Entry(root, width=30)
    e0.grid(row=0, column=1)
    label1 = Label(root, text="Medicine Name", width=20)
    label1.grid(row=1, column=0)
    e1 = Combobox(root, width=28, values=list(dict_medicine.keys()))
    e1.grid(row=1, column=1)

    def submit():
        id = e0.get()
        med_name = e1.get()
        med_id = dict_medicine.get(med_name)
        med_data = fetch_inventory()
        qty = None
        for row in med_data:
            if row[0] == med_id:
                qty = row[8]
                break

        if not id or not id.isdigit():
            Messagebox.show_error("ID not Valid", title = "ERROR")
            return 
        if not med_name or med_id is None:
            Messagebox.show_error("Please select a medicine", title="ERROR")
            return
        del_purchase(int(id), med_id, qty)

    submit_btn = ttk.Button(master = root, text="SUBMIT", command=submit)
    submit_btn.grid(row=3, column=1, pady=10)

def open_purchase(parent):
    clear(parent)
    print("Entered purchase")
    purchase_frame=ttk.Frame(master=parent, style="Content.TFrame")
    purchase_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=purchase_frame, text="PURCHASE PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=30, padx=10)
    
    purchase_data = fetch_purchases()
    #(1, 'Neev Panchal', 'Paracetamol 500mg', 200, 9100.0, datetime.date(2026, 1, 15))
    cards_frame = ttk.Frame(master=purchase_frame, style="Content.TFrame")
    cards_frame.pack(fill=X, padx=20, pady=10)

    total_purchases = len(purchase_data)
    amt_spent = sum(s[4] for s in purchase_data)
    total_qty = sum(s[3] for s in purchase_data)
    freq_supplier = top_supplier()
    #[('Neev Panchal', 3)]
    lbls=[
        ("Total Purchases Made", total_purchases), 
        ("Total Amount Spent", f"₹ {amt_spent}"), 
        ("Quantity Medicine", total_qty),
        ("Most Frequent Supplier", freq_supplier[0][0])
    ]
    for label, cmd in lbls:
        widget(cards_frame, label, cmd)

    charts_frame = ttk.Frame(master = purchase_frame)
    charts_frame.pack(pady=10, fill=BOTH, expand=True)
    cols=("ID", "Supplier Name", "Medicine Name", "Quantity", "Total")
    tree=ttk.Treeview(
        master=charts_frame,
        columns=cols,
        show="headings"
        )
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER, width=150)
    for row in purchase_data:
        tree.insert("", END, values=(row[0], row[1], row[2], row[3], row[4]))
    tree.pack(side="left", fill = BOTH, expand=True, padx=10, pady=10)

    btn_panel=ttk.Frame(charts_frame)
    btn_panel.pack(fill="x", anchor="w", pady=10)

    sup = fetch_supplier()
    #[(1, 'Neev Panchal', '7977424440', 'neev.p4@gmail.com'), ..]
    dict_supplier = {}
    for data in sup:
        dict_supplier[data[1]] = data[0]
    #{'Neev Panchal': 1, 'Reyhaan Ansari': 2, 'Amit Sharma': 3,..}

    med=fetch_inventory()
    #print(med) # [(3, 1, 'Paracetamol 500mg', '8901234567890', 'Analgesic', datetime.date(2026, 12, 31), 'Sun Pharma', 45.5, 10),
    dict_medicine = {}
    for data in med:
        dict_medicine[data[2]] = data[0]
    # print(dict_medicine) {'Paracetamol 500mg': 3, 'Amoxicillin 250mg': 8, 'Ibuprofen 400mg': 11, 'Cetirizine 10mg': 12, 'Dolo 650': 13, 'Metformin 500mg': 20}

    btns=[("Add Purchase", lambda:new_purchase(parent, dict_supplier, dict_medicine)), 
          ("Update Purchase", lambda:update_purchase(parent, dict_supplier, dict_medicine)), 
          ("Delete Purchase", lambda:delete_purchase(parent, dict_medicine)) ]
    for label, cmd in btns:
        btn = ttk.Button(btn_panel, text=label, command=cmd)
        btn.pack(side="left", padx=5)

    df = pd.DataFrame(purchase_data)
    df = df.sort_values(5)
    print(df)
    #      0  1             2                  3     4       5
    # 0    ID Neev Panchal  Paracetamol 500mg  200   9100.0  2026-01-15
    
    fig = Figure(figsize=(12, 4))
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.25, left=0.15)

    ax = fig.add_subplot(111) 
    ax.plot(df[5], df[4], marker="s")
    ax.set_xlabel("Time Stamp")
    ax.set_ylabel("Total Cost")
    ax.set_title("Purchases Line Chart")
    ax.tick_params(axis='x', rotation=30)

    plot1 = FigureCanvasTkAgg(fig, master=charts_frame) #Figure to kinter widget
    plot1.draw()
    plot1.get_tk_widget().pack(pady=10)