# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if not left:
                node.left = None
                
            if not right:
                node.right = None
                
            
            if left or right or node.val == 1:
                return True
            
        dummy = TreeNode()
        dummy.left = root
        dfs(dummy)
        return dummy.left if dummy.left else None
            
                