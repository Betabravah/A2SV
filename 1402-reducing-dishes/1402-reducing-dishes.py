class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        nums = sorted(satisfaction,reverse=True)
        
        sum = ans = 0
        for num in nums:
            if(sum + num > 0):
                ans += sum + num
                sum += num
        return ans