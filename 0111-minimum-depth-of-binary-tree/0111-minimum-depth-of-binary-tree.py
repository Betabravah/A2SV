# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            if not node.left and not node.right:
                return 1
            
            left = dfs(node.left) if node.left else float('inf')
            right = dfs(node.right) if node.right else float('inf')
            
            return 1 + min(left, right)
        
        return dfs(root)