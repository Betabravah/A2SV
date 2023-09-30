class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        def dfs(idx):
            if idx in visited:
                return False

            visited.add(idx)

            if arr[idx] == 0:
                return True
            
            left = idx - arr[idx]
            right = idx + arr[idx]
            
            if left >= 0 and dfs(left):
                return True
            
            if right < len(arr) and dfs(right):
                return True
                
            return False
        
        return dfs(start)