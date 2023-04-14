class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjacency = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                
                if i == j:
                    continue
                    
                    
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                
                if r1 ** 2 >= (y1 - y2) ** 2 + (x1 - x2) ** 2:
 
                    adjacency[i].append(j)
                    
        
        def dfs(bomb, visited):
            
            
            for child in adjacency[bomb]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)
                
                
        max_bombs = 0    
        for i in range(len(bombs)):
            visited = set([i])
            dfs(i, visited)
            max_bombs = max(max_bombs, len(visited))
            
        return max_bombs