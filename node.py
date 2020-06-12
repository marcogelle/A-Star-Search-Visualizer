class NodeMap:
    """A map of all the nodes on the grid."""
    def __init__(self):
        self.dict = {}

    def add(self, node: Node):
        """Adds a node into the map."""
        pos = f"{node.get_x},{node.get_y}"
        if pos not in self.dict:
            self.dict[pos] = node
        else:
            raise TypeError('Node already exists in this map.')

    def get(self, x: int, y: int) -> Node:
        """Returns the node at the specified location."""
        return self.dict[f"{x},{y}"]

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
