class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.index = None

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word, index):
        cur = self.root

        
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
                
            cur = cur.children[i]
            
        cur.is_end = True
        cur.index = index
        
        
    def startsWith(self, word):
        cur = self.root
        
        for i in word:
            if i not in cur.children:
                return -1
            
            cur = cur.children[i]
        
        return self.traverse(cur)
        
        
    def traverse(self, node):
        ans = -1
        
        if node.is_end:
            ans = max(ans, node.index)
        
        
        for child in node.children:
            ans = max(ans, self.traverse(node.children[child]))
        
        return ans

    
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for index, word in enumerate(words):
            for idx, i in enumerate(word):
                
                self.trie.insert(word[idx:] + '{' + word, index)
        

    def f(self, pref: str, suff: str) -> int:
        
        return self.trie.startsWith(suff + '{' + pref)
            


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)