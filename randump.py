import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename="flatly")

# Left Frame
frame_left = tb.Frame(root, bootstyle="primary", width=200, height=100)
frame_left.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=YES)

# Right Frame
frame_right = tb.Frame(root, bootstyle="secondary", width=200, height=100)
frame_right.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=YES)

root.mainloop()
