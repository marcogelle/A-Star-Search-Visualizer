from queue import PriorityQueue

from node import *

class AbstractSearch:
    def search(self, start: Node, dest: Node):
        """Finds and draws the shortest path from the starting
        node to the destination node."""
        pass

class AStar(AbstractSearch):
    def __init__(self, heuristic: str):
        self.h = heuristic

    def search(self, start: Node, dest: Node):
        open = PriorityQueue()
        g = {start.pos_str(): 0}
        open.put((0, start))
        closed = ()
        while open:
            curr = open.get()
            closed.add(curr)
            for s in curr.get_succ():
                cost =
