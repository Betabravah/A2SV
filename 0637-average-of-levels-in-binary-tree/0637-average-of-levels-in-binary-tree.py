# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        
        queue = deque([root])
        
        while queue:
            length = len(queue)
            level = []
            
            for i in range(length):
                node = queue.popleft()
                
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if level:
                ans.append(sum(level) / len(level))
                
                
        return ans
        
        return bfs(root)
                