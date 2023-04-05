# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return none
        
        root = TreeNode(preorder[0])
        def binary(root, val):
            if root.val < val:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                    
                binary(root.right, val)
                
            else:
                if not root.left:
                    root.left = TreeNode(val)
                    return
                
                binary(root.left, val)
                
                
        for i in range(1, len(preorder)):
            binary(root, preorder[i])
            
        return root