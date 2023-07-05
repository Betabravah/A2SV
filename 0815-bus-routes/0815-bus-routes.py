class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        to_route = defaultdict(set)
        
        for i, route in enumerate(routes):
            for j in route:
                to_route[j].add(i)
                        

                    
        queue = deque([(source, 0)])
        visited = set([source])
        
        while queue:
            cur, buses = queue.popleft()
            
            if cur == target:
                return buses
            
            for bus in to_route[cur]:
                for stop in routes[bus]:
                    if stop not in visited:
                        visited.add(stop)
                        queue.append((stop, buses+1))
                        
                    routes[bus] = [] # seen route
                        
                        
        return -1
                    
        
        