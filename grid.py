import tkinter as tk

def handle_click(event):
    """Print the character associated to the key pressed"""
    btn = event.widget
    btn["bg"] = "black"

window = tk.Tk()

for r in range(20):
    for c in range(35):
        frm = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
            width=30,
            height=30
        )
        frm.grid(row=r, column=c)
        frm.bind("<Button-1>", handle_click)

window.mainloop()
