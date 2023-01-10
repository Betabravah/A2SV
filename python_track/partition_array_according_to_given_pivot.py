class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        great = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                great.append(num)

        nums = []
        for num in less:
            nums.append(num)
        for num in equal:
            nums.append(num)
        for num in great:
            nums.append(num)
        
        return nums
   
