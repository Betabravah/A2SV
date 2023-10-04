# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, par):
            if not node:
                return True
            
            if par != None and node.val != par:
                return False
            
            return dfs(node.left, node.val) and dfs(node.right, node.val)
        
        return dfs(root, None)