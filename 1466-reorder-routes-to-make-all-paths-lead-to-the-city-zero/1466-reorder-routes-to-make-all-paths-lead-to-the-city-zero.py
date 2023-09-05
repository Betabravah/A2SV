class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for node1, node2 in connections:
            graph[node1].append([node2, 0])
            graph[node2].append([node1, 1])
            
            
        ans = 0
        queue = deque([0])
        visited = set([0])
        while queue:
            cur = queue.popleft()
            
            for child, val in graph[cur]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
                    
                    if val == 0:
                        ans += 1
                    
        
        return ans 
        