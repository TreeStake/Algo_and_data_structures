# Fourth lab 2 level 1 option

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class BinaryHeap:
    def __init__(self):
        self.priority_queue = []

    def swap_two_elements(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def add_element(self, value, priority):
        new_node = Node(value, priority)
        self.priority_queue.append((new_node.value, new_node.priority))
        if len(self.priority_queue) > 1:
            for i in range((len(self.priority_queue)-2) // 2, -1, -1):
                self.build_heapify(self.priority_queue, i, len(self.priority_queue))

    def build_heapify(self, arr, pos_node, heap_size):
        left_child, right_child = pos_node * 2 + 1, pos_node * 2 + 2
        if max(left_child, right_child) < heap_size:
            if arr[left_child][1] > arr[pos_node][1]:
                self.swap_two_elements(arr, left_child, pos_node)
                self.build_heapify(arr, left_child, heap_size)
            if arr[right_child][1] > arr[pos_node][1]:
                self.swap_two_elements(arr, right_child, pos_node)
                self.build_heapify(arr, right_child, heap_size)
        elif left_child < heap_size:
            if arr[left_child][1] > arr[pos_node][1]:
                self.swap_two_elements(arr, left_child, pos_node)
                self.build_heapify(arr, left_child, heap_size)
        elif right_child < heap_size:
            if arr[right_child][1] > arr[pos_node][1]:
                self.swap_two_elements(arr, right_child, pos_node)
                self.build_heapify(arr, right_child, heap_size)

    def pop_element(self):
        top_element = self.priority_queue[0]
        self.priority_queue[0] = self.priority_queue[-1]
        self.priority_queue.pop()
        for i in range(0, (len(self.priority_queue) - 2) // 2):
            self.build_heapify(self.priority_queue, i, len(self.priority_queue))
        # print(top_element)
        return top_element[0]

    def show_queue(self):
        # print(self.priority_queue)
        return self.priority_queue


if __name__ == "__main__":
    heap = BinaryHeap()
    heap.add_element(5, 5)
    heap.add_element(9, 16)
    heap.add_element(10, 8)
    heap.add_element(4, 14)
    heap.add_element(4, 20)
    heap.add_element(4, 1)
    heap.add_element(4, 26)
    heap.show_queue()
    heap.pop_element()
    heap.show_queue()
