class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        last_pos = 0
        last_neg = 1
        
        ans = [None] * len(nums)
        
        for i in nums:
            if i > 0:
                ans[last_pos] = i
                last_pos += 2
                
            else:
                ans[last_neg] = i
                last_neg += 2
                
        return ans