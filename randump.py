import ttkbootstrap as tb
from ttkbootstrap.constants import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tb.Window(themename="flatly")

fig, ax = plt.subplots()
ax.bar(["Jan", "Feb", "Mar"], [100, 200, 150])
ax.set_title("Sales")

# Embed into window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=YES)

root.mainloop()