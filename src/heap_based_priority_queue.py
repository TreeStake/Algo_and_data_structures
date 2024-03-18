class Node:
    def __init__(self, value, priority, left=None, right=None):
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right


class BinaryHeap:
    def __init__(self):
        self.root = None

    def add_element(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
        else:
            self.add_recursively(value, priority, self.root)

    def add_recursively(self, value, priority, node):
        if node.priority <= priority:
            if node.right is None:
                node.right = Node(value, priority)
            else:
                self.add_recursively(value, priority, node.right)
        else:
            if node.left is None:
                node.left = Node(value, priority)
            else:
                self.add_recursively(value, priority, node.left)

    def find_the_biggest(self):
        cur_node = self.root
        if cur_node.right is not None:
            while cur_node.right.right is not None:
                cur_node = cur_node.right
            return cur_node, cur_node.right
        else:
            return cur_node, None

    def delete(self):
        node_to_delete = self.find_the_biggest()
        if node_to_delete[1] is not None:
            node_to_delete[0].right = node_to_delete[1].left
            return node_to_delete[1].value, node_to_delete[1].priority
        else:
            self.root = node_to_delete[0].left
            return node_to_delete[0].value, node_to_delete[0].priority

    def show_heap(self, node):
        show_que = []

        def create_que(node):
            nonlocal show_que
            if node is None:
                return
            show_que.append((node.value, node.priority))
            create_que(node.left)
            create_que(node.right)
        create_que(node)
        show_que.sort(key=lambda x: x[1], reverse=True)
        print(show_que)
        return show_que


if __name__ == "__main__":
    heap = BinaryHeap()
    heap.add_element(5, 5)
    heap.add_element(15, 4)
    heap.add_element(7, 3)
    heap.add_element(2, 6)
    heap.add_element(9, 10)
    heap.add_element(8, 9)

    heap.show_heap(heap.root)
    print(heap.delete())
    heap.show_heap(heap.root)
