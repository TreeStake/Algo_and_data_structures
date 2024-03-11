import unittest
from max_diametr import BinaryTree, binary_tree_diameter


class TestMinimalPosition(unittest.TestCase):

    def test_data_lecture(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        self.assertEquals(binary_tree_diameter(root), 6)

    def test_data_student(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(4)
        root.left.left = BinaryTree(6)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.left.right = BinaryTree(2)
        root.left.left.right.right = BinaryTree(7)
        root.left.left.right.right.right = BinaryTree(1)
        root.left.left.right.right.right.left = BinaryTree(4)
        self.assertEquals(binary_tree_diameter(root), 7)


if __name__ == "__main__":
    unittest.main()