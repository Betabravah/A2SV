class TrieNode:
    def __init__(self):
        self.is_end = True
        self.children = {}
        self.val = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        
        for i in key:
            if i not in cur.children:
                cur.children[i] = TrieNode()
                
            cur = cur.children[i]
            
        cur.is_end = True
        cur.val = val
        

    def sum(self, prefix: str) -> int:
        def dfs(node, index):
            nonlocal ans
            
            if index >= len(prefix) and node.is_end:
                ans += node.val
                
            if index >= len(prefix):
                for child in node.children:
                    dfs(node.children[child], index+1)
            
            elif prefix[index] in node.children:
                dfs(node.children[prefix[index]], index + 1)
                
        ans = 0
        dfs(self.root, 0)
        return ans
        
                
                
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)