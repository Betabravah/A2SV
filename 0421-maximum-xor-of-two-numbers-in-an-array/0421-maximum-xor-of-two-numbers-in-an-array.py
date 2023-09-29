class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
    
    
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, num, binary):
            
        cur = self.root

        for i in binary:
            if i == '0':
                if cur.left == None:
                    cur.left = TrieNode()
                    
                cur = cur.left
                
            else:
                if cur.right == None:
                    cur.right = TrieNode()
                    
                cur = cur.right

        cur.val = num


    def search(self, num, binary):
        cur = self.root

        for i in binary:
            
            if i == '0':
                if cur.right:
                    cur = cur.right
                else:
                    cur = cur.left
                    
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur = cur.right

        return cur.val ^ num

    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        
        
        for num in nums:
            trie.insert(num, bin(num)[2:].zfill(32))
    
        ans = 0
        for num in nums:
            ans = max(ans, trie.search(num, bin(num)[2:].zfill(32)))

        return ans
        