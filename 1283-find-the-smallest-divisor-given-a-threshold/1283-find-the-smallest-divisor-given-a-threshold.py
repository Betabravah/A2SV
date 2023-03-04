class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def feasible(div):
            total = 0
            for num in nums:
                total += ceil((num) / div)
                if total > threshold:
                    return False
            return True
        
        low, high = 1, sum(nums)
        while low <= high:
            mid = low + (high - low) // 2
            
            if feasible(mid):
                high = mid - 1
            else:
                low = mid + 1
                
        return low