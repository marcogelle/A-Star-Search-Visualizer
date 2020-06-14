from node import *
from constants import SEARCH_COLOR

class AbstractSearch:
    def __init__(self, walls):
        self.walls = walls

    def search(self, start: Node, dest: Node):
        """Finds and draws the shortest path from the starting
        node to the destination node. Returns a path."""
        pass

class AStar(AbstractSearch):
    def search(self, start: Node, dest: Node):
        """Performs A* search from start to destination. Returns a path."""
        self.searched = []

        open = [start]
        closed = set()
        g = {start.pos_str(): 0}
        f = {start.pos_str(): 0 + self.heur(start, dest)}
        parents = {start.pos_str(): None}

        while open:
            # Get node with min f from open list
            curr = open[0]
            curr_ind = 0
            for i, node in enumerate(open):
                if f[node.pos_str()] < f[curr.pos_str()]:
                    curr = node
                    curr_ind = i
            open.pop(curr_ind)
            closed.add(curr)

            # Destination is reached
            if curr is dest:
                path = []
                while curr is not None:
                    path.append(curr)
                    curr = parents[curr.pos_str()]
                # reverse path, exclude start and destination nodes
                return path[len(path)-2:0:-1]

            # Plan to color curr in GUI
            if curr is not start:
                self.searched.append(curr.get_frm())

            # Check each of the current node's successors
            for next in curr.get_succ():
                cost = g[curr.pos_str()] + 1
                if next in closed or next in self.walls:
                    continue
                if next not in open:
                    parents[next.pos_str()] = curr
                    g[next.pos_str()] = cost
                    f[next.pos_str()] = cost + self.heur(next, dest)
                    open.append(next)
                elif cost < g[start.pos_str()]:
                    parents[next.pos_str()] = curr
                    g[next.post_str()] = cost
                    f[next.post_str()] = cost + self.heur(next, dest)

        return []

    def get_searched(self):
        """Returns a list of nodes in the order they were inspected in
        the last call of self.search()."""
        return self.searched

    def heur(self, node: Node, dest: Node, method='Manhattan') -> int:
        """Heuristic used in the A* search."""
        def manhattan():
            return (abs(node.get_x() - dest.get_x())
                + abs(node.get_y() - dest.get_y()))

        if method == 'Manhattan':
            return manhattan()
        raise TypeError('Invalid heuristic.')
        #TODO include other heuristics
