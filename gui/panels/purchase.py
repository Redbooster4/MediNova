from . import * #from __init__.py
from components import *
from db import *

def open_purchase(parent):
    clear(parent)
    print("Entered purchase")
    purchase_frame=ttk.Frame(master=parent, style="Content.TFrame")
    purchase_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=purchase_frame, text="PURCHASE PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=30, padx=10)
    
    purchase_data = fetch_purchases()
    #('Neev Panchal', 'Paracetamol 500mg', 200, 9100.0, datetime.date(2026, 1, 15))

    cards_frame = ttk.Frame(master=purchase_frame, style="Content.TFrame")
    cards_frame.pack(fill=X, padx=20, pady=10)

    total_purchases = len(purchase_data)
    amt_spent = sum(s[3] for s in purchase_data)
    total_qty = sum(s[2] for s in purchase_data)
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

    charts_frame = ttk.Frame(master = purchase_frame, style="Content.TFrame")
    charts_frame.pack(pady=10, fill=BOTH, expand=True)
    cols=("Supplier Name", "Medicine Name", "Quantity", "Total")
    tree=ttk.Treeview(
        master=charts_frame,
        columns=cols,
        show="headings"
        )
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER)
    for row in purchase_data:
        tree.insert("", END, values=(row[0], row[1], row[2], row[3]))
    tree.pack(side="left", fill = BOTH, expand=True, padx=10, pady=10)
    
    df = pd.DataFrame(purchase_data)
    #print(df)
    #      0             1                  2     3       4
    # 0    Neev Panchal  Paracetamol 500mg  200   9100.0  2026-01-15
    
    fig = Figure(figsize=(12, 4))
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.25, left=0.15)
    
    ax = fig.add_subplot(111) 
    ax.plot(df[4], df[3], marker="s")
    ax.set_xlabel("Time Stamp")
    ax.set_ylabel("Total Cost")
    ax.set_title("Purchases Line Chart")
    ax.tick_params(axis='x', rotation=30)

    plot1 = FigureCanvasTkAgg(fig, master=charts_frame) #Figure to kinter widget
    plot1.draw()
    plot1.get_tk_widget().pack(pady=10)
