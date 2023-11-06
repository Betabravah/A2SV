# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue1 = deque([original])
        queue2 = deque([cloned])
        
        while queue1 and queue2:
            cur1 = queue1.popleft()
            cur2 = queue2.popleft()
            
            if cur1 == target:
                return cur2
            
            if cur1.left:
                queue1.append(cur1.left)
                queue2.append(cur2.left)
                
            if cur1.right:
                queue1.append(cur1.right)
                queue2.append(cur2.right)
                
            