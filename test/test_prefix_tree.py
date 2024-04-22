import unittest
from Algo_and_data_structures.src.prefix_tree import Trie


class TestPrefixTree(unittest.TestCase):
    def test_insert(self):
        tree = Trie()
        tree.insert("apple")
        self.assertEqual(tree.search("apple"), True)

    def test_search(self):
        tree = Trie()
        tree.insert("apple")
        tree.insert("banana")
        tree.insert("lemon")
        self.assertEqual(tree.search("banana"), True)

    def test_search_prefix(self):
        tree = Trie()
        tree.insert("apple")
        tree.insert("banana")
        tree.insert("lemon")
        self.assertEqual(tree.search_prefix("lem"), True)


if __name__ == '__main__':
    unittest.main()
