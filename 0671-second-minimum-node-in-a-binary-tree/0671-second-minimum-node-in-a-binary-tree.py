# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal minn
            nonlocal second_minn
            
            if not node:
                return 
            
            if node.val < minn:
                second_minn = minn
                minn = node.val
                
            elif node.val != minn and node.val < second_minn:
                second_minn = node.val
                
            dfs(node.left)
            dfs(node.right)
            
        minn = second_minn = float('inf')
        dfs(root)
        return second_minn if second_minn < float('inf') else -1