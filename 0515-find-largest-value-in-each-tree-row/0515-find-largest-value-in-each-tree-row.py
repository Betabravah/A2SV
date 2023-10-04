# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root]) if root else []
        ans = []
        
        while queue:
            length = len(queue)
            temp = -float('inf')
            
            for _ in range(length):
                node = queue.popleft()
                
                temp = max(temp, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            ans.append(temp)
            
        return ans
                
                
                
            
        