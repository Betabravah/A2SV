# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def dfs(root, path):

            nonlocal total
            
            if not root:
                return
            
            if not root.left and not root.right:
                path.append(root.val)
                
                num = ''
                for i in path:
                    num += str(i)
                    
                total += int(num)
                return
                
            
            dfs(root.left, path + [root.val])
            dfs(root.right, path + [root.val])
            
            
        dfs(root, [])
        return total 