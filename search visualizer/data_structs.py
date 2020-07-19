import heapq

class PriorityQueue:
    """
    Credit: taken from util.py of Project 3 for CS 188 Summer 2020 at UC Berkeley.
    https://inst.eecs.berkeley.edu/~cs188/su20/project3/

    Implements a priority queue data structure. Each inserted item
    has a priority associated with it and the client is usually interested
    in quick retrieval of the lowest-priority item in the queue. This
    data structure allows O(1) access to the lowest-priority item.
    """

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        _, _, item = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0
