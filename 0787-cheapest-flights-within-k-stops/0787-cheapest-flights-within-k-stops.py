class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append([v, w])
            
        heap = []
        heappush(heap, [0, 0, src])
        node_count = defaultdict(lambda: float('inf'))
        node_count[src] = 0
        
        while heap:
            
            cost, count, node = heappop(heap)
            
            node_count[node] = count
                    
            if node == dst and count - 1 <= k:
                return cost
            
            for child, w in graph[node]:
                new_cost = cost + w
                
                if count < node_count[child]:
                    heappush(heap, [new_cost, count + 1, child])
                    
        return -1
                