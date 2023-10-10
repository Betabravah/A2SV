class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        vector = [0, 0]
        direction = (0, 1)
        
        left = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
        right = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        
        
        for i in instructions:
            if i == 'G':
                vector[0] += direction[0]
                vector[1] += direction[1]
                
            elif i == 'L':
                direction = left[direction]
                
            else:
                direction = right[direction]
        
        
        if (vector[0] == vector[1] == 0) or not (direction[0] == 0 and direction[1] == 1):
            return True
        
        return False
            
                