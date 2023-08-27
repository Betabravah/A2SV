"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        graph = defaultdict(list)
        
        def dfs(node):
            if node in graph:
                return graph[node]
            
            copy = Node(node.val)
            graph[node] = copy
            
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
                
                
            
            return copy
        
        return dfs(node) if node else None
            
            
            
