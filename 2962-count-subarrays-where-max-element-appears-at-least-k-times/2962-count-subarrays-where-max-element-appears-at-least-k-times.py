class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_count = 0
        max_num = max(nums)
        left = ans = 0
        
        prev = 0
        for i in range(n):
            if nums[i] == max_num:
                max_count += 1
                
            while max_count == k:
                if nums[left] == max_num:
                    max_count -= 1
                left += 1
                
            ans += left
            
        return ans
                
        