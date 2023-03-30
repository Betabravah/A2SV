class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        got = False
        while i < len(nums):
            idx = nums[i] - 1
            
            if nums[i] < 0:
                i += 1
                continue
            
            if abs(nums[i]) != i + 1:
                if nums[idx] < 0:
                    if not got:
                        ans.append(nums[i])
                        got = True
                    i += 1
                else:
                    nums[idx], nums[i] = -nums[i], nums[idx]
            else:
                nums[i] = -nums[i]
                i += 1
                
                
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
                return ans
                