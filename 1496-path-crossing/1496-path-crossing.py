class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0,0)])
        
        cur = [0, 0]
        for i in path:
            
            if i == "N":
                cur[1] += 1
            elif i == "S":
                cur[1] -= 1
            elif i == "E":
                cur[0] += 1
            else:
                cur[0] -= 1
                
                
            tup = tuple(cur)
            if tup in visited:
                return True
            
            visited.add(tup)
            
        return False