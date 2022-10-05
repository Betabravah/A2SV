class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = currentSum = 0
        prefixSums = {0:1} # to store prefix sums with their respective count  
        
        for n in nums:
            currentSum += n
            difference = currentSum - k
            
            result += prefixSums.get(difference, 0) # return 0 if difference not in prefixSums
            prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)
            
    
        return result
