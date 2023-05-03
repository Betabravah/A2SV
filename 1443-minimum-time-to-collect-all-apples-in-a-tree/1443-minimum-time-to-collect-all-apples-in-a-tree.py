class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            

        visited = set()
        
        def dfs(node, parent):          
            
            distance = 0
            
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                    
                distance += dfs(neigh, node)
                    
            if node != 0 and (hasApple[node] or distance > 0):
                distance += 2
                
            return distance
                    
                
                
        return dfs(0, -1)
