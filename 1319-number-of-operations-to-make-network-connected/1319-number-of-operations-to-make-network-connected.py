class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for node1, node2 in connections:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        
        
        def dfs(node, parent):
            nonlocal visited
            nonlocal cables
            nonlocal graph

            
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    
                    dfs(child, node)
                else:
                    if child != parent:
                        cables += 1
        
        visited = set()
        cables = 0
        disconnected = 0
        for i in range(n):
            if i not in visited:
                disconnected += 1
                visited.add(i)
                dfs(i, -1)
                
        if cables // 2 >= disconnected - 1:
            return disconnected - 1
        
        return -1
                
                    