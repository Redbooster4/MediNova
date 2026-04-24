from . import * #from __init__.py
from db import *
from components import *
from tkinter import *
from ttkbootstrap.dialogs import Messagebox

def new_supplier(parent):
    print("Inside new Supplier")
    root = Toplevel(parent)
    root.title("Add Supplier Form")
    root.geometry("500x200")
    label1 = Label(root, text="ID", width=20).grid(row=0, column=0)
    label2 = Label(root, text="Name", width=20).grid(row=1, column=0)
    label3 = Label(root, text="Phone Number", width=20).grid(row=2, column=0)
    label4 = Label(root, text="Email", width=20).grid(row=3, column=0)

    e1 = Entry(root, width=30)
    e1.grid(row=0, column=1)
    e2 = Entry(root, width=30)
    e2.grid(row=1, column=1)
    e3 = Entry(root, width=30)
    e3.grid(row=2, column=1)
    e4 = Entry(root, width=30)
    e4.grid(row=3, column=1)
    
    def submit():
        id = e1.get().strip()
        name = e2.get().strip()
        number = e3.get().strip()
        email = e4.get().strip()
        if not id.isdigit():
            Messagebox.show_error("ID must be a number", title = "ERROR")
            return
        if not name:
            Messagebox.show_error("Name must not be empty", title = "ERROR")
            return
        if not number.isdigit() and len(number) <= 10:
            Messagebox.show_error("Phone number not Valid", title = "ERROR")
            return 
        if not email:
            Messagebox.show_error("Email not Valid", title = "ERROR")
            return 
        add_supplier(id, name, number, email)

    submit_btn = ttk.Button(master = root, text="SUBMIT", command=submit)
    submit_btn.grid(row=4, column=1, pady=10)

def update_supplier(parent):
    print("Inside update Supplier")
    root = Toplevel(parent)
    root.title("Update Supplier Form")
    root.geometry("500x200")
    label1 = Label(root, text="ID", width=20).grid(row=0, column=0)
    label2 = Label(root, text="Name", width=20).grid(row=1, column=0)
    label3 = Label(root, text="Phone Number", width=20).grid(row=2, column=0)
    label4 = Label(root, text="Email", width=20).grid(row=3, column=0)

    e1 = Entry(root, width=30)
    e1.grid(row=0, column=1)
    e2 = Entry(root, width=30)
    e2.grid(row=1, column=1)
    e3 = Entry(root, width=30)
    e3.grid(row=2, column=1)
    e4 = Entry(root, width=30)
    e4.grid(row=3, column=1)
    
    def submit():
        id = e1.get().strip()
        name = e2.get().strip()
        number = e3.get().strip()
        email = e4.get().strip()
        if not id or not id.isdigit():
            Messagebox.show_error("ID must be a number", title = "ERROR")
            return
        if not name:
            Messagebox.show_error("Name must not be empty", title = "ERROR")
            return
        if not number.isdigit() and len(number) <= 10:
            Messagebox.show_error("Phone number not Valid", title = "ERROR")
            return 
        if not email:
            Messagebox.show_error("Email not Valid", title = "ERROR")
            return 
        else:
            upd_supplier(id, name, number, email)

    submit_btn = ttk.Button(master = root, text="SUBMIT", command=submit)
    submit_btn.grid(row=4, column=1, pady=10)

def delete_supplier(parent):
    print("Inside update Supplier")
    root = Toplevel(parent)
    root.title("Delete Supplier Form")
    root.geometry("500x200")
    label1 = Label(root, text="Enter ID: ", width=20).grid(row=0, column=0)
    e1 = Entry(root, width=30)
    e1.grid(row=0, column=1)
    
    def submit():
        id = e1.get().strip()
        if not id or not id.isdigit():
            Messagebox.show_error("ID must be a number", title = "ERROR")
            return
        else:
            del_supplier(id)

    submit_btn = ttk.Button(master = root, text="SUBMIT", command=submit)
    submit_btn.grid(row=4, column=1, pady=10)

def open_supplier(parent):
    clear(parent)
    print("Entered suppliers")
    supplier_data = fetch_supplier() #getting from db
    print(supplier_data)

    supplier_frame=ttk.Frame(master=parent, style="Content.TFrame")
    supplier_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=supplier_frame, text="SUPPLIER PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=25, padx=10)

    table_frame = ttk.Frame(master=supplier_frame)
    table_frame.pack(fill=BOTH, expand=True, padx=20, pady=5)
    
    cols=("ID", "Name", "Contact Number", "Email")
    tree=ttk.Treeview (
        master=table_frame,
        columns=cols,
        show="headings"
        )
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER)
    for row in supplier_data:
        tree.insert("", END, values=(row[0], row[1], row[2], row[3]))
    tree.pack(fill = Y, side="left", anchor="nw", padx=10, pady=15)

    btns = [
        ("Add Supplier", lambda: new_supplier(parent)),
        ("Update Supplier", lambda: update_supplier(parent)), 
        ("Delete Supplier", lambda: delete_supplier(parent)), 
    ]
    btn_panel = ttk.Frame(table_frame)
    btn_panel.pack(fill="y", padx=10, pady=10)

    for label, cmd in btns:
        btn = ttk.Button(btn_panel, text =label, command=cmd)
        btn.pack(side="left", fill=X, padx=10, pady=5)

    supplier_data = provider_medicine_count()
    print(supplier_data)
    #[('Neev Panchal', 4)]

    df = pd.DataFrame(supplier_data)
    
    fig = Figure(figsize=(12, 4))
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.2)
    
    ax = fig.add_subplot(111) 
    ax.bar(df[0], df[1])
    ax.set_title("Provider Distribution")
    ax.axis("equal")
    ax.tick_params(axis="x", rotation=30)

    plot1 = FigureCanvasTkAgg(fig, master=table_frame) #Figure to kinter widget
    plot1.draw()
    plot1.get_tk_widget().pack(padx=5)