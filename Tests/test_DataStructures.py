from DataStructures.Trie import Trie

obj = Trie()
words = ["bat","cat","mat","hat","balloon","ball"]
for word in words:
    obj.insert(word,[])

def test_FindWords():
    result = obj.findWords("ba")
    assert type(result) == list