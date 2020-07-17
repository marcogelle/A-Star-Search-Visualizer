import os, sys
import unittest
import tkinter as tk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('node.py'))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('search.py'))))
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

    def test_trivial(self):
        walls = set()
        start = self.map.get_from_pos(1, 1)
        dest = self.map.get_from_pos(5, 4)
        a_star = AStar(walls)
        path = a_star.search(start, dest)
        self.print_test('test_trivial', start, dest, walls, path)

    def test_wall_simple(self):
        walls = set()
        for x, y in [[3, 1], [3, 2], [3, 3], [3, 4]]:
            walls.add(self.map.get_from_pos(x, y))
        start = self.map.get_from_pos(1, 1)
        dest = self.map.get_from_pos(5, 4)
        a_star = AStar(walls)
        path = a_star.search(start, dest)
        self.print_test('test_wall_simple', start, dest, walls, path)

    def test_no_path(self):
        walls= set()
        for x, y in [[0, 2], [1, 2], [2, 2], [3, 2], [3, 1], [3, 0]]:
            walls.add(self.map.get_from_pos(x, y))
        start = self.map.get_from_pos(1, 1)
        dest = self.map.get_from_pos(5, 4)
        a_star = AStar(walls)
        path = a_star.search(start, dest)
        self.print_test('test_no_path', start, dest, walls)
        self.assertEqual(len(path), 0)

    def print_test(self, name, start, dest, walls, path=None):
        print(name)
        print(f"Start: {start.pos_str()}, Destination: {dest.pos_str()}")
        if walls:
            print(f"Walls: { {w.pos_str() for w in walls} }")
        else:
            print('Walls: None')
        if path is not None:
            print([node.pos_str() for node in path])
        print()

if __name__ == '__main__':
    unittest.main()
