class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        
        queue = deque([0])
        
        while queue:
            cur = queue.popleft()
            
            for key in rooms[cur]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
                    
        if len(visited) == len(rooms):
            return True
        
        return False
            