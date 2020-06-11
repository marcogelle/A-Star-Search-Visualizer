import tkinter as tk

current_widget = None
def show_info(event):
    """Intermediate event generation function. Taken from here:
    https://stackoverflow.com/questions/51369844/how-to-trigger-tkinters-enter-event-with-mouse-down"""
    global current_widget
    widget = event.widget.winfo_containing(event.x_root, event.y_root)
    if current_widget != widget:
        if current_widget:
            current_widget.event_generate("<<B1-Leave>>")
        current_widget = widget
        current_widget.event_generate("<<B1-Enter>>")

def handle_click(event):
    """Change color of the spot that is clicked"""
    btn = event.widget
    btn["bg"] = "black"

def handle_drag(event):
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
        frm.bind("<B1-Motion>", show_info)
        frm.bind("<<B1-Enter>>", handle_drag)

window.mainloop()
