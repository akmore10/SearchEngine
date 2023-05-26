class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.indexList = []


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word,values):
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.indexList = values
        current.isEndOfWord = True

