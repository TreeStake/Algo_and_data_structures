import unittest
from Algo_and_data_structures.src.heap_based_priority_queue import BinaryHeap


class TestHeapBasedPriority(unittest.TestCase):

    def test_add_element(self):
        heap = BinaryHeap()
        heap.add_element(5, 5)
        self.assertEquals(heap.show_queue(), [(5, 5)])

    def test_pop_element(self):
        heap = BinaryHeap()
        heap.add_element(5, 5)
        heap.add_element(9, 16)
        heap.add_element(10, 8)
        heap.add_element(4, 14)
        heap.add_element(4, 20)
        heap.add_element(4, 1)
        heap.add_element(4, 26)
        self.assertEquals(heap.pop_element(), 4)

    def test_add_element_if_build_heap(self):
        heap = BinaryHeap()
        heap.add_element(5, 1)
        heap.add_element(15, 2)
        heap.add_element(7, 5)
        self.assertEquals(heap.show_queue(), [(7, 5), (5, 1), (15, 2)])


if __name__ == "__main__":
    unittest.main()
