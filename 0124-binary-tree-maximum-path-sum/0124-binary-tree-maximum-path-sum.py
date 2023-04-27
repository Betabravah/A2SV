# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        
        def dfs(node):
            nonlocal max_sum
            
            if not node:
                return -float('inf')
            
            
            cur = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            
            
            cur_left = cur + left
            cur_right = cur + right
            left_cur_right = left + cur + right
            
            
            max_sum = max(max_sum, cur, cur_left, left_cur_right, cur_right)
            
            return max(cur_left, cur, cur_right)
            
            
        dfs(root)
        return max_sum
            
            
            
            
            
            
            