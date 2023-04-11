class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            _gcd = nums[i]
            
            for j in range(i, len(nums)):
                _gcd = math.gcd(_gcd, nums[j])
                
                if _gcd == k:
                    count += 1
                    
        return count