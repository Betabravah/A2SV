# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, is_left):
            nonlocal ans
            
            if not node:
                return False
            
            
            left = dfs(node.left, True)
            right = dfs(node.right, False)
            
            if not left and not right and is_left:
                ans += node.val
                
            return True
        
                
        ans = 0
        dfs(root, False)
        return ans
                