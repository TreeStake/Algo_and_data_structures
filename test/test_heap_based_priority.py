import os
import sys
import unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from src.heap_based_priority_queue import BinaryHeap


class TestHeapBasedPriority(unittest.TestCase):

    def test_add_element(self):
        heap = BinaryHeap()
        heap.add_element(5, 5)
        self.assertEquals(heap.show_heap(heap.root), [(5, 5)])

    def test_delete_from_root(self):
        heap = BinaryHeap()
        heap.add_element(5, 5)
        heap.add_element(3, 3)
        heap.add_element(1, 1)
        self.assertEquals(heap.delete(), (5, 5))

    def test_delete_from_right(self):
        heap = BinaryHeap()
        heap.add_element(5, 5)
        heap.add_element(15, 4)
        heap.add_element(7, 3)
        heap.add_element(2, 6)
        heap.add_element(9, 10)
        heap.add_element(1, 12)
        heap.add_element(8, 9)
        self.assertEquals(heap.delete(), (1, 12))


if __name__ == "__main__":
    unittest.main()
