from tkinter import *
# from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def clear(parent):
    for widget in parent.winfo_children():
        widget.destroy()

def widget(parent, text, val):
    card=Frame(master=parent, background="#2a2a3d", padx=20, pady=15)
    card.pack(side=LEFT, padx=10)
    
    head=Label(master=card, text=text, background="#2a2a3d", foreground="#aaaaaa", font="Calibri 11")
    head.pack()
    number=Label(master=card, text=str(val), background="#2a2a3d", foreground="#ffffff", font="Calibri 20 bold")
    number.pack()