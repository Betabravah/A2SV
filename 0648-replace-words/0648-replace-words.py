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
    
    
    def get_root(self, word):
        cur = self.root
        depth = 0
        
        for i in word:
            if i not in cur.children or cur.is_end:
                break
            
            cur = cur.children[i]
            depth += 1
        
        return word[:depth] if cur.is_end else word
    
    
    
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
            
            
        ans = []
        words = sentence.split()
        for word in words:
            root = trie.get_root(word)
            
            ans.append(root)
                
        return ' '.join(ans)
