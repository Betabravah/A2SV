class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.words_passed = 0
    
    
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
            
        cur = self.root

        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
             
            cur = cur.children[i]
            cur.words_passed += 1


        cur.is_end = True
        
    
    def search(self, word):
        
        cur = self.root
        ans = cur.words_passed

        for index, i in enumerate(word):
            cur = cur.children[i]

            ans += cur.words_passed
            
        return ans

    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        ans = []
        for word in words:
            ans.append(trie.search(word))
            
        return ans
            
        