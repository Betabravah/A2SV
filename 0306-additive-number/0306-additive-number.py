class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        
        def backtrack(index=0, nums=[]):
            
            if index == len(num) and len(nums) >= 3:
                return True
            
            for i in range(index+1, len(num)+1):
                cur = int(num[index:i])
                
                if len(nums) < 2 or nums[-1] + nums[-2] == cur:
                    if num[index] == '0' and i - index > 1: # if the number has a leading zero
                        continue
                        
                    nums.append(cur)
                    if backtrack(i, nums):
                        return True
                    nums.pop()
                        
                        
        return backtrack()
    