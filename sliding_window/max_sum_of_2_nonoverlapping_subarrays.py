class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int, unused: bool = True) -> int:
        leftSum = rightSum = 0
        maxSum = maxLeft = 0
        
        for i in range(firstLen): # window of firstLen size
            leftSum += nums[i]
        maxLeft = leftSum
        
        for i in range(secondLen): # window of secondLen size
            rightSum += nums[i + firstLen]
        maxSum = maxLeft + rightSum
        
        for i in range(len(nums)): # sliding both windows
            try:
                if i >= firstLen:
                    leftSum += nums[i] - nums[i - firstLen]
                    rightSum += nums[i + secondLen] - nums[i]
                maxLeft = max(maxLeft, leftSum)
                maxSum = max(maxSum, maxLeft + rightSum)
            except Exception:
                break

        if unused:
            return max(maxSum, self.maxSumTwoNoOverlap(nums, secondLen, firstLen, False))
        else:
            return maxSum