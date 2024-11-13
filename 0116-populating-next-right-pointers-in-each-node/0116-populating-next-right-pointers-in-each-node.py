"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        if root: queue.append(root)
        
        while queue:
            length = len(queue)
            prev = None
            
            for _ in range(length):
                cur = queue.popleft()
                
                if prev:
                    prev.next = cur
                
                prev = cur
                    
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                    
        return root
                
        
        