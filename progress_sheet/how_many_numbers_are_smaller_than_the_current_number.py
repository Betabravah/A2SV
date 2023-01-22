class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ctr = 0
        freqList = []
        for i in nums:
            for j in nums:
                if j < i:
                    ctr += 1
            freqList.append(ctr)
            ctr = 0
        return freqList