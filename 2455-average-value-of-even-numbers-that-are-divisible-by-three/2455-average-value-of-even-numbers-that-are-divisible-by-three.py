class Solution:
    def averageValue(self, nums: List[int]) -> int:     
        
        ans = total = 0
        for num in nums:
            if num % 6 == 0:
                ans += num
                total += 1
                
                
        return ans // total if total else 0