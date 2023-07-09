# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)
        
        def dp(node):
            if not node:
                return (0, 0)
            
            
            left = dp(node.left)
            right = dp(node.right)
            
            
            memo[node] = (node.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))

            return memo[node]

        
        return max(dp(root))