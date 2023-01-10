class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        idx = 0
        nums = []
        while idx < len(positives):
            nums.append(positives[idx])
            nums.append(negatives[idx])
            idx += 1
        return nums
