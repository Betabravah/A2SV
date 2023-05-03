class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        adjacency = defaultdict(list)
        
        
        for node1, node2 in edges:
            
            adjacency[node1].append(node2)
            adjacency[node2].append(node1)
            
        
        output = [0] * n
        label = defaultdict(int)
        seen = defaultdict(int)
        visited = set([0])
        
        def dfs(node):
            prev = seen[labels[node]]
            
                        
            for neighbour in adjacency[node]:
                
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
                    
            seen[labels[node]] += 1
            output[node] = seen[labels[node]] - prev
                    
            
        dfs(0)
        return output
                    
        
        