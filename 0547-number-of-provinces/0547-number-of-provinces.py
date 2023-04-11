class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adjacency = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    adjacency[i].append(j)
                    

                    
        def dfs(row):
            
            visited.add(row)
            
            for neighbour in adjacency[row]:
                if neighbour not in visited:
                    dfs(neighbour)
            
    
    
        visited = set()
        count = 0
        for i in range(n):
                
            if i not in visited:
                count += 1
                dfs(i)
            
                    
        return count

            
        
            