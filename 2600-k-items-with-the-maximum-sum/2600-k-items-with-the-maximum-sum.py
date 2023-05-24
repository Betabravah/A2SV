class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = ctr = 0
        nums = [numOnes, numZeros, numNegOnes]
        
        for i in range(len(nums)):
            
            if i == 0:
                    j = 1
            elif i == 1:
                j = 0
            else:
                j = -1

            total += nums[i] * j
            ctr += nums[i]
            
            if ctr >= k:
                temp = ctr - k
                
                
                
                
                total -= j * temp
                return total
                
            
            
            
        return total
                    
            
            
            