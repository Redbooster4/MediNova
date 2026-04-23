# import tkinter as tk

# root = tk.Tk()
# root.title("Sticky Example")

# # Configure the grid to expand with the window
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# # Create a label and make it stick to all sides of its cell
# label = tk.Label(root, text="I will stick and expand", bg="lightblue")
# label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10) #

# root.mainloop()

# FILE OPENING

# #https://pythonassets.com/posts/browse-file-or-folder-in-tk-tkinter/
# from tkinter import filedialog
# from tkinter import *
# root = Tk()
# root.title("Main Window")
# def browse():
#     # for directory=> directory = filedialog.askdirectory()
#     filename = filedialog.askopenfilename(
#     parent=root,
#     title="Browse File"
#     )
#     print(filename)

# browsebtn = Button(
#     master=root,
#     text="BROWSE",
#     command=browse
# )
# browsebtn.pack()
# root.mainloop()