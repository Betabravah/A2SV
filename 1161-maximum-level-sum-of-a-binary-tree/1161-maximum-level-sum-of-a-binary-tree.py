# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([[root, 1]])
        max_sum = -float('inf')
        ans = 0
        
        while queue:
            
            length = len(queue)
            temp = 0
            
            for _ in range(length):
                node, level = queue.popleft()
                temp += node.val
                
                
                
                if node.left:
                    queue.append((node.left, level+1))
                    
                if node.right:
                    queue.append((node.right, level+1))
                    
            if temp > max_sum:
                ans = level
                max_sum = temp
                    
                    
        return ans
                    
                
               
                
                
                
                
                
            
            
            