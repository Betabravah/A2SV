# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        even_level = True
        
        
        while queue:
            prev = -inf if even_level else inf
            
            length = len(queue)            
            for _ in range(length):
                cur = queue.popleft()
                
                if even_level:
                    if cur.val % 2 == 0 or cur.val <= prev:
                        return False
                else:
                    if cur.val % 2 or cur.val >= prev:
                        return False
                
                if cur.left:
                    queue.append(cur.left)
                    
                if cur.right:
                    queue.append(cur.right)
                    
                prev = cur.val
                
            even_level = not even_level
            
        return True
                    
                
        