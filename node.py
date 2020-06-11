class Node:
    """Represents one square on the grid."""
    def __init__(self, frame, x_coord, y_coord):
        self.frm = frame
        self.x = x_coord
        self.y = y_coord

    @staticmethod
    def getNode(x: int, y: int): -> Node
        """Returns the node at the specified location"""
        
