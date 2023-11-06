# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = []
        
        queue = deque([root])
        
        while queue:
            cur = queue.popleft()
            
            nums.append(cur.val)
            
            if cur.left:
                queue.append(cur.left)
            
            if cur.right:
                queue.append(cur.right)
                
        nums.sort()
        ans = float('inf')
        
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i-1])
            
        return ans
            
        