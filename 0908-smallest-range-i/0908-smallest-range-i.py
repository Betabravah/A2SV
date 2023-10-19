class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        minn = min(nums)
        
        maxx += - k
        minn += k
        
        return maxx - minn if maxx > minn else 0