class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
             
        cur = self.root
        
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
                
            cur = cur.children[i]
            
        cur.is_end = True
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        
        for word in strs:
            trie.insert(word)
            
        return self.traverse(trie.root, '')
            
    def traverse(self, node, prefix):
        
        if len(node.children) != 1:
            return prefix
        
        if node.is_end:
            return prefix
        
        for child in node.children:

            return self.traverse(node.children[child], prefix+child)
            
            
        
        