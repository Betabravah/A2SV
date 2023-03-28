class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        rangee = [0] * (n + 1)
        
        for start, end in requests:
            rangee[start] += 1
            rangee[end + 1] -= 1
            
        prefix = []
        running = 0
        for i in range(n):
            running += rangee[i]
            prefix.append(running)
            
        prefix.sort()
        nums.sort()
        
        ans = 0
        for i in range(n):
            ans += prefix[i] * nums[i]
        return ans % (10**9 + 7)
        
        
            
            