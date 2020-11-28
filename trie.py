class TrieNode:
    def __init__(self):
        self.char_map = {}
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.char_map:
                curr.char_map[char] = TrieNode()
            curr = curr.char_map[char]
        curr.is_leaf = True

    def contains(self, word):
        curr = self.root
        for char in word:
            if char in curr.char_map:
                curr = curr.char_map[char]
            else:
                return False
        return curr.is_leaf

    def start_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char in curr.char_map:
                curr = curr.char_map[char]
            else:
                return False
        return True
