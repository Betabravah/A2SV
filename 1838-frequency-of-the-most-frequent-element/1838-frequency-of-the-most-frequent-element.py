class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = 0 # sliding window
        maxFreq = total = 0
        while right < len(nums): # 
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k: # shrink window if we can't increment elements to the highest element
                total -= nums[left]
                left += 1 
            maxFreq = max(maxFreq, right - left + 1)
            right += 1

        return maxFreq