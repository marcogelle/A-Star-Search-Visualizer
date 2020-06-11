import tkinter as tk

current_widget = None
def show_info(event):
    """Intermediate event generation function for mouse dragging.
    Taken from here:
    https://stackoverflow.com/
    questions/51369844/how-to-trigger-tkinters-enter-event-with-mouse-down"""
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
    """Change color of the spot that is dragged over"""
    btn = event.widget
    btn["bg"] = "black"



window = tk.Tk()

frm_input = tk.Frame(master=window)

lbl_start = tk.Label(master=frm_input, font="Helvetica 11 bold",
    text="Start ")
lbl_start_x = tk.Label(master=frm_input, text="X:")
ent_start_x = tk.Entry(master=frm_input, width=5)
lbl_start_y = tk.Label(master=frm_input, text="Y:")
ent_start_y = tk.Entry(master=frm_input, width=5)
lbl_stop = tk.Label(master=frm_input, font="Helvetica 11 bold",
    text="Destination ")
lbl_stop_x = tk.Label(master=frm_input, text="X:")
ent_stop_x = tk.Entry(master=frm_input, width=5)
lbl_stop_y = tk.Label(master=frm_input, text="Y:")
ent_stop_y = tk.Entry(master=frm_input, width=5)

lbl_start.pack(side=tk.LEFT, padx=(10,0))
lbl_start_x.pack(side=tk.LEFT)
ent_start_x.pack(side=tk.LEFT)
lbl_start_y.pack(side=tk.LEFT)
ent_start_y.pack(side=tk.LEFT)
lbl_stop.pack(side=tk.LEFT, padx=(20,0))
lbl_stop_x.pack(side=tk.LEFT)
ent_stop_x.pack(side=tk.LEFT)
lbl_stop_y.pack(side=tk.LEFT)
ent_stop_y.pack(side=tk.LEFT)



frm_input.pack()


frm_grid = tk.Frame(master=window)
for r in range(1, 1 + 25):
    for c in range(35):
        frm = tk.Frame(
            master=frm_grid,
            relief=tk.RAISED,
            borderwidth=1,
            width=30,
            height=30
        )
        frm.grid(row=r, column=c)
        frm.bind("<Button-1>", handle_click)
        frm.bind("<B1-Motion>", show_info)
        frm.bind("<<B1-Enter>>", handle_drag)
frm_grid.pack()

window.mainloop()
