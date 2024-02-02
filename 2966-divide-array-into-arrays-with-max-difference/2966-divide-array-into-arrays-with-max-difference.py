class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        
        for i in range(1, 3):
            if nums[i] - nums[i-1] > k:
                return []
            
        
        left = 0
        right = i
        ans = []
        for _ in range(3, len(nums), 3):
            if nums[right] - nums[left] > k:
                return []
            
            ans.append(nums[left:right+1])
            
            left += 3
            right += 3
            
            
        if nums[right] - nums[left] > k:
                return []
            
        ans.append(nums[left:right+1])
        return ans