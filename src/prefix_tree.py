class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.end_word = True

    def search(self, word):
        current = self.root

        for i in word:
            if i not in current.children:
                return False
            current = current.children[i]
        return True

    def search_prefix(self, prefix):
        current = self.root

        for i in prefix:
            if i not in current.children:
                return False
            current = current.children[i]

        if current.end_word is False:
            return True
        else:
            return "It is word not prefix"
        