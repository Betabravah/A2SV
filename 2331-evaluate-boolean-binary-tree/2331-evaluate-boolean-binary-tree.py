# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def evaluate(node):
            
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            
            elif node.val == 2:
                return evaluate(node.left) or evaluate(node.right)
            
            else:
                return evaluate(node.left) and evaluate(node.right)
            
        return evaluate(root)