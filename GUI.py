import tkinter as tk

from node import *
from constants import *

class GUI:
    """When a GUI instance is created, the GUI for this project is set up
    on the given tkinter window."""

    def __init__(self, root, node_map):
        self.root = root
        self.node_map = node_map
        self.start_node = None
        self.dest_node = None

        # Flags for holding info during the event loop. Used by event handlers.
        self.current_widget = None
        self.initial_click = None
        self.initial_black = False

        self.__draw_top_bar()
        self.__draw_grid()

    def __draw_top_bar(self):
        """Sets up all widgets for the top bar of the UI."""
        frm_input = tk.Frame(master=self.root)
        self.__draw_start_input(frm_input)
        self.__draw_destination_input(frm_input)
        self.__draw_start_buttons(frm_input)
        self.__draw_position_tracker(frm_input)
        frm_input.pack()

    def __draw_grid(self):
        """Creates the grid."""
        frm_grid = tk.Frame(master=self.root)
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                frm = tk.Frame(
                    master=frm_grid,
                    relief=tk.RIDGE,
                    borderwidth=1,
                    width=SPOT_SIZE,
                    height=SPOT_SIZE
                )
                frm.grid(row=r, column=c)
                frm.bind("<Button-1>", self.__handle_click)
                frm.bind("<B1-Motion>", self.__handle_drag)
                frm.bind("<Enter>", lambda event: self.__track_position(event))
                self.node_map.add(Node(frm, c, NUM_ROWS-r-1, self.node_map))
        frm_grid.pack()

    def __draw_start_input(self, frame):
        """Sets up widgets for inputting the starting position."""
        def draw_start():
            x, y = ent_start_x.get(), ent_start_y.get()
            node = self.node_map.get_from_pos(x, y)
            node.get_frm()["bg"] = "red"
            if self.start_node:
                self.start_node.get_frm()["bg"] = "#d9d9d9"
            self.start_node = node

        btn_start = tk.Button(master=frame, font="Helvetica 11 bold",
            text="Start ", command=draw_start)
        lbl_start_x = tk.Label(master=frame, text="X:")
        ent_start_x = tk.Entry(master=frame, width=5)
        lbl_start_y = tk.Label(master=frame, text="Y:")
        ent_start_y = tk.Entry(master=frame, width=5)

        btn_start.pack(side=tk.LEFT, padx=(10,0))
        lbl_start_x.pack(side=tk.LEFT)
        ent_start_x.pack(side=tk.LEFT)
        lbl_start_y.pack(side=tk.LEFT)
        ent_start_y.pack(side=tk.LEFT)

    def __draw_destination_input(self, frame):
        """Sets up widgets for inputting the destination position."""
        def draw_dest():
            x, y = ent_dest_x.get(), ent_dest_y.get()
            node = self.node_map.get_from_pos(x, y)
            node.get_frm()["bg"] = "green"
            if self.dest_node:
                self.dest_node.get_frm()["bg"] = "#d9d9d9"
            self.dest_node = node
        lbl_dest = tk.Button(master=frame, font="Helvetica 11 bold",
            text="Destination ", command=draw_dest)
        lbl_dest_x = tk.Label(master=frame, text="X:")
        ent_dest_x = tk.Entry(master=frame, width=5)
        lbl_dest_y = tk.Label(master=frame, text="Y:")
        ent_dest_y = tk.Entry(master=frame, width=5)

        lbl_dest.pack(side=tk.LEFT, padx=(20,0))
        lbl_dest_x.pack(side=tk.LEFT)
        ent_dest_x.pack(side=tk.LEFT)
        lbl_dest_y.pack(side=tk.LEFT)
        ent_dest_y.pack(side=tk.LEFT)

    def __draw_start_buttons(self, frame):
        """Creates a button for starting the A* search."""
        btn_Astar = tk.Button(master=frame, text="Start A* Search",
            bg="#2f4454", fg="white")
        btn_Astar.pack(side=tk.LEFT, padx=(20,0))

    def __draw_position_tracker(self, frame):
        """Creates the labels that track the cursor coordinates."""
        lbl_x = tk.Label(master=frame, text="x:")
        self.lbl_mouse_x = tk.Label(master=frame, width=2, text="?")
        lbl_y = tk.Label(master=frame, text="y:")
        self.lbl_mouse_y = tk.Label(master=frame, width=2, text="?")

        lbl_x.pack(side=tk.LEFT, padx=(100,0))
        self.lbl_mouse_x.pack(side=tk.LEFT)
        lbl_y.pack(side=tk.LEFT, padx=(10,0))
        self.lbl_mouse_y.pack(side=tk.LEFT)

    def __handle_click(self, event):
        """Event handler that changes the  color of the spot that is clicked."""
        self.initial_click = event.widget
        if self.initial_click["bg"] == "#d9d9d9":
            self.initial_click["bg"] = "black"
            self.initial_black = True
        elif self.initial_click["bg"] == "black":
            self.initial_click["bg"] = "#d9d9d9"
            self.initial_black = False

    def __handle_drag(self, event):
        """Event handler that changes the color of the spot that
        is dragged over."""
        widget = event.widget.winfo_containing(event.x_root, event.y_root)
        if (self.current_widget != widget and widget != self.initial_click
            and self.node_map.contains_widget(widget)):
            self.current_widget = widget
            if (self.current_widget["bg"] == "black"
                or self.current_widget["bg"] == "#d9d9d9"):
                if self.initial_black:
                    self.current_widget["bg"] = "black"
                else:
                    self.current_widget["bg"] = "#d9d9d9"

    def __track_position(self, event):
        """Event handler that updates the current grid position in
        x and y coordinates."""
        widget = event.widget
        node = self.node_map.get(widget)
        self.lbl_mouse_x["text"] = str(node.get_x())
        self.lbl_mouse_y["text"] = str(node.get_y())

def main():
    window = tk.Tk()
    all_nodes = NodeCollection()
    GUI(window, all_nodes)
    window.mainloop()

if __name__ == '__main__':
    main()
