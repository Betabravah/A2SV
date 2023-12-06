class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        player = (abs(target[0]) + abs(target[1]))

        for ghost in ghosts:
            val = (abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]))
            if val <= player:
                return False
        
        return True
