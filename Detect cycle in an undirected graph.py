from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        noncyclic = 0
        count = [0] * V
        
        for i in range(V):
            for j in adj[i]:
                count[j] += 1
        
                
        queue = deque()
        visited = set()
        for i in range(V):
            if count[i] == 1 or count[i] == 0:
                queue.append(i)
                visited.add(i)
                noncyclic += 1
        
        
        while queue:
            cur = queue.popleft()
            
            for child in adj[cur]:
                count[child] -= 1
                
                if (count[child] == 0 or count[child] == 1) and child not in visited:
                    queue.append(child)
                    visited.add(child)
                    noncyclic += 1
        
        if noncyclic == V:
            return False
        return True
