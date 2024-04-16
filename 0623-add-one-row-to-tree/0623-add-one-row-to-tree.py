# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy  = TreeNode()
        queue = deque([dummy])
        dummy.left = root
        
        
        for _ in range(depth-1):
            length = len(queue)
            
            for _ in range(length):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)


        for i in queue:
            # if i.left:
                new_left = TreeNode(val)
                
                new_left.left = i.left
                i.left = new_left
                
            # if i.right:
                new_right = TreeNode(val)
                
                new_right.right = i.right
                i.right = new_right
                
        return dummy.left
            