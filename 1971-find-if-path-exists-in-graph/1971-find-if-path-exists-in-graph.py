class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        found = False
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(vertex, visited):
            nonlocal found
            
            if vertex == destination:
                return True
            
            visited.add(vertex)
            
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited)
                
                if found:
                    return True
                
            return False
        

        
        visited = set()
        return dfs(source, visited)