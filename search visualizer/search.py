import node
from constants import NUM_ROWS, NUM_COLS


class AbstractSearch:
    def __init__(self, walls):
        """Tracks the walls as a set of Nodes."""
        self.walls = walls

    def search(self, start, dest):
        """Finds and draws the shortest path from start (type Node) to the
        destination, dest (type Node). Returns a path. Should update
        self.searched for use in the GUI."""
        pass

    def get_searched(self):
        """Returns a list of nodes in the order they were inspected in
        the last call of self.search()."""
        pass

class AStar(AbstractSearch):
    def __init__(self, walls, heuristic):
        """The heuristic should be a function that takes in two nodes and
        outputs a number."""
        AbstractSearch.__init__(self, walls)
        self.heuristic = heuristic

    def search(self, start, dest):
        """Performs A* search from start to destination (both Node objects).
        Returns a path, which is a list of Nodes. Updates self.searched."""
        self.searched = []

        closed = set()
        best_parents = {start: None}
        g = {start: 0}

        # Key: node. Value: (f value, parent node)
        fringe = {start: (0 + self.heuristic(start, dest), None)}

        while fringe:
            # Get node with min f from fringe
            get_f = lambda fringe_item: fringe_item[1][0]
            curr, temp = min(fringe.items(), key=get_f)
            curr_parent = temp[1]
            del fringe[curr]

            # Destination is reached
            if curr is dest:
                path = []
                while curr is not None:
                    path.append(curr)
                    curr = best_parents[curr]
                # reverse path, exclude start and destination nodes
                return path[len(path)-2:0:-1]

            # Avoid checking nodes repeatedly
            if curr not in closed:
                closed.add(curr)
                best_parents[curr] = curr_parent

                # Plan to color curr in GUI
                if curr is not start:
                    self.searched.append(curr.get_frm())

                # Check each of the current node's successors
                for succ in curr.get_succ():
                    if succ not in self.walls:
                        if succ not in closed:
                            best_parents[succ] = curr
                        g[succ] = g[curr] + 1
                        f_val = g[succ] + self.heuristic(succ, dest)
                        fringe[succ] = (f_val, curr)

        return []

    def get_searched(self):
        """Returns a list of tkinter Frames in the order they were inspected in
        the last call of self.search()."""
        return self.searched


def trivial(node, dest):
    return 0

def manhattan(node, dest):
    return (abs(node.get_x() - dest.get_x()) + abs(node.get_y() - dest.get_y()))

def euclidean(node, dest):
    return ((node.get_x() - dest.get_x())**2 + (node.get_y() - dest.get_y())**2) ** 0.5

def inadmissible(node, dest):
    return 2 * manhattan(node, dest)

def manhattan_tie_break(node, dest):
    p = 1 / (NUM_ROWS * NUM_COLS)
    return manhattan(node, dest) * (1.0 + p)
