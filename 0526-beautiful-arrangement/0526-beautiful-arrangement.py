class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        nums = list(range(1, n+1))
        
        def dfs(idx):
            nonlocal count
            
            if idx == n:
                count += 1
                
            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                
                if nums[idx] % (idx + 1) == 0 or (idx + 1) % nums[idx] == 0:
                    dfs(idx+1)
                
                nums[i], nums[idx] = nums[idx], nums[i]
                
        dfs(0)
        return count
                
                