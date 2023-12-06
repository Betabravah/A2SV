class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])
        
        for i, j in ghosts:
            cur_dist = abs(i-target[0]) + abs(j-target[1])
            
            if cur_dist <= dist:
                return False
            
        return True