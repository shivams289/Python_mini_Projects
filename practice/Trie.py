class TrieNode:
    def __init__(self) -> None:

        self.children = {}
        self.endofword = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.endofword = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endofword

    def startswith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return True
