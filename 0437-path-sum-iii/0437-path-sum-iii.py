# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        
        def traverse(root, pathsum):
            nonlocal count

            if not root:
                return
            
            pathsum += root.val
            
            count += prefix[pathsum - targetSum]
            prefix[pathsum] += 1
            
            traverse(root.left, pathsum)
            traverse(root.right, pathsum)
            
            prefix[pathsum] -= 1
            
            
            
            
        traverse(root, 0)
        
            
        return count