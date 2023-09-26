class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
            
        cur = self.root
        
        for idx, i in enumerate(word):
            
            if idx < len(word) - 1:
                if i not in cur.children:
                    return 0
                
            else:
                cur.children[i] = TrieNode()
                
            cur = cur.children[i]
            
        cur.is_end = True
        
        return len(word)


class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        max_len = 0
        words.sort()
        ans = []
        
        
        for word in words:
            length = trie.insert(word)
            
            if length > max_len:
                ans = [word]
                max_len = length
                
            elif length > 0 and length == max_len:
                ans.append(word)
                
            
        ans.sort()
        return ans[0] if ans else ''
            
            
                    
        
        
        
        