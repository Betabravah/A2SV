class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        newList = []
        for num in nums:
            revList = []
            while num > 0:
                digit = num % 10
                revList.append(str(digit))
                num = num // 10
            reversed = ''.join(revList)

            newList.append(int(reversed))
        return len(Counter(nums+newList))
