# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # ans
        def dfs(root):
            if not root:
                return '', 0
            
            left, left_leaf = dfs(root.left)
            right, right_leaf = dfs(root.right)
            
            # print(root.val, left_leaf, right_leaf)
            
            res = f'{root.val}'
            
            if right_leaf:
                res += f'({left})({right})'
                
            elif left_leaf:
                res += f'({left})'
                

            
            return res, 1
        
        ans = dfs(root)
        return ans[0]