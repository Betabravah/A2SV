# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        queue = deque([root])
        
        while queue:

            cur = queue.popleft()
            
            if cur.left:
                graph[cur.left.val].append(cur.val)
                graph[cur.val].append(cur.left.val)
                queue.append(cur.left)
        
            if cur.right:
                graph[cur.right.val].append(cur.val)
                graph[cur.val].append(cur.right.val)
                queue.append(cur.right)                
                
                
                
        
        
        queue = deque([(target.val, 0)])
        
        visited = set([target.val])
        output = []
        
        while queue:
            cur, step = queue.popleft()
            
            if step > k:
                break
            
            if step == k:
                output.append(cur)
                
            
            for neigh in graph[cur]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, step + 1))
                    
                    
        return output
            
            
            
            
            
            
            
            
            
            