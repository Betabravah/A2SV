# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def equal(root1, root2):
            
            if not root1 or not root2:
                return root1 == root2
            else:
                return root1.val == root2.val and equal(root1.left, root2.right) and equal(root1.right, root2.left)
            
        return equal(root, root)