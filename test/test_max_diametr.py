import os
import sys
import unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from src.max_diametr import BinaryTree, binary_tree_diameter


class TestMaxDiameter(unittest.TestCase):

    def test_binary_tree_diameter_data_lecture(self):
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

    def test_binary_tree_diameter_data_student(self):
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

    def test_binary_tree_diameter_the_hardest_data(self):
        root = BinaryTree(100)
        root.left = BinaryTree(50)
        root.right = BinaryTree(120)
        root.left.left = BinaryTree(10)
        root.right.right = BinaryTree(125)
        root.right.left = BinaryTree(105)
        root.left.right = BinaryTree(71)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(12)
        root.left.left.left.left = BinaryTree(6)
        root.left.left.left.left.left = BinaryTree(5)
        root.left.left.right.right = BinaryTree(15)
        root.left.left.right.right.right = BinaryTree(18)
        root.left.left.right.right.right.left = BinaryTree(19)
        root.left.left.right.right.right.left.left = BinaryTree(20)
        self.assertEquals(binary_tree_diameter(root), 9)


if __name__ == "__main__":
    unittest.main()
