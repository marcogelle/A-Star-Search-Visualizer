from constants import NUM_ROWS

class Node:
    """Represents one square on the grid."""
    def __init__(self, frame, x_coord, y_coord):
        self.frm = frame
        self.x = x_coord
        self.y = y_coord

    def get_frm(self) -> int:
        return self.frm

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y


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
        return self.dict[f"{x},{y}"]

    def get(self, frame) -> Node:
        """Returns the node for the specified frame widget."""
        info = frame.grid_info()
        row, col = info["row"], info["column"]
        return self.get_from_pos(col, NUM_ROWS-row-1)

    def contains_widget(self, widget) -> bool:
        return widget in self.widgets
