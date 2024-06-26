# Third lab 3 level 3 option

class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(root):
    max_distance = 0

    def calculate_depth(node):
        nonlocal max_distance
        if node is None:
            return 0
        left_subtree = calculate_depth(node.left)
        right_subtree = calculate_depth(node.right)
        max_distance = max(max_distance, left_subtree + right_subtree)
        return 1 + max(left_subtree, right_subtree)
    calculate_depth(root)
    return max_distance
