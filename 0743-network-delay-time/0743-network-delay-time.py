class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, target, time in times:
            graph[src].append((target, time))
        
        costs = defaultdict(lambda: float('inf'))
        costs[k] = 0
            
        heap = []
        heappush(heap, (0, k))
        
        visited = set()
        
        while heap:
            cost, node = heappop(heap)
            
            if node in visited:
                continue
                
            visited.add(node)
            
            for child, c in graph[node]:
                new_cost = cost + c
                
                if new_cost < costs[child]:
                    costs[child] = new_cost
                    heappush(heap, (new_cost, child))           
                    
        
        if len(visited) == n:
            ans = 0
            for i in costs.values():
                ans = max(ans, i)
                
            return ans
        return -1