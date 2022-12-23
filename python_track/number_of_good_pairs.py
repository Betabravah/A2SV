class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ctr = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] == nums[i]:
                    ctr += 1
        
        return ctr
