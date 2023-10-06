class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        for i, (u, v) in enumerate(edges):
            graph[u].append([v, succProb[i]])
            graph[v].append([u, succProb[i]])
            
        
        heap = []
        heappush(heap, [-1, start_node])
        
        probability = defaultdict(float)
        probability[start_node] = 1
        visited = set()
        
        
        while heap:
            prob, node = heappop(heap)
            
            if node in visited:
                continue
                
            visited.add(node)
            
            for child, p in graph[node]:
                new_prob = prob * -p
                
                if probability[child] < new_prob:
                    probability[child] = new_prob
                    heappush(heap, [-new_prob, child])
                    
        return probability[end_node]
                