class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        
        for u, v, w in edges:
            self.graph[u].append([v, w])

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append([edge[1], edge[2]])

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [[0, node1]]
        visited = set([node1])
        distances = defaultdict(lambda: float('inf'))
        distances[node1] = 0
        
        while heap:
            cost, node = heappop(heap)
            
            if cost > distances[node]:
                continue
                
            visited.add(node)
            
            if node == node2:
                return cost
            
            for child, c in self.graph[node]:
                
                new_cost = distances[node] + c
                
                if new_cost < distances[child]:
                    distances[child] = new_cost
                    heappush(heap, (new_cost, child))    
                
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)