from . import * #from __init__.py
from db import *
from components import *

# dummy plot+problem of zooming when reusing !!

# fig = Figure(figsize=(5, 4), dpi=100)
# ax = fig.add_subplot(121)
# ax.bar(["Jan", "Feb", "Mar"], [100, 200, 150])
# ax.set_title("Monthly Sales")

#Simply Actual plots
# plt.plot(df[4], df[3])
# plt.xlabel("Time Stamp")
# plt.ylabel("Total")
# plt.title("Sales Line Chart")
# plt.show()

def open_sales(parent):
    clear(parent)
    print("Entered sales")
    sales_data = fetch_sales() #connect to db
    #print(sales_data)
    #[(1, 'Paracetamol 500mg', 100, 45.5, 4550.0, 'Analgesic', datetime.datetime(2026, 3, 28, 1, 16, 37)), ..]

    sales_frame=ttk.Frame(master=parent, style="Content.TFrame")
    sales_frame.pack(pady=10, fill=BOTH,expand=True)
    
    head=ttk.Label(master=sales_frame, text="SALES PANEL", font="Calibri 25 bold", background="#12121e")
    head.pack(pady=25, padx=10)

    cards_frame = ttk.Frame(master=sales_frame, style="Content.TFrame")
    cards_frame.pack(fill=X, padx=20, pady=10)

    total_sales = len(sales_data)
    total_revenue = sum(s[4] for s in sales_data)
    total_qty = sum(s[2] for s in sales_data)
    for label, value in [("Total Sales", total_sales), ("Revenue",f"₹ {total_revenue}"), ("Units Sold", total_qty)]:
        widget(cards_frame, label, value)

    df = pd.DataFrame(sales_data)
    print(df)
    df = df.sort_values(6) #on the basis of ts 
    # 0                      1    2      3       4            5                   6
    # 0   1  Paracetamol 500mg  100   45.5  4550.0    Analgesic 2026-03-28 01:16:37
    # 1   2  Paracetamol 500mg   50   45.5  2275.0    Analgesic 2026-04-19 18:08:27
    
    fig = Figure(figsize=(12, 4))
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.23)
    
    ax = fig.add_subplot(121) 
    ax.plot(df[6], df[4], marker="s")
    ax.set_xlabel("Time Stamp")
    ax.set_ylabel("Total Cost")
    ax.set_title("Sales Line Chart")
    ax.tick_params(axis='x', rotation=30)

    category_data = df.groupby(5)[2].sum() # Analgesic-(100+50+20) = 180..
    ax1 = fig.add_subplot(122)
    ax1.bar(category_data.index, category_data.values)
    ax1.set_title("Category-wise Sales")
    ax1.tick_params(axis='x', rotation=30)

    plot1 = FigureCanvasTkAgg(fig, master=sales_frame) #Figure to kinter widget
    plot1.draw()
    plot1.get_tk_widget().pack(pady=10)