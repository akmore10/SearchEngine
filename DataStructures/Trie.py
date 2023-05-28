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
    
    def _iterator(self,word):
        temp = self.root
        for w in word:
            if w in temp.children:
                temp = temp.children[w]
            else:
                return None
        return temp

    def findWords(self,inComplete:str):
        result = []
        ptr = self._iterator(inComplete)

        if ptr != None:  
            for k,v in ptr.children.items():
                result.append(self._dfs(v,inComplete+k,result))
        return result
    
    def _dfs(self,root:TrieNode,res:str,result):
        if root.isEndOfWord:
            result.append(res)
        for k,v in root.children.items():
            self._dfs(v,res + k,result)