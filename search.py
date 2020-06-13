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
        open.put((0, start))
        closed = ()
        g = {start.pos_str(): 0}
        parents = {start.pos_str(): None}
        while open:
            curr = open.get()
            closed.add(curr)
            for next in curr.get_succ():
                cost = g[curr.pos_str()] + 1
                if next in closed:
                    continue
                if next not in [x[1] for x in open.queue]:
                    parents[next.pos_str()] = curr
                    g[next.pos_str()] = cost
                    f_next = cost + self.heur(next, dest)
                    open.put((f_next, next))
                elif cost < g[start.pos_str()]:
                    #TODO: remove from list

    def heur(self, node: Node, dest: Node) -> int:
        pass
