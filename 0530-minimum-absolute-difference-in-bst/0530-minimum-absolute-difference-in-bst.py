# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return float('inf'), -float('inf')
            
            min_left, max_left = dfs(node.left)
            min_right, max_right = dfs(node.right)
            
            ans = min(ans, node.val - max_left, min_right - node.val)
            
            cur_min = min(min_left, min_right, node.val)
            cur_max = max(max_left, max_right, node.val)
            
            
            return cur_min, cur_max
        
        ans = float('inf')
        dfs(root)
        return ans