import tkinter as tk
from node import *
from constants import *

# Global variable flags that persist through the event loop,
# used in the event handlers
current_widget = None
initial_click = None
initial_black = False

def handle_drag(event):
    """Event handler that changes the color of the spot that is dragged over.
    Implementation inspired by this source:
    https://stackoverflow.com/
    questions/51369844/how-to-trigger-tkinters-enter-event-with-mouse-down"""
    global current_widget
    widget = event.widget.winfo_containing(event.x_root, event.y_root)
    if current_widget != widget and widget != initial_click:
        current_widget = widget
        if current_widget["bg"] == "black" or current_widget["bg"] == "#d9d9d9":
            if initial_black:
                current_widget["bg"] = "black"
            else:
                current_widget["bg"] = "#d9d9d9"

def handle_click(event):
    """Event handler that changes the  color of the spot that is clicked."""
    global initial_click
    global initial_black
    initial_click = event.widget
    if initial_click["bg"] == "#d9d9d9":
        initial_click["bg"] = "black"
        initial_black = True
    elif initial_click["bg"] == "black":
        initial_click["bg"] = "#d9d9d9"
        initial_black = False

def track_position(event, node_map):
    """Event handler that updates the current grid position in
    x and y coordinates."""
    widget = event.widget
    e = node_map.get(widget)
    print(f"{e.get_x}, {e.get.y}")

def draw_top_bar(root):
    """Sets up all widgets for the top bar of the UI."""
    frm_input = tk.Frame(master=root)

    lbl_start = tk.Button(master=frm_input, font="Helvetica 11 bold",
        text="Start ")
    lbl_start_x = tk.Label(master=frm_input, text="X:")
    ent_start_x = tk.Entry(master=frm_input, width=5)
    lbl_start_y = tk.Label(master=frm_input, text="Y:")
    ent_start_y = tk.Entry(master=frm_input, width=5)
    lbl_stop = tk.Button(master=frm_input, font="Helvetica 11 bold",
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

    btn_Astar = tk.Button(master=frm_input, text="Start A* Search",
        bg="#2f4454", fg="white")
    btn_Astar.pack(side=tk.LEFT, padx=(20,0))

    lbl_x = tk.Label(master=frm_input, text="x:")
    lbl_hover_x = tk.Label(master=frm_input, text="?")
    lbl_y = tk.Label(master=frm_input, text="y:")
    lbl_hover_y = tk.Label(master=frm_input, text="?")

    lbl_x.pack(side=tk.LEFT, padx=(100,0))
    lbl_hover_x.pack(side=tk.LEFT)
    lbl_y.pack(side=tk.LEFT)
    lbl_hover_y.pack(side=tk.LEFT)

    frm_input.pack()

def draw_grid(root, node_map):
    """Creates the grid."""
    frm_grid = tk.Frame(master=root)
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            frm = tk.Frame(
                master=frm_grid,
                relief=tk.RAISED,
                borderwidth=1,
                width=30,
                height=30
            )
            frm.grid(row=r, column=c)
            frm.bind("<Button-1>", handle_click)
            frm.bind("<B1-Motion>", handle_drag)
            frm.bind("<Enter>", lambda event: track_position(event, node_map))
            node_map.add(Node(frm, c+1, NUM_ROWS-r))
    frm_grid.pack()

def main():
    window = tk.Tk()
    map = NodeMap()
    draw_top_bar(window)
    draw_grid(window, map)
    window.mainloop()

main()
