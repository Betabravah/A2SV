# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        maxWidth = 0
        
        while queue:
            if queue[0][1] != queue[-1][1]:
                maxWidth = max(maxWidth, queue[-1][1] - queue[0][1] + 1)
                
                
            for i in range(len(queue)):
                cur, idx = queue.popleft()
                
                if cur.left:
                    queue.append((cur.left, idx * 2 - 1))
                    
                if cur.right:
                    queue.append((cur.right, idx * 2))
                    
                    
        return max(1, maxWidth)