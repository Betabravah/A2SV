# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return 0, 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            ans += abs(left[0] - left[1]) + abs(right[0] - right[1])
            
            coins = left[0] + right[0] + node.val
            nodes = left[1] + right[1] + 1
                        
            return coins,  nodes
        
        ans = 0
        dfs(root)
        return ans
            
        
            