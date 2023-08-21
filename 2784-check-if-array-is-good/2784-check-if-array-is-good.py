class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        freq = Counter(nums)
        
        for num in freq:
            if num == n:
                if freq[num] != 2:
                    return False
            elif 0 < num < n:
                if freq[num] != 1:
                    return False
            else:
                return False
        return True
                