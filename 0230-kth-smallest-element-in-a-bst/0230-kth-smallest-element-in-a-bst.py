# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def getarr(root):
            if not root:
                return []
            else:
                return getarr(root.left) + [root.val] + getarr(root.right)
            
        arr = getarr(root)
        
        return arr[k-1]