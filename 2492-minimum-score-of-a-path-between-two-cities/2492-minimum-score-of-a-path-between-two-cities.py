class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i, j, cost in roads:
            graph[i].append([j, cost])
            graph[j].append([i, cost])
            
            
        queue = deque([[1, inf]])
        visited = set()
        minn = inf
        
        while queue:

            cur, cost = queue.popleft()
            
            
            for child, child_cost in graph[cur]:
                minn = min(minn, child_cost)
                
                if child not in visited:
                    queue.append([child, child_cost])
                    visited.add(child)
            
        return minn
            