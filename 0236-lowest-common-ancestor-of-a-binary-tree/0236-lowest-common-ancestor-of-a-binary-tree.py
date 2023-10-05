# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            nonlocal ans
            
            if not node:                
                return False, set()
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            gotP = left[0] or right[0]
            gotQ = left[1] or right[1]
            
            if node.val == p.val:
                gotP = True
                
            elif node.val == q.val:
                gotQ = True
                
            if gotP and gotQ:
                if not ans:
                    ans = node
                    
            return gotP, gotQ
        
        ans = None
        dfs(root)
        return ans
                