class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if '0000' in deadends:
            return -1
        
        queue = deque([('0000', 0)])
        visited = set()
                
        
        def get_neighbours(state):
            nonlocal deadends
            neighbours = []
            
            for i in range(4):
                
                digit = int(state[i])
                
                case1 = state[:i] + str((digit + 1) % 10) + state[i+1:]
                case2 = state[:i] + str((digit - 1) % 10) + state[i+1:]
                
                
                if case1  not in deadends:
                    neighbours.append(case1)
                
                if case2 not in deadends:
                    neighbours.append(case2)
                    
            return neighbours
                
                
        
        
        while queue:
            cur, depth = queue.popleft()
            
            if cur == target:
                return depth
            
            for neighbour in get_neighbours(cur):
                
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, depth + 1))
                    
        return -1
                
                
                
                
                
                
                
            