class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        cur = self.root

        
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
                
            cur = cur.children[i]
            
        cur.is_end = True
        
        
    def startsWith(self, word):
        cur = self.root
        
        for i in word:
            if i not in cur.children:
                return []
            
            cur = cur.children[i]
            
            
        def traverse(node, prefix):
            nonlocal words
            
            if node.is_end:
                words.append(prefix)
                
            for child in node.children:
                traverse(node.children[child], prefix + child)
                
                
        words = []
        traverse(cur, word)
        return words
            
                
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        
        for word in products:
            trie.insert(word)
            
        res = []
        for i in range(len(searchWord)):
            ans = trie.startsWith(searchWord[:i+1])
            
            ans.sort()
            res.append(ans[:min(3, len(ans))])
            
        return res
            
            
        