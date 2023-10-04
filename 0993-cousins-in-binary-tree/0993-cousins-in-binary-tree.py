# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth = {}
        
        queue = deque([[root, 0, None]])
        while queue:
            length = len(queue)
            
            for _ in range(length):
                node, d, par = queue.popleft()
                depth[node.val] = [d, par]
                
                if node.left:
                    queue.append([node.left, d+1, node.val])
                
                if node.right:
                    queue.append([node.right, d+1, node.val])
                    
        return depth[x][0] == depth[y][0] and depth[x][1] != depth[y][1]