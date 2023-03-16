# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def average(root):
            if not root:
                return 0, 0
            
            left_count, left_half = average(root.left)
            right_count, right_half = average(root.right)
            
            
            summ = left_half + root.val + right_half
            total = left_count + 1 + right_count
            
            if root.val == summ//total:
                self.count += 1
        
                
            return total, summ
        
        average(root)
        return self.count
            
            
                