class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        
        minn = nums[0]
        seen = set([nums[0]])
        
        ans = 0
        
        for idx, i in enumerate(nums):
            if i > minn:
                if i not in seen:
                    ans += len(seen)
                else:
                    ans += (len(seen) - 1)
                
                seen.add(i)
                
        return ans