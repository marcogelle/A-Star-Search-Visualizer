import unittest
import tkinter as tk

from node import *
from search import *

class TestNode(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.map = NodeCollection()
        for i in range(20):
            for j in range(20):
                frm = tk.Frame()
                node = Node(frm, i, j, self.map)
                self.map.add(node)
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_search_simple(self):
        a_star = AStar('Manhattan')
        start = self.map.get_from_pos(1, 1)
        dest = self.map.get_from_pos(5, 4)
        path = a_star.search(start, dest)
        print([node.pos_str() for node in path])

if __name__ == '__main__':
    unittest.main()
