class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0 
        blue = 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
            elif i == 2:
                blue += 1
        for i in range(red):
            nums[i] = 0
        for i in range(white):
            nums[red + i] = 1
        for i in range(blue):
            nums[red + white + i] = 2

        print(nums)

        
