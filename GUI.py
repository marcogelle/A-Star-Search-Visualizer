import tkinter as tk

from node import *
from search import *
from constants import *

class GUI:
    """When a GUI instance is created, the GUI for this project is set up
    on the given tkinter window. A GUI also as a node_map containing node
    objects for every spot on the grid."""

    def __init__(self, root, node_map):
        self.root = root
        self.node_map = node_map
        self.start_node = None
        self.dest_node = None
        self.walls = set()

        # Flags for holding info during the event loop. Used by event handlers.
        self.current_widget = None
        self.initial_click = None
        self.initial_black = False

        self.draw_top_bar()
        self.draw_grid()

    def draw_top_bar(self):
        """Sets up all widgets for the top bar of the UI."""
        frm_input = tk.Frame(master=self.root)
        self.draw_start_input(frm_input)
        self.draw_destination_input(frm_input)
        self.draw_start_button(frm_input)
        self.draw_clear_button(frm_input)
        self.draw_position_tracker(frm_input)
        frm_input.pack()

    def draw_grid(self):
        """Creates the grid."""
        frm_grid = tk.Frame(master=self.root)
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                frm = tk.Frame(
                    master=frm_grid,
                    relief=tk.RIDGE,
                    borderwidth=1,
                    bg=GRID_COLOR,
                    width=SPOT_SIZE,
                    height=SPOT_SIZE
                )
                frm.grid(row=r, column=c)
                frm.bind("<Button-1>", self.handle_click)
                frm.bind("<B1-Motion>", self.handle_drag)
                frm.bind("<Enter>", lambda event: self.track_position(event))
                self.node_map.add(Node(frm, c, NUM_ROWS-r-1, self.node_map))
        frm_grid.pack()

    def draw_start_input(self, frame):
        """Sets up widgets for inputting the starting position."""
        def draw_start():
            x, y = int(ent_start_x.get()), int(ent_start_y.get())
            node = self.node_map.get_from_pos(x, y)
            node.get_frm()["bg"] = "red"
            if self.start_node:
                self.start_node.get_frm()["bg"] = GRID_COLOR
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

    def draw_destination_input(self, frame):
        """Sets up widgets for inputting the destination position."""
        def draw_dest():
            x, y = int(ent_dest_x.get()), int(ent_dest_y.get())
            node = self.node_map.get_from_pos(x, y)
            node.get_frm()["bg"] = "green"
            if self.dest_node:
                self.dest_node.get_frm()["bg"] = GRID_COLOR
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

    def draw_start_button(self, frame):
        """Creates a button for starting the A* search."""
        def start_search():
            a_star = AStar(self.walls, self.root) #HERE
            path = a_star.search(self.start_node, self.dest_node)
            for node in path:
                node.get_frm()["bg"] = PATH_COLOR

        btn_Astar = tk.Button(master=frame, text="Start A* Search",
            bg="#2f4454", fg="white", command=start_search)
        btn_Astar.pack(side=tk.LEFT, padx=(20,0))

    def draw_clear_button(self, frame):
        """Creates the button for clearing the grid."""
        def clear():
            for w in self.node_map.widg_set():
                w["bg"] = GRID_COLOR
            self.start_node = None
            self.dest_node = None
            self.walls = set()

        btn_clear = tk.Button(master=frame, text="Clear",
            bg="#2f4454", fg="white", command=clear)
        btn_clear.pack(side=tk.LEFT, padx=(10,0))

    def draw_position_tracker(self, frame):
        """Creates the labels that track the cursor coordinates."""
        lbl_x = tk.Label(master=frame, text="x:")
        self.lbl_mouse_x = tk.Label(master=frame, width=2, text="?")
        lbl_y = tk.Label(master=frame, text="y:")
        self.lbl_mouse_y = tk.Label(master=frame, width=2, text="?")

        lbl_x.pack(side=tk.LEFT, padx=(100,0))
        self.lbl_mouse_x.pack(side=tk.LEFT)
        lbl_y.pack(side=tk.LEFT, padx=(10,0))
        self.lbl_mouse_y.pack(side=tk.LEFT)

    def handle_click(self, event):
        """Event handler that changes the color of the spot that is clicked."""
        self.initial_click = event.widget
        if self.initial_click["bg"] == GRID_COLOR:
            self.initial_click["bg"] = WALL_COLOR
            self.initial_black = True
            node = self.node_map.get(self.initial_click)
            self.walls.add(node)
        elif self.initial_click["bg"] == WALL_COLOR:
            self.initial_click["bg"] = GRID_COLOR
            self.initial_black = False
            node = self.node_map.get(self.initial_click)
            self.walls.remove(node)

    def handle_drag(self, event):
        """Event handler that changes the color of the spot that
        is dragged over."""
        widget = event.widget.winfo_containing(event.x_root, event.y_root)
        if (self.current_widget != widget and widget != self.initial_click
            and self.node_map.contains_widget(widget)):
            self.current_widget = widget
            if (self.current_widget["bg"] == WALL_COLOR
                or self.current_widget["bg"] == GRID_COLOR):
                if self.initial_black:
                    self.current_widget["bg"] = WALL_COLOR
                    node = self.node_map.get(self.current_widget)
                    self.walls.add(node)
                else:
                    self.current_widget["bg"] = GRID_COLOR
                    node = self.node_map.get(self.current_widget)
                    if node in self.walls:
                        self.walls.remove(node)

    def track_position(self, event):
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
