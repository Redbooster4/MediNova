from . import * #from __init__.py
from components import *
from db import *
import subprocess
from panels.automation import send_email

email_sent = False
def open_inventory(parent):
    global email_sent
    clear(parent)
    print("Entered inventory")
    inv_frame=ttk.Frame(master=parent, style="Content.TFrame")
    inv_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=inv_frame, text="INVENTORY PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=30, padx=10)

    cards_frame = ttk.Frame(master=inv_frame, style="Content.TFrame")
    cards_frame.pack(fill=X, padx=20, pady=10)

    total_sku, total_revenue, total_qty, expiry = fetch_inventory_statistics()
    #print("Total low stock = ", total_qty)
    #print("exp = ", expiry)
    if (total_qty>=1 or expiry>=1) and not email_sent:
        print("Trigger")
        email_sent = True
        send_email()

    cards = [("Total SKUS", total_sku),
        ("Total Units", total_revenue),
        ("Low In Stock", total_qty),
        ("Expiring Soon", expiry)]
    for label, value in cards:
        widget(cards_frame, label, value)

    charts_frame = ttk.Frame(master=inv_frame)  
    charts_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    stock_data = fetch_inventory()
    #print(stock_data)
    #(3, 1, 'Paracetamol 500mg', '8901234567890', 'Analgesic', datetime.date(2026, 12, 31), 'Sun Pharma', 45.5, 10)

    cols=("Medicine Name", "MRP", "Stock Quantity", "Expiry Date")
    tree=ttk.Treeview(
        master=charts_frame,
        columns=cols,
        show="headings"
        )
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER)
    for row in stock_data:
        tree.insert("", END, values=(row[2], row[7], row[8], row[5].strftime("%d/%m/%Y")))
    tree.pack(side="left", fill = BOTH, expand=True, padx=10, pady=10)

    btn_panel = ttk.Frame(charts_frame)
    btn_panel.pack(fill="x", anchor="w", padx=10, pady=10)
    for label, cmd in [("Notify Providers", send_email)]:
        btn = ttk.Button(btn_panel, text =label, command=cmd)
        btn.pack(side="left", padx=5)
    
    df = pd.DataFrame(stock_data)
    df = df.sort_values(5)
    # 0  1                  2              3              4           5           6      7    8
    # 2  11  1    Ibuprofen 400mg  8901234567892    Pain Relief  2026-09-10  Dr Reddy's   60.0  300
    
    fig = Figure(figsize=(12, 4))
    fig.tight_layout()
    
    ax = fig.add_subplot(111) 
    ax.pie(df[8], labels=df[2], autopct="%1.1f%%", startangle=90)
    ax.set_title("Current Inventory")
    ax.axis("equal")

    plot1 = FigureCanvasTkAgg(fig, master=charts_frame) #Figure to kinter widget
    plot1.draw()
    plot1.get_tk_widget().pack(pady=10)