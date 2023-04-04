class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small, large = min(nums), max(nums)
        

        while small != 0:
            large, small = small, large % small
        
        return large
