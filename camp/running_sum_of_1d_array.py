class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        running = []
        for num in nums:
            sum += num
            running.append(sum)
        
        return running