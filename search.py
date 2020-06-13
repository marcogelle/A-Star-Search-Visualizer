from node import *

class AbstractSearch:
    def search(self, start: Node, dest: Node):
        """Finds and draws the shortest path from the starting
        node to the destination node."""
        pass

class AStar(AbstractSearch):
    def __init__(self, heuristic: string):
        self.h = heuristic

    def search(self, start, dest):
        
