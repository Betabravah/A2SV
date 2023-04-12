class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adjacency = defaultdict(set)
        for p1, p2 in dislikes:
            adjacency[p1].add(p2)
            adjacency[p2].add(p1)
            
        colors = defaultdict(int)
        
        def dfs(cur, color):
            
            if colors[cur] != 0:
                if colors[cur] != color:
                    return False
                else:
                    return True
                
                
            colors[cur] = color
            
            
            for child in adjacency[cur]:
                temp = dfs(child, -color)
                
                if not temp:
                    return False
                
            return True
                
            
        for key in adjacency:
            if colors[key] == 0:
                ans = dfs(key, 1)
                if not ans:
                    return False
            
        return True
            
            