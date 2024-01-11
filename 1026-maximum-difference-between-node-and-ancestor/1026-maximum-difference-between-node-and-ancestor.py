# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, minn, maxx):
            nonlocal ans
            
            if not node:
                return
            
            ans = max(ans, abs(node.val - minn), abs(node.val - maxx))
            
            minn = min(minn, node.val)
            maxx = max(maxx, node.val)
            
            dfs(node.left, minn, maxx)
            dfs(node.right, minn, maxx)
            
            
        
        ans = 0
        dfs(root, root.val, root.val)
        return ans