from constants import *

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


class NodeMap:
    """A map of all the nodes on the grid."""
    def __init__(self):
        self.dict = {}

    def add(self, node: Node):
        """Adds a node into the map."""
        pos = f"{node.get_x()},{node.get_y()}"
        if pos not in self.dict:
            self.dict[pos] = node
        else:
            raise TypeError('Node already exists in this map.')

    def __get_from_pos(self, x: int, y: int) -> Node:
        return self.dict[f"{x},{y}"]

    def get(self, frame) -> Node:
        """Returns the node for the specified frame widget."""
        info = frame.grid_info()
        row, col = info["row"], info["column"]
        return self.__get_from_pos(col+1, NUM_ROWS-row)
