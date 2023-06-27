class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def dfs(idx):
            if idx == len(requests):
                return 0 if min(degrees) == max(degrees) == 0 else -float('inf')
            
            degrees[requests[idx][0]] -= 1
            degrees[requests[idx][1]] += 1
            
            result = 1 + dfs(idx + 1)
            
            degrees[requests[idx][0]] += 1
            degrees[requests[idx][1]] -= 1
            
            return max(result, dfs(idx + 1))
        
        
        degrees = [0] * n
        return dfs(0)