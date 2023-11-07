# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left = left_len + 1
            else:
                left = 0
                    
            if node.right and node.right.val == node.val:
                right = right_len + 1
            else:
                right = 0
                
            ans = max(ans, left + right)
            
            return max(left, right)
                  
        ans = 0
        dfs(root)
        return ans