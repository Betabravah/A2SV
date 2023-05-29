class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        queue = deque()
        visited = set()
        coins.sort(reverse=True)
        
        for i in coins:
            remaining = amount - i
            if remaining == 0:
                return 1
            
            elif remaining > 0:
                queue.append([remaining, 1])
                visited.add(remaining)

                
        while queue:
            cur, depth = queue.popleft()
            
            for i in coins[::-1]:
                remaining = cur - i
                if remaining == 0:
                    return depth + 1
                
                if remaining >= 0 and remaining not in visited:
                    queue.append([remaining, depth+1])
                    visited.add(remaining)
        
        return -1