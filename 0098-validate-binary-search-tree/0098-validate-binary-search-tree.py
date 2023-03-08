# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def compare(root):
            if root == None:
                return []
            else:
                return compare(root.left) + [root.val] + compare(root.right)
            
        arr = compare(root)
        print(arr)
        if (all(arr[i] < arr[i+1] for i in range(len(arr)-1))):
            return True
        return False
            