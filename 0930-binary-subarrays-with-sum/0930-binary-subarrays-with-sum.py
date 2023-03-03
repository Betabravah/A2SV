class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = collections.Counter({0: 1})
       
        left = prefix = subarrays = 0
        for num in nums:
            prefix += num
            subarrays += counter[prefix - goal]
            counter[prefix] += 1
            
        return subarrays
                
                
                
        