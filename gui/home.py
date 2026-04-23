import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from scanner import *
from panels.sales import *
from panels.purchase import *
from panels.inventory import *
from panels.supplier import *
from panels.invoice import *

def open_scanner():
    launch_scanner(master=window)

window = ttk.Window(themename="darkly")
window.state("zoomed")#fullscreen
window.title("Home Page")
window.geometry("1000x500")

#stylingssss
style = ttk.Style()
style.configure("TopBar.TFrame", background="#1c1c2e")
style.configure("Side.TFrame", background="#2a2a3d", foreground="#7c83fd")
style.configure("Content.TFrame", background="#12121e")

frame = ttk.Frame(master=window, padding=20, style="TopBar.TFrame")
frame.pack(side=TOP, fill=X)

headtxt = ttk.Label(master=frame, text="MediNova: Pharmacy Management", font="Calibri 30 bold",
background="#1c1c2e", foreground="#e0e0e0")
headtxt.pack(pady=18,padx=30)
btn = ttk.Button(master=frame, text="Scan Your Medicine", width=20, command=open_scanner)
btn.pack(anchor=E)

main_area = ttk.Frame(master=window)
main_area.pack(side=TOP, fill=BOTH, expand=True)

sideBar=ttk.Frame(master=main_area, style="Side.TFrame", width=220)
sideBar.pack(padx=10, pady=10, side=LEFT, fill=Y)
sideBar.pack_propagate(False)

content_frame = ttk.Frame(master=main_area)
content_frame.pack(side=LEFT, fill=BOTH, expand=True)
open_sales(content_frame)
nav_button = [ #dictionary of tupless /for btns
        ("Sales", lambda: open_sales(content_frame)),
        ("Purchases", lambda: open_purchase(content_frame)),
        ("Inventory", lambda: open_inventory(content_frame)),
        ("Suppliers", lambda: open_supplier(content_frame)),
        ("Invoice", lambda:open_invoice(content_frame))
    ]
for txt, cmd in nav_button:
    btn=ttk.Button(master=sideBar, text=txt, bootstyle="outline-light", width=25, command=cmd)
    btn.pack(pady=8, padx=10)
window.mainloop()