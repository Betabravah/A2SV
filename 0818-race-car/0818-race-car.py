class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set((0, 1))
        
        
        while queue:
            pos, speed, level = queue.popleft()
            
            if pos == target:
                return level
            
            # accelerate
            newpos, newspeed = pos + speed, speed * 2
            
            if (newpos, newspeed) not in visited:
                visited.add((newpos, newspeed))
                queue.append((newpos, newspeed, level + 1))
                
            
            # reverse
            if speed > 0:
                newspeed = -1
            else:
                newspeed = 1
            
            if (pos, newspeed) not in visited:
                visited.add((pos, newspeed))
                queue.append((pos, newspeed, level + 1))
                
                
                
        return -1
            