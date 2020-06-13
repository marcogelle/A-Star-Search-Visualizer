from constants import NUM_ROWS, NUM_COLS

class Node:
    """Represents one square on the grid."""
    def __init__(self, frame, x_coord, y_coord, node_map):
        self.frm = frame
        self.x = x_coord
        self.y = y_coord
        self.map = node_map

    def get_frm(self) -> int:
        return self.frm

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def pos_str(self) -> str:
        """Returns a string that represents this node's position on the grid."""
        return f"{self.get_x},{self.get_y}"

    def get_succ(self):
        """Returns a list of a node's neighbors/successors. Starts with the
        top successor and goes clockwise. Does not show diagonal neighbors.
        There are 4 successors total."""
        x, y = self.get_x(), self.get_y()
        succ = []
        for [dx, dy] in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            next = self.map.get_from_pos(x + dx, y + dy)
            if next:
                succ.append(next)
        return succ

class NodeCollection:
    """A collection of all the nodes on the grid. Contains a map between
    coordinates and nodes as well as a set of widgets included."""
    def __init__(self):
        self.dict = {}
        self.widgets = set()

    def add(self, node: Node):
        """Adds a node into the collection."""
        pos = f"{node.get_x()},{node.get_y()}"
        if pos not in self.dict:
            self.dict[pos] = node
        else:
            raise TypeError("Node already exists in this map.")
        self.widgets.add(node.get_frm())

    def get_from_pos(self, x: int, y: int) -> Node:
        """Returns the node at given coordinates (bottom left is (0,0))."""
        if x >= 0 and x < NUM_COLS and y >= 0 and y < NUM_ROWS:
            return self.dict[f"{x},{y}"]    # FIXME: ABSTRACTION BARRIER
        return None

    def get(self, frame) -> Node:
        """Returns the node for the specified frame widget."""
        info = frame.grid_info()
        row, col = info["row"], info["column"]
        return self.get_from_pos(col, NUM_ROWS-row-1)

    def contains_widget(self, widget) -> bool:
        """Returns True if the given widget is in our collection."""
        return widget in self.widgets
