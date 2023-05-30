class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        count = [0] * len(edges)
        for i, j in enumerate(edges):
            if j != -1:
                count[j] += 1
                
        
        queue = deque([i for i, j in enumerate(count) if j == 0])
        visited = set(queue)

        
        while queue:
            
            cur = queue.popleft()
            child = edges[cur]
            
            if child != -1:
                count[child] -= 1

                if count[child] == 0:
                    queue.append(child)
                    visited.add(child)
        
        
        if len(visited) == len(edges):
            return -1
        
        ans = -1
        for i in range(len(edges)):
            
            if i not in visited:
                visited.add(i)
                length = 1
                neighbour = edges[i]
                
                while neighbour != i:
                    length += 1
                    visited.add(neighbour)
                    neighbour = edges[neighbour]
                    
                    
                ans = max(ans, length)
                
                
        return ans
                    
                    
                    
        
                        
                
        
            